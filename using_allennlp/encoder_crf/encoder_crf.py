"""
@Time    :2019/10/8 11:54
@Author  : 梁家熙
@Email:  :11849322@mail.sustech.edu.cn
"""

import logging
from typing import Dict, Optional, List, Any

from allennlp.models import Model
from overrides import overrides
import torch
from torch.nn.modules.linear import Linear

from allennlp.data import Vocabulary
from allennlp.modules import Seq2SeqEncoder, TimeDistributed, TextFieldEmbedder
from allennlp.modules import ConditionalRandomField, FeedForward
from allennlp.modules.conditional_random_field import allowed_transitions

from allennlp.nn import RegularizerApplicator
import allennlp.nn.util as util
from allennlp.training.metrics import CategoricalAccuracy, SpanBasedF1Measure
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

@Model.register("encoder_and_crf", exist_ok=True)
class Encoder_crf(Model):
    def __init__(self, vocab: Vocabulary,
                 text_field_embedder: TextFieldEmbedder,
                 encoder: Seq2SeqEncoder,
                 feedforward: Optional[FeedForward] = None,
                 dropout: Optional[float] = None,
                 regularizer: Optional[RegularizerApplicator] = None) -> None:

        super().__init__(vocab, regularizer)
        label_namespace = 'labels'
        self.label_namespace = label_namespace
        self.text_field_embedder = text_field_embedder

        self.num_tags = self.vocab.get_vocab_size(label_namespace)
        self.encoder = encoder

        if dropout:
            self.dropout = torch.nn.Dropout(dropout)
        else:
            self.dropout = None

        self._feedforward = feedforward

        if feedforward is not None:
            output_dim = feedforward.get_output_dim()
        else:
            output_dim = self.encoder.get_output_dim()
        self.tag_projection_layer = TimeDistributed(Linear(output_dim,
                                                           self.num_tags))

        # if  constrain_crf_decoding and calculate_span_f1 are not
        # provided, (i.e., they're None), set them to True
        # if label_encoding is provided and False if it isn't.


        self.label_encoding = 'BIOUL'
        labels = self.vocab.get_index_to_token_vocabulary(label_namespace)
        constraints = allowed_transitions(self.label_encoding, labels)


        self.include_start_end_transitions = True
        self.crf = ConditionalRandomField(
            self.num_tags, constraints,
            include_start_end_transitions=self.include_start_end_transitions
        )

        self.metrics = {
            "accuracy": CategoricalAccuracy(),
            "accuracy3": CategoricalAccuracy(top_k=3)
        }

        self._f1_metric = SpanBasedF1Measure(vocab,
                                             tag_namespace=label_namespace,
                                             label_encoding=self.label_encoding)

    def forward(self, abstract, labels = None, metadata = None):
        embedded_text_input = self.text_field_embedder(abstract)
        mask = util.get_text_field_mask(abstract)

        if self.dropout:
            embedded_text_input = self.dropout(embedded_text_input)

        encoded_text = self.encoder(embedded_text_input, mask)

        if self.dropout:
            encoded_text = self.dropout(encoded_text)

        if self._feedforward is not None:
            encoded_text = self._feedforward(encoded_text)

        # shape: (batch_size, seq_len, embedding_dim)
        logits = self.tag_projection_layer(encoded_text)
        best_paths = self.crf.viterbi_tags(logits, mask)

        predicted_tags = [x for x, y in best_paths]

        output = {"logits": logits, "mask": mask, "tags": predicted_tags, 'metadata': metadata}

        # 训练阶段与验证阶段
        if labels is not None:
            log_likelihood = self.crf(logits, labels, mask)
            output["loss"] = -log_likelihood

            class_probabilities = logits * 0.
            for i, instance_tags in enumerate(predicted_tags):
                for j, tag_id in enumerate(instance_tags):
                    class_probabilities[i, j, tag_id] = 1
            for metric in self.metrics.values():
                # prediction 比 golden_label 多一个 num of classes 维度
                metric(class_probabilities, labels, mask.float())
            self._f1_metric(class_probabilities, labels, mask.float())

            # 如果验证阶段，我们还想看一下解码后的效果
            if not self.training:
                decode_data: Dict = self.decode(output)
                if len(decode_data) != 0:
                    print(f" \033[1;35m {''.join(list(decode_data.items())[0])}\033[0m")
        # 测试阶段
        else:
            output['predict_title'] = [self.decode(output), ]
        return output

    @overrides
    def decode(self, output_dict: Dict[str, torch.Tensor]):
        ret = []
        for instance_tags in output_dict['tags']:
            t = []
            for tag in instance_tags:
                t.append(self.vocab.get_token_from_index(tag, namespace=self.label_namespace))
            ret.append(t)
        # print(f'\033[1;33;44m{ret[0]}\033[0m')

        ans = {'text': [], 'predict_title': []}

        for batch_index, (text, tags) in enumerate(zip(output_dict['metadata'], ret)):
            i = 0
            t = ''
            while i < len(text):
                a = tags[i][0]
                if a == 'U':
                    t += str(text[i])
                else:
                    # 这种解码是一直找到 L 为止。
                    if a == 'B':
                        j = i
                        while j <len(text) and tags[j][0] != 'L':
                            j += 1
                        t += "".join([str(w) for w in text[i: j+1]])
                i += 1
            ans['text'].append("".join(w.text for w in text))
            ans['predict_title'].append(t)

        return ans

    @overrides
    def get_metrics(self, reset: bool = False):
        metrics_a = {metric_name: metric.get_metric(reset) for
                             metric_name, metric in self.metrics.items()}
        metrics_b = self._f1_metric.get_metric(reset)
        metrics_a.update(metrics_b)
        return metrics_a




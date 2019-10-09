"""
@Time    :2019/10/8 11:36
@Author  : 梁家熙
@Email:  :11849322@mail.sustech.edu.cn
"""
import json

from allennlp.data import Token

from tqdm import tqdm
import random
from pprint import pprint
import os
import collections
from typing import List, Dict, Tuple
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
from typing import Dict
import json
import logging

from overrides import overrides

from allennlp.common.file_utils import cached_path
from allennlp.data.dataset_readers.dataset_reader import DatasetReader
from allennlp.data.fields import LabelField, TextField, SequenceLabelField, MetadataField
from allennlp.data.instance import Instance
from allennlp.data.tokenizers import Tokenizer, WordTokenizer
from allennlp.data.token_indexers import TokenIndexer, SingleIdTokenIndexer


@DatasetReader.register("zhaiyao_datareader")
class zhaiyao_datareader(DatasetReader):
    def __init__(self,
                 lazy: bool = False,
                 token_indexers: Dict[str, TokenIndexer] = None,
                 ) -> None:

        super().__init__(lazy)
        self._token_indexers = token_indexers or {"tokens": SingleIdTokenIndexer()}

    @overrides
    def _read(self, file_pth):
        with open(file_pth) as f:
            data = json.load(f)
        for dct in data:
            abstract = dct['abstract']
            title = dct['title']
            labels = dct['labels']
            yield self.text_to_instance(abstract, labels, title)

    @overrides
    def text_to_instance(self, abstract: str, labels: List[str] = None, title: str = None):
        # 以字为单位
        abstract = [Token(w) for w in abstract]
        abstract_field = TextField(abstract, self._token_indexers)
        meta_field = MetadataField(abstract)
        fields = {'abstract': abstract_field, 'metadata': meta_field}
        if labels:
            labels_field = SequenceLabelField(labels, abstract_field)

            t = {'labels': labels_field}
            fields.update(t)

        return Instance(fields)







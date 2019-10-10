"""
@Time    :2019/10/10 9:06
@Author  : 梁家熙
@Email:  :11849322@mail.sustech.edu.cn
"""
import json
from tqdm import tqdm
import random
from pprint import pprint
import os
import collections
from typing import List, Dict, Tuple
import logging

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


@DatasetReader.register("simple_seq2seq_reader")
class seq2seq_datareader(DatasetReader):
    def __init__(self, lazy = False, token_indexers = None):
        super().__init__(lazy)
        self._token_indexers = token_indexers or {'tokens': SingleIdTokenIndexer()}
    @overrides
    def _read(self, file_path: str):
        with open(file_path) as f:
            data = json.load(f)
        for dct in data:
            abstract = dct['abstract']
            title = dct['title']
            yield self.text_to_instance(abstract, title)
    @overrides
    def text_to_instance(self, abstract, title = None):
        abstract = [Token(w) for w in abstract]
        abstract_field = TextField(abstract, self._token_indexers)
        fields = {'source_tokens': abstract_field}
        if title:
            title_field = TextField([Token(w) for w in title], self._token_indexers)
            fields['target_tokens'] = title_field
        return Instance(fields)

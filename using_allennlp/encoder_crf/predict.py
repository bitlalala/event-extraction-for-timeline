"""
@Time    :2019/10/9 9:44
@Author  : 梁家熙
@Email:  :11849322@mail.sustech.edu.cn
"""
import json
import logging
import os
from typing import Dict, Union, List, Set

import numpy
import torch

from allennlp.common.checks import ConfigurationError
from allennlp.common.params import Params
from allennlp.common.registrable import Registrable
from allennlp.data import Instance, Vocabulary
from allennlp.data.dataset import Batch
from allennlp.nn import util
from allennlp.nn.regularizers import RegularizerApplicator
import torch
from allennlp.data.dataset import Batch
from allennlp.models import load_archive
from tqdm import tqdm
import random
from pprint import pprint
import os
import collections
from typing import List, Dict, Tuple
import logging

from using_allennlp.encoder_crf.datareader import zhaiyao_datareader

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
from overrides import overrides

from allennlp.common.util import JsonDict, import_submodules
from allennlp.data import Instance
from allennlp.predictors.predictor import Predictor

@Predictor.register('bistm_crf_predictor', exist_ok=True)
class bistm_crf_predictor(Predictor):

    def predict_json(self, inputs: JsonDict):
        abstract = inputs['abstract']
        return self.predict_line(abstract)

    def predict_line(self, line: str):
        instance = self._dataset_reader.text_to_instance(line)
        ouput_dict = self.predict_instance(instance)

        # return {'predict_title': ouput_dict['predict_title']}
        return {'input': line, 'predict_title': ouput_dict['predict_title']}


if __name__ == '__main__':
    import_submodules('using_allennlp')
    serialization_dir = "/home/liangjiaxi/TMP_PROJECT/pingan_event_extraction/tmp/debugger_train"
    archive = load_archive(os.path.join(serialization_dir, 'model.tar.gz'))
    predictor = Predictor.from_archive(archive, 'bistm_crf_predictor',
                                  dataset_reader_to_load = "zhaiyao_datareader")
    line = '东土科技(300353)公告，公司此前曾披露，控股股东、实控人、董事长李平拟于2017年10月23日起12个月内增持不低于1亿元，累计增持比例不超本公司已发行股份的2%。李平于2018年1月31日至2月8日增持212.68万股，增持资金2431万元。由于相关融资增持监管政策变化导致无法筹措增持资金，李平现申请终止履行未实施部分的增持计划。'
    a = predictor.predict_line(line)
    print(a)
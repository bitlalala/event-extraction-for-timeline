"""
@Time    :2019/9/30 9:58
@Author  : 梁家熙
@Email:  :11849322@mail.sustech.edu.cn
"""
import json

import jieba
from tqdm import tqdm
import random
from pprint import pprint
import os
import collections
from typing import List, Dict, Tuple
import logging

from dataprocess_scripts.meta_class import Biaozhu

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class bioul_biaozhu(Biaozhu):
    def __init__(self, pth: str, yuzhi_ratio: float):
        super(bioul_biaozhu, self).__init__(pth, yuzhi_ratio)

    def biaozhu(self, source, spans: List) -> List[str]:
        label_lst = ['O', ] * len(source)
        for span in spans:
            a, b = span
            # 因为是左闭右开
            if a == b:
                label_lst[a] = 'U-None'
            else:
                for i in range(a, b + 1):
                    if i == a:
                        label_lst[i] = 'B-None'
                    elif i == b:
                        label_lst[i] = 'L-None'
                    else:
                        label_lst[i] = 'I-None'
        return label_lst

    def tokenize(self, source: str):
        return jieba.lcut(source)

if __name__ == '__main__':
    a = bioul_biaozhu('../data/news_data_09_29.json', 0.7)
    a.run('./temp.json')
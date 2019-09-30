"""
@Time    :2019/9/30 9:58
@Author  : 梁家熙
@Email:  :11849322@mail.sustech.edu.cn
"""
import json
import pkuseg

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
                if label_lst[a] == 'O':
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

# 结巴分词器
class bioul_biaozhu_jieba(bioul_biaozhu):
    def tokenize(self, source: str):
        return list(jieba.cut_for_search(source))

class bioul_biaozhu_pkuseg(bioul_biaozhu):
    def __init__(self, pth: str, yuzhi_ratio: float):
        super(bioul_biaozhu_pkuseg, self).__init__(pth, yuzhi_ratio)
        self.tokenizer =  pkuseg.pkuseg(model_name='news')
    def tokenize(self, source: str):
        return self.tokenizer.cut(source)


if __name__ == '__main__':
    pth = '../data/news_data_09_29.json'
    # a = bioul_biaozhu_jieba(pth, 0.7)
    # a.run('./jieba.json')

    b= bioul_biaozhu_pkuseg(pth, 0.7)
    b.run('./pkuseg.json')

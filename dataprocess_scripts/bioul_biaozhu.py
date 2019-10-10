"""
@Time    :2019/9/30 9:58
@Author  : 梁家熙
@Email:  :11849322@mail.sustech.edu.cn
"""
import json
import pkuseg
import jieba
from overrides import overrides

from tqdm import tqdm
import random
from pprint import pprint
import os
import collections
from typing import List, Dict, Tuple
import logging

from dataprocess_scripts.meta_class import Biaozhu
from dataprocess_scripts.myutils import longestCommonSubsequence

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger.setLevel(logging.DEBUG)

class bioul_biaozhu(Biaozhu):
    def __init__(self, pth: str, yuzhi_ratio: float):
        super(bioul_biaozhu, self).__init__(pth, yuzhi_ratio)

    def biaozhu(self, source, spans: List) -> List[str]:
        label_lst = ['O', ] * len(source)
        try:
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
        except:
            print()
        return label_lst

# 结巴分词器
class bioul_biaozhu_jieba(bioul_biaozhu):
    def tokenize(self, source: str, abstract = None) -> List[str]:
        return list(jieba.cut_for_search(source))

# pkuseg 分词器
class bioul_biaozhu_pkuseg(bioul_biaozhu):
    def __init__(self, pth: str, yuzhi_ratio: float):
        super(bioul_biaozhu_pkuseg, self).__init__(pth, yuzhi_ratio)
        self.tokenizer =  pkuseg.pkuseg(model_name='news')

    def tokenize(self, source: str, abstract = None) -> List[str]:
        return self.tokenizer.cut(source)

# 最长公共子序列
class zuichanggongongzixulie(bioul_biaozhu):
    def tokenize(self, source: str, abstract) -> List[str]:
        _, common_text, _ = longestCommonSubsequence(abstract, source)
        return common_text

    @overrides
    def search_targetlist_in_string(self, text1: str, text2: str, yuzhi: int, zuobiyoukai: bool):
        if isinstance(text1, list) or isinstance(text2, list):
            print()
        length, common_text, index_lst = longestCommonSubsequence(text1, text2)
        # 不满足阈值则略过
        if length < yuzhi:
            return []
        if zuobiyoukai:
            return [[w, w+1] for w in index_lst]
        else:
            return [[w, w] for w in index_lst]




if __name__ == '__main__':
    # pth = '../data/news_data_09_29.json'
    # a = bioul_biaozhu_jieba(pth, 0.7)
    # a.run('./jieba_0_7.json')
    #
    # b= bioul_biaozhu_pkuseg(pth, 0.7)
    # b.run('./pkuseg_0_7.json')
    #
    # a = bioul_biaozhu_jieba(pth, 0.9)
    # a.run('./jieba_0_9.json')
    #
    # b= bioul_biaozhu_pkuseg(pth, 0.9)
    # b.run('./pkuseg_0_9.json')
    #
    # a = bioul_biaozhu_jieba(pth, 1)
    # a.run('./jieba_1.json')
    #
    # b= bioul_biaozhu_pkuseg(pth, 1)
    # b.run('./pkuseg_1.json')

    pth = '../data/news_data_09_29.json'
    a = zuichanggongongzixulie(pth, 0.7)
    a.run('./zuichanggongongzixulie_0_7.json')

    a = zuichanggongongzixulie(pth, 0.9)
    a.run('./zuichanggongongzixulie_0_9.json')

    # a = zuichanggongongzixulie(pth, 1)
    # a.run('./zuichanggongongzixulie_1.json')
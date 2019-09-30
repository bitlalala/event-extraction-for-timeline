"""
@Time    :2019/9/30 10:14
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

from dataprocess_scripts.bioul_biaozhu import bioul_biaozhu

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


from unittest import TestCase

class Test_bioul(TestCase):
    def setUp(self):
        self.obj = bioul_biaozhu('../data/news_data_09_29.json', 0.7)





    def test_search_targetlist_in_string(self):
        abstract = "圆通速递(600233)9月24日晚间公告，20.38亿股限售股将于9月30日上市流通，占公司总股本的71.85%。"
        fenci = ["圆通","速递","：","20.38","亿股","限售","股","9","月","30","日","上市","流通","占","总","股本","71%"]
        self.assertListEqual(self.obj.search_targetlist_in_string(abstract, fenci, 1, False),
                             [[0, 1], [2, 3], [22, 26], [27, 28], [29, 30], [28, 28], [12, 12], [13, 13], [36, 37],
                              [16, 16], [39, 40], [41, 42], [44, 44], [47, 47], [48, 49]])


    def test_tokenize(self):
        title = "圆通速递：20.38亿股限售股9月30日上市流通占总股本71%"
        fenci = ["圆通", "速递", "：", "20.38", "亿股", "限售", "股", "9", "月", "30", "日", "上市", "流通", "占", "总", "股本", "71%"]

        a = self.obj.tokenize(title)
        self.assertListEqual(a, fenci)

# # """
# # @Time    :2019/9/30 10:59
# # @Author  : 梁家熙
# # @Email:  :11849322@mail.sustech.edu.cn
# # """
# # import json
# # from tqdm import tqdm
# # import random
# # from pprint import pprint
# # import os
# # import collections
# # from typing import List, Dict, Tuple
# # import logging
# #
# # logger = logging.getLogger(__name__)
# # logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# # import jieba
# # from pyhanlp import *
# #
# # s = "圆通速递：20.38亿股限售股9月30日上市流通占总股本71%"
# # print(jieba.lcut_for_search(s))
# #
# # print(HanLP.segment(s))
# dct = {
#     "abstract": "圆通速递(600233)9月24日晚间公告，20.38亿股限售股将于9月30日上市流通，占公司总股本的71.85%。",
#     "title": "圆通速递：20.38亿股限售股9月30日上市流通占总股本71%",
#     "fenci": [
#       "圆通",
#       "速递",
#       "：",
#       "20.",
#       "38亿股",
#       "限售",
#       "股",
#       "9月30日",
#       "上市",
#       "流通",
#       "占",
#       "总",
#       "股本",
#       "71%"
#     ],
#     "labels": [
#       "B-None",
#       "I-None",
#       "I-None",
#       "L-None",
#       "O",
#       "O",
#       "O",
#       "O",
#       "O",
#       "O",
#       "O",
#       "O",
#       "O",
#       "O",
#       "O",
#       "O",
#       "O",
#       "O",
#       "O",
#       "O",
#       "O",
#       "O",
#       "B-None",
#       "I-None",
#       "I-None",
#       "I-None",
#       "I-None",
#       "I-None",
#       "I-None",
#       "I-None",
#       "L-None",
#       "O",
#       "O",
#       "O",
#       "B-None",
#       "I-None",
#       "I-None",
#       "I-None",
#       "O",
#       "O",
#       "O",
#       "B-None",
#       "I-None",
#       "I-None",
#       "I-None",
#       "I-None",
#       "I-None",
#       "I-None",
#       "I-None",
#       "L-None",
#       "O",
#       "U-None",
#       "O",
#       "O",
#       "O",
#       "B-None",
#       "I-None",
#       "I-None",
#       "I-None",
#       "I-None",
#       "I-None",
#       "I-None",
#       "I-None",
#       "L-None",
#       "O",
#       "U-None",
#       "O",
#       "O",
#       "B-None",
#       "I-None",
#       "L-None",
#       "O",
#       "O",
#       "O",
#       "O",
#       "O",
#       "O",
#       "O",
#       "O"
#     ]
#   }
# for a, b in zip(dct['abstract'], dct["labels"]):
#     if not b.startswith('O'):
#       print(a, end="")
from dataprocess_scripts.myutils import show_extract_info, compare_2_dct_lst
import json
with open('../dataprocess_scripts/pkuseg_0.9.json') as f:
    dct_lsta = json.load(f)
# show_extract_info(dct_lst)

with open('../dataprocess_scripts/jieba_0.9.json') as f:
    dct_lstb = json.load(f)
# show_extract_info(dct_lst)
compare_2_dct_lst(dct_lsta, dct_lstb)
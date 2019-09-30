"""
@Time    :2019/9/29 15:26
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
import jieba

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def get_dct_from_file(pth: str):
    "得到数据"
    with open(pth) as f:
        for line in f.readlines():
            yield json.loads(line)


flag = True
def tokenize(s: str, mode = 'jieba'):
    "分词"
    global flag
    if mode == 'jieba':
        if flag:
            logger.info(f"using {mode} to tokenize")
            flag = False
        return jieba.lcut(s)

    raise Exception("请选择分词器（mode）")

def search_targetlist_in_string(string: str, target_lst: List, zuo_bi_you_kai = True):
    "从字符串中搜索 词 出现的位置"
    if not (isinstance(string, str) and isinstance(target_lst, list)):
        raise Exception

    for target in target_lst:
        if target not in string:
            continue
        # 注意范围是左闭右开， 还是左闭右闭
        if zuo_bi_you_kai:
            yield [string.index(target), len(target)]
        else:
            yield [string.index(target), len(target) - 1]

def show_extract_info(dct_list: List[Dict]):
    for dct in dct_list:
        for a, b in zip(dct['abstract'], dct["labels"]):
            if not b.startswith('O'):
                print(a, end="")
        print()

def _show(dct):
    for a, b in zip(dct['abstract'], dct["labels"]):
        if not b.startswith('O'):
            print(a, end="")

def compare_2_dct_lst(a, b):
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]['abstract'] == b[j]['abstract']:
                print('|', end='')
                _show(a[i])
                print('|', end='')
                _show(b[j])
                print('|', end='')
                print()






if __name__ == '__main__':
    # 确认 logger只输出一次
    # 2019-09-29 17:45:39,328 - __main__ - INFO - using jieba to tokenize
    data = ["一类是我们知道怎么去通过算法将输入转化为输出，通过学习此类模式得到相应输出结果。",
            '另一类是寻找不到此类模式，通过深度学习去做。',
            '另一类是寻找不到此类模式，通过深度学习去做。',
            '另一类是寻找不到此类模式，通过深度学习去做。'
            ]
    for d in data:
        print(tokenize(d))

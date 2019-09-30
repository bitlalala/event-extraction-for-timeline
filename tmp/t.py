
"""
@Time    :2019/9/29 15:34
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

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def search_targetlist_in_string(s: str, target_lst: List[str], yuzhi: int, zuobiyoukai: bool):
    if not (isinstance(s, str) and isinstance(target_lst, list)):
        raise Exception

    ans = []
    pre = 0
    for t in target_lst:
        if t not in s:
            continue
        index = s[pre: ].index(t)
        if zuobiyoukai:
            ans.append([pre + index, pre + index + len(t)])
        else:
            ans.append([pre + index, pre + index + len(t) - 1])
        pre = index

    # 不满足阈值的就返回为空
    if len(ans) >= yuzhi:
        return ans
    else:
        return []
s = "安装步骤在官方安装上很清楚"
target_lst = ["安装", "在", "安装", "清楚"]
print(search_targetlist_in_string(s, target_lst, 0, False))

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
import jieba

s = "德邦股份(603056)9月25日晚间公告，自7月3日起至公告日止，公司及控股子公司累计获得与收益相关的各类政府补助共计7086万元。"
print(s.index('9月26'))
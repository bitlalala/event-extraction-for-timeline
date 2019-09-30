"""
@Time    :2019/9/29 17:33
@Author  : 梁家熙
@Email:  :11849322@mail.sustech.edu.cn
所有 _ 开头的都认为是仅在本文件内使用的小函数
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

from dataprocess_scripts.myutils import get_dct_from_file, tokenize, search_targetlist_in_string




def labeling_data(pth: str):
    "标注函数"
    for dct in tqdm(get_dct_from_file(pth), desc="labeling_data: "):
        abstract = dct['abstract'].strip()
        title = dct['title'].strip()
        _a(abstract, )





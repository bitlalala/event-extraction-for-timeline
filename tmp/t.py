
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

import pkuseg

seg = pkuseg.pkuseg(model_name='news')           # 以默认配置加载模型
text = seg.cut('圆通速递：20.38亿股限售股9月30日上市流通占总股本71%')  # 进行分词
print(text)
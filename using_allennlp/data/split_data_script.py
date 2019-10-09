"""
@Time    :2019/10/8 14:06
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


if __name__ == '__main__':
    file_pth = '/home/liangjiaxi/TMP_PROJECT/pingan_event_extraction/dataprocess_scripts/pkuseg_0_7.json'
    with open(file_pth) as f:
        data = json.load(f)
    random.shuffle(data)
    i = int(len(data) * 0.7)
    j = int(len(data) * 0.9)
    train = data[: i]
    dev = data[i: j]
    test = data[j: ]
    filename = file_pth.split(r'/')[-1].split('.')[0]
    with open(filename+'_train.json', 'w') as f:
        json.dump(train, f, ensure_ascii=False, indent=2)
    with open(filename+'_dev.json', 'w') as f:
        json.dump(dev, f, ensure_ascii=False, indent=2)
    with open(filename+'_test.json', 'w') as f:
        json.dump(test, f, ensure_ascii=False, indent=2)

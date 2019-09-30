"""
@Time    :2019/9/30 9:13
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

from dataprocess_scripts.myutils import get_dct_from_file

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class Biaozhu():
    def __init__(self, pth: str, yuzhi_ratio: float):
        self.pth = pth
        self.yuzhi_ratio = yuzhi_ratio

    def biaozhu(self, source: str, spans) -> List[str]:
        raise NotImplementedError

    def run(self, write_file = None):
        ans = []
        for dct in tqdm(get_dct_from_file(self.pth), desc="打标签中~  "):
            abstract = dct['abstract'].strip()
            title = dct['title'].strip()
            target_lst = self.tokenize(title)
            spans = self.search_targetlist_in_string(abstract, target_lst, yuzhi= int(len(target_lst) * self.yuzhi_ratio), zuobiyoukai=False)
            if len(spans) == 0:
                logger.info(f"没有达到阈值：\n Title:\n{title}\n abstract{abstract}")
                continue
            label_lst = self.biaozhu(abstract, spans)

            ans.append({'abstract': abstract, "title": title, "fenci": target_lst,'labels': label_lst})

        if write_file:
            logger.debug("写文件中。。。")
            with open(write_file, 'w', encoding='utf-8') as f:
                json.dump(ans, f, ensure_ascii=False, indent=2)
        return ans


    def search_targetlist_in_string(self, s: str, target_lst: List[str], yuzhi: int, zuobiyoukai: bool):
        if not (isinstance(s, str) and isinstance(target_lst, list)):
            raise Exception
        ans = []
        for t in target_lst:
            if t not in s:
                continue
            if zuobiyoukai:
                ans.append([s.index(t), s.index(t) +  len(t)])
            else:
                ans.append([s.index(t), s.index(t) + len(t) - 1])
        if len(ans) >= yuzhi:
            return ans
        else:
            return []

    def tokenize(self, source: str) -> List[str]:
        raise NotImplementedError


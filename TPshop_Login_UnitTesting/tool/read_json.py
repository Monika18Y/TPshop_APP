# 导包
import json


def read_json(filename):
    filepath = "../data/" + filename
    # 打开文件并调用 load方法
    with open(filepath, "r", encoding="utf-8")as f:
        return json.load(f)

#!/Users/dengjinxi/mambaforge/envs/yuki/bin/python
# -*- coding: UTF-8 -*-
# 文件夹底下的所有文件，将所有的<div>和</div>相关标签去掉。删除<div>，将</div>替换为回车。
import os
import logging
import re
from pathlib import Path

def change_file(path):
# 打开文件，读取所有内容
    if len(re.findall(r'in.*txt', path)) == 0:
        return

    out = ""
    with open(path, 'r') as file:
        
        fileinfo = file.read()
        # 正则表达式 *? 表示非贪婪模式
        out = re.sub(re.compile(r'<div.*?>'), '', fileinfo)
        out = re.sub(re.compile(r'</div.*?>'), '\n', out)

    if out != "" and out != fileinfo:
        print("修复文件: " + path)
        with open(path, 'w') as file:
            file.write(out)

# 写入修改的内容

def parse_dir(dir):
    file_list = os.listdir(dir)
    parent_dir = Path(dir)
    for element in file_list:
        sub_path = parent_dir / element
        if os.path.isdir(sub_path):
            # 文件夹，继续递归
            parse_dir(str(sub_path.absolute()))
        else:
            # 文件，执行正则替换
            change_file(str(sub_path.absolute()))
    

def main():
    # check self DIR
    # root_dir = os.getcwd()
    root_dir = "/Users/dengjinxi/workspace/personal/cf/contest/"
    print("cf文件检验工具，执行根目录: " + root_dir)

    parse_dir(root_dir)
    

if __name__ == "__main__":
    main()

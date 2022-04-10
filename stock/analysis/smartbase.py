import os
import json
from stock.base.myfile import getDataDirBase

class SmartValue:
  code = ''
  value = 0.0
  msg = ''
  def __init__(self, code, value, msg=''):
    self.code = code
    self.value = value
    self.msg = msg
  def format(self):
    return "code = {0} value = {1} msg = {2}".format(self.code, self.value, self.msg)


class SmartBase(object):
  # 1. 构造函数
  def __init__(self, name):
    self.dirname = getDataDirBase() + name + "/"
    self.suss = False
    self.table = []
  
  # 2. 当前name目录下的文件列表
  def fileList(self):
    try :
      codelist = os.listdir(self.dirname)
      names = [code for code in codelist if os.path.isfile(self.dirname + code )]
      return names
    except :
      self.suss = False
    return []

  # 3. 读取内容
  def read(self, code):
    self.table = []
    try :
      with open(self.dirname + code, 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            lines[i] = lines[i].rstrip('\n')
        return lines
    except :
      self.suss = False
    return []

  # 3. 解析code文件的的内容，放在table中
  def parse(self, code):
    self.table = []
    lines = self.read(code)
    # print(lines)
    for line in lines:
      try:
        items = line.split(",")
        items[1] = int(items[1])
        items[2] = int(float(items[2]))
        items[3] = int(float(items[3]))
        items[4] = int(float(items[4]))
        items[5] = int(float(items[5]))
        self.table.append(items)
      except Exception as e:
        continue

  # 启动分析
  def analysis(self, code):
    print(self.table)
    return

  # 4.
  def run(self):
    codes = self.fileList()
    results = []
    for code in codes:
      try:
        self.parse(code)
        value = self.analysis(code)
        results.append(SmartValue(code, value))
      except Exception as e:
        self.suss = False
        print(e)
    results.sort(key=lambda v:v.value, reverse=True)
    return results



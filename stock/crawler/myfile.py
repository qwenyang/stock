import os
from pathlib import Path

BASE_STOCK_DATA_DIR = '/data/stock/'

class StockFileBase(object):
  def __init__(self, name, code):
    self.name = name
    self.code = code
    self.filename = BASE_STOCK_DATA_DIR+name+'/'+code
    mypath = Path(BASE_STOCK_DATA_DIR+name)
    if not mypath.exists():
      os.mkdir(BASE_STOCK_DATA_DIR+name)
    if not os.access(self.filename, os.F_OK):
      fp = open(self.filename, "w")

  def readAll(self):
    with open(self.filename, 'r') as f:
      lines = f.readlines()
      for i in range(0, len(lines)):
        lines[i] = lines[i].rstrip('\n')
      return lines

  def append(self, results):
    lines = self.readAll()
    # 数据没有变多
    if len(lines) >= len(results):
      return
    with open(self.filename, 'w') as f:
      for i in range(len(lines), len(results)):
        f.write(results[i]+'\n')

def getCodeList():
    codes = []
    with open(BASE_STOCK_DATA_DIR+'/codelist', 'r') as f:
      lines = f.readlines()
      for i in range(0, len(lines)):
        row = lines[i].rstrip('\n').split('=')
        codes.append(row[0])
      return codes
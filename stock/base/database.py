import os
from stock.base.filebase import BASE_STOCK_DATA_DIR, DEFAULT_SPLIT_TOKEN

def getCodeList():
  codes = []
  with open(BASE_STOCK_DATA_DIR+'base/codelist', 'r') as f:
    lines = f.readlines()
    for i in range(0, len(lines)):
      row = lines[i].rstrip('\n').split(DEFAULT_SPLIT_TOKEN)
      codes.append(row[0])
    return codes

def getCodePreList():
  codes = []
  with open(BASE_STOCK_DATA_DIR+'base/codelist', 'r') as f:
    lines = f.readlines()
    for i in range(0, len(lines)):
      row = lines[i].rstrip('\n').split(DEFAULT_SPLIT_TOKEN)
      codes.append(row[1])
    return codes

def getIndustryList():
  codes = []
  with open(BASE_STOCK_DATA_DIR+'/base/industrylist', 'r') as f:
    lines = f.readlines()
    for i in range(0, len(lines)):
      row = lines[i].rstrip('\n').split(DEFAULT_SPLIT_TOKEN)
      codes.append(row[0])
    return codes
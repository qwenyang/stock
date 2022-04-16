import json
from stock.base.webbase import WebBase
from stock.base.parserbase import ParserBase
from stock.base.writefile import MergeWriteFile
from stock.base.spiderbase import SpiderBase
from stock.base.database import getCodeList

class ShareHoldersWeb(WebBase):
  # 1. 构造函数
  def __init__(self, code):
    url = "https://datacenter-web.eastmoney.com/api/data/v1/get?"
    params = {
      "reportName": "RPT_HOLDERNUM_DET",
      "columns": "END_DATE,TOTAL_A_SHARES,AVG_HOLD_NUM,TOTAL_MARKET_CAP,AVG_MARKET_CAP,HOLDER_NUM",
      "source": "WEB",
      "client": "WEB",
      "sortColumns": "END_DATE",
      "sortTypes": -1,
      "pageSize": 1000,
      "filter": "(SECURITY_CODE=%s)" % code,
    }
    headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    WebBase.__init__(self, url, params, headers)
    
class ShareHolderParser(ParserBase):
  def __init__(self):
    ParserBase.__init__(self)
  def parse(self):
    results = []
    if not self.data or self.data == "" or self.data == "{ }" or self.data == "{}":
      return results
    jsondata = json.loads(self.data)
    if not jsondata or ('result' not in jsondata) or\
      not jsondata['result'] or ('data' not in jsondata['result'])\
      or not jsondata['result']['data']:
      return results
    for row in jsondata['result']['data']:
      # 统计日期 END_DATE
      # 股东户数 HOLDER_NUM
      # 户均持股数量 AVG_HOLD_NUM
      # 平均持股市值 AVG_MARKET_CAP
      # 总市值 TOTAL_MARKET_CAP
      # 总股本 TOTAL_A_SHARES
      try:
        item1 = self.getKeyValueStr(row, 'END_DATE', '')
        item2 = self.getKeyValueStr(row, 'HOLDER_NUM', '')
        item3 = self.getKeyValueStr(row, 'AVG_HOLD_NUM', '')
        item4 = self.getKeyValueStr(row, 'AVG_MARKET_CAP', '')
        item5 = self.getKeyValueStr(row, 'TOTAL_MARKET_CAP', '')
        item6 = self.getKeyValueStr(row, 'TOTAL_A_SHARES', '')
        results.append([item1, item2, item3, item4, item5, item6])
      except Exception as e:
        print("parse error ", e)
    return results

class ShareHolderMergeWriteFile(MergeWriteFile):
  def __init__(self, name, code):
    MergeWriteFile.__init__(self, self.getFilename(name + '/' +code))

class ShareHolderSpider(SpiderBase):
  # 1. 构造函数
  def __init__(self, name, code):
    SpiderBase.__init__(self, ShareHoldersWeb(code), ShareHolderParser(), ShareHolderMergeWriteFile(name, code))

if __name__ == '__main__':
  codes = getCodeList()
  for code in codes:
    try:
      spider = ShareHolderSpider("shareholders", code)
      spider.run()
    except Exception as e:
      print("some code parse error ", e)


# http://83.push2.eastmoney.com/api/qt/clist/get?pn=1&pz=20&po=1&np=1&fs=b:BK0447+f:!50&fields=f12

import json
from stock.base.webbase import WebBase
from stock.base.parserbase import ParserBase
from stock.base.writefile import AppendWriteFile
from stock.base.spiderbase import SpiderBase
from stock.base.database import getIndustryList
class CodeIndustryWeb(WebBase):
  # 1. 构造函数
  def __init__(self, ic):
    url = "http://83.push2.eastmoney.com/api/qt/clist/get?"
    params = {
      "pn": 1,
      "pz": 1000,
      "fs": "b:%s+f:!50" % ic,
      "fields": "f12",
    }
    headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    WebBase.__init__(self, url, params, headers)

class CodeIndustryParser(ParserBase):
  def __init__(self, ic):
    ParserBase.__init__(self)
  # 解析回包数据 parse json格式的数据
  def parse(self):
    results = []
    if self.data == "" or self.data == "{ }" or self.data == "{}":
      return
    jsondata = json.loads(self.data)
    if not jsondata or ('data' not in jsondata) or ('diff' not in jsondata['data']):
      return
    total = jsondata['data']['total']
    diff = jsondata['data']['diff']
    items = ''
    for index in range(total):
      try:
        items = items + self.getKeyValueStr(diff[str(index)], 'f12', '') + '+'
      except Exception as e:
        print("code=%s parse error" % ic)
    results.append([ic, items])
    return results
    
class CodeIndustryWriteFile(AppendWriteFile):
  def __init__(self):
    AppendWriteFile.__init__(self, self.getFilename('base/codeindustry'))

class CodeIndustrySpider(SpiderBase):
  # 1. 构造函数
  def __init__(self, ic):
    SpiderBase.__init__(self, CodeIndustryWeb(ic), CodeIndustryParser(ic), CodeIndustryWriteFile())

if __name__ == '__main__':
  codes = getIndustryList()
  for ic in codes:
    try:
      spider = CodeIndustrySpider(ic)
      spider.run()
    except Exception as e:
      print(e)

# http://50.push2.eastmoney.com/api/qt/clist/get?pn=1&pz=1000&fs=m:90+t:2+f:!50&fields=f12,f14

#http://83.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112406451793515260225_1649772537007&pn=1&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=b:BK0447+f:!50&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152,f45&_=1649772537042

import json
from stock.base.webbase import WebBase
from stock.base.parserbase import ParserBase
from stock.base.writefile import MergeWriteFile
from stock.base.spiderbase import SpiderBase

class IndustryeListWeb(WebBase):
  # 1. 构造函数
  def __init__(self):
    url = "http://50.push2.eastmoney.com/api/qt/clist/get?"
    params = {
      "pn": 1,
      "pz": 1000,
      "fs": "m:90+t:2+f:!50",
      "fields": "f12,f14",
    }
    headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    WebBase.__init__(self, url, params, headers)

class IndustryeListParser(ParserBase):
  def __init__(self):
    ParserBase.__init__(self)
  # 解析回包数据 parse json格式的数据
  def parse(self):
    results = []
    if self.data == "" or self.data == "{ }" or self.data == "{}":
      return results
    jsondata = json.loads(self.data)
    if not jsondata or ('data' not in jsondata) or ('diff' not in jsondata['data']):
      return results
    total = jsondata['data']['total']
    diff = jsondata['data']['diff']
    for index in range(total):
      try:
        item1 = self.getKeyValueStr(diff[str(index)], 'f12', '')
        item2 = self.getKeyValueStr(diff[str(index)], 'f14', '')
        results.append([item1,item2])
      except Exception as e:
        print("parse error ", e)
    return results

class IndustryeListWriteFile(MergeWriteFile):
  def __init__(self):
    MergeWriteFile.__init__(self, self.getFilename('base/industrylist'))

class IndustryeListSpider(SpiderBase):
  # 1. 构造函数
  def __init__(self):
    SpiderBase.__init__(self, IndustryeListWeb(), IndustryeListParser(), IndustryeListWriteFile())
    

if __name__ == '__main__':
  try:
    spider = IndustryeListSpider()
    spider.run()
  except Exception as e:
    print(e)
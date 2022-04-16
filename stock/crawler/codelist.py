# https://eniu.com/static/data/stock_list.json

import json
from stock.base.webbase import WebBase
from stock.base.parserbase import ParserBase
from stock.base.writefile import WriteFile
from stock.base.spiderbase import SpiderBase

class CodeListWeb(WebBase):
  # 1. 构造函数
  def __init__(self):
    url = "https://eniu.com/static/data/stock_list.json"
    params = { }
    headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    WebBase.__init__(self, url, params, headers)

class CodeListParser(ParserBase):
  def __init__(self):
    ParserBase.__init__(self)
  # 解析回包数据 parse json格式的数据
  def parse(self):
    results = []
    if self.data == "" or self.data == "{ }" or self.data == "{}":
      return results
    jsondata = json.loads(self.data)
    print(len(jsondata))
    for row in jsondata:
      # stock_number 600000
      # stock_id  sh600000
      # stock_name 股票名称
      try:
        item1 = self.getKeyValueStr(row, 'stock_number', '')
        if len(item1) < 6:
          continue
        item2 = self.getKeyValueStr(row, 'stock_id', '')
        item3 = self.getKeyValueStr(row, 'stock_name', '')
        results.append([item1, item2, item3])
      except Exception as e:
        print("parse error data ", e)
    return results

class CodeListWriteFile(WriteFile):
  def __init__(self):
    WriteFile.__init__(self, self.getFilename('base/codelist'))

class CodeListSpider(SpiderBase):
  # 1. 构造函数
  def __init__(self):
    SpiderBase.__init__(self, CodeListWeb(), CodeListParser(), CodeListWriteFile())

if __name__ == '__main__':
  try :
    codelist = CodeListSpider()
    codelist.run()
  except Exception as e:
    print(e)

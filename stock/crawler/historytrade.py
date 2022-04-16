import json
from stock.base.webbase import WebBase
from stock.base.parserbase import ParserBase
from stock.base.writefile import MergeWriteFile
from stock.base.spiderbase import SpiderBase
from stock.base.database import getCodeList
from stock.base.utils import getNumberCodeName

# 'http://quotes.money.163.com/service/chddata.html?code=' + market + number + '&start=' + start_data + '&end=' + end_data
#  http://quotes.money.163.com/service/chddata.html?code=0601898&start=19600101&end=20300101
#  http://quotes.money.163.com/service/chddata.html?code=sz300823&start=19600101&end=20300101
#  http://quotes.money.163.com/service/chddata.html?code=0688175&start=19600101&end=20300101

# market: 0:沪市 1:深市
# number: 股票代码
# start_data: 起始日期:yyyymmdd
# end_data: 结束时间:yyyymmdd

class HistoryTradeWeb(WebBase):
  # 1. 构造函数
  def __init__(self, code):
    url = "http://quotes.money.163.com/service/chddata.html?"
    params = {
      "code": getNumberCodeName(code),
      "start": "20000101",
      "end": "20300101",
    }
    headers = { 
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    WebBase.__init__(self, url, params, headers)

class HistoryTradeParser(ParserBase):
  def __init__(self):
    ParserBase.__init__(self)
  # 解析回包数据 parse json格式的数据
  def parse(self):
    results = []
    if not self.data or self.data == "" or self.data == "{ }" or self.data == "{}":
      return results
    # 日期 0	股票代码 1	名称 2	收盘价 3	最高价 4	最低价 5	开盘价 6 
    # 前收盘 7	涨跌额 8	涨跌幅 9	换手率 10	成交量 11	成交金额 12	总市值 13	流通市值 14	成交笔数 15
    lines = self.data.split('\n')
    for i in range(1, len(lines)):
      results.append(lines[i])
    return results

class HistoryTradeMergeWriteFile(MergeWriteFile):
  def __init__(self, code):
    MergeWriteFile.__init__(self, self.getFilename('historytrade/' + code))

class HistoryTradeSpider(SpiderBase):
  # 1. 构造函数
  def __init__(self, code):
    SpiderBase.__init__(self, HistoryTradeWeb(code), HistoryTradeParser(), HistoryTradeMergeWriteFile(code))

if __name__ == '__main__':
  codes = getCodeList()
  codes = ['002241']
  for code in codes[0:1]:
    try:
      spider = HistoryTradeSpider(code)
      spider.run()
    except Exception as e:
      print(e)

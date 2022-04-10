import json
from spiderbase import SpiderBase
from stock.base.myfile import getCodeList
from stock.base.utils import getNumberCodeName


# 'http://quotes.money.163.com/service/chddata.html?code=' + market + number + '&start=' + start_data + '&end=' + end_data
#  http://quotes.money.163.com/service/chddata.html?code=sh601898&start=19600101&end=20300101
#  http://quotes.money.163.com/service/chddata.html?code=sz300823&start=19600101&end=20300101
#  http://quotes.money.163.com/service/chddata.html?code=0688175&start=19600101&end=20300101

# market: 0:沪市 1:深市
# number: 股票代码
# start_data: 起始日期:yyyymmdd
# end_data: 结束时间:yyyymmdd

class HistoryTrade(SpiderBase):
  # 1. 构造函数，
  def __init__(self, code, name):
    SpiderBase.__init__(self, code, name)

  # 2. 初始化请求参数，code
  def initRequest(self):
    url = "http://quotes.money.163.com/service/chddata.html?"
    params = {
      "code": getNumberCodeName(self.code),
      "start": "19600101",
      "end": "20300101",
    }
    headers = { 
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    SpiderBase.initRequest(self, url, params, headers)
  
  # 3. 去请求数据 request
  def request(self):
    SpiderBase.request(self)

  # 4. 解析回包数据 parse json格式的数据
  def parse(self):
    results = []
    if not self.suss or self.body == "":
      return
    # 日期 0	股票代码 1	名称 2	收盘价 3	最高价 4	最低价 5	开盘价 6 	前收盘 7	涨跌额 8	涨跌幅 9	换手率 10	成交量 11	成交金额 12	总市值 13	流通市值 14	成交笔数 15
    lines = self.body.split('\n')
    for i in range(1, len(lines)):
      results.append(lines[i])
    self.table = results

  # 5. 比较写入/增量写入
  def incWrite(self):
    SpiderBase.incWrite(self)
    return

  # 6. 爬虫跑起来
  def run(self):
    SpiderBase.run(self)

if __name__ == '__main__':
  codes = getCodeList()
  for code in codes:
    try:
      spider = HistoryTrade("historytrade", code)
      spider.initRequest()
      spider.run()
    except Exception as e:
      print(e)

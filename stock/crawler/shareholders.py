import json
from spiderbase import SpiderBase
from stock.base.myfile import getCodeList

class ShareHolders(SpiderBase):
  # 1. 构造函数，
  def __init__(self, code, name):
    SpiderBase.__init__(self, code, name)

  # 2. 初始化请求参数，code
  def initRequest(self):
    url = "https://datacenter-web.eastmoney.com/api/data/v1/get?"
    params = {
      "reportName": "RPT_HOLDERNUM_DET",
      "columns": "END_DATE,TOTAL_A_SHARES,AVG_HOLD_NUM,TOTAL_MARKET_CAP,AVG_MARKET_CAP,HOLDER_NUM",
      "filter": "(SECURITY_CODE=%s)" % self.code,
      "source": "WEB",
      "client": "WEB",
      "sortColumns": "END_DATE",
      "sortTypes": -1,
      "pageSize": 1000,
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
    jsondata = json.loads(self.body)
    if not jsondata or ('result' not in jsondata) or ('data' not in jsondata['result']):
      return
    for row in jsondata['result']['data']:
      # 统计日期 END_DATE
      # 股东户数 HOLDER_NUM
      # 户均持股数量 AVG_HOLD_NUM
      # 平均持股市值 AVG_MARKET_CAP
      # 总市值 TOTAL_MARKET_CAP
      # 总股本 TOTAL_A_SHARES
      try:
        item = str(row['END_DATE']) + ',' + str(row['HOLDER_NUM']) + ',' + str(row['AVG_HOLD_NUM']) + ',' +\
        str(row['AVG_MARKET_CAP']) + ',' + str(row['TOTAL_MARKET_CAP']) + ',' + str(row['TOTAL_A_SHARES'])
        results.append(item)
      except :
        print("code=%s parse error" % self.code)
        self.suss = False
    self.table = results
  
  # 5. 比较写入/增量写入
  def incWrite(self):
    SpiderBase.incWrite(self)

  # 6. 爬虫跑起来
  def run(self):
    SpiderBase.run(self)

if __name__ == '__main__':
  codes = getCodeList()
  for code in codes:
    try:
      spider = ShareHolders("shareholders", code)
      spider.initRequest()
      spider.run()
    except :
      print("some code arse error")

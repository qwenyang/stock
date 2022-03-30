import json
from spiderbase import SpiderBase

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
    self.data = json.dumps(self.body, ensure_ascii=False)
    print(self.data)
  
  # 5. 比较写入/增量写入
  def incWrite(self):
    return self.body

  # 6. 爬虫跑起来
  def run(self):
    SpiderBase.run(self)
 
if __name__ == '__main__':
    spider = ShareHolders("002241", "shareholders")
    spider.initRequest()
    spider.run()

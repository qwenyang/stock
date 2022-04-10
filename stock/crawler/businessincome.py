import json
from spiderbase import SpiderBase
from stock.base.myfile import getCodeList
from stock.base.utils import getCodeName, deleteTag, chineseNumber
class BusinessIncome(SpiderBase):
  # 1. 构造函数，
  def __init__(self, code, name):
    SpiderBase.__init__(self, code, name)

  # 2. 初始化请求参数，code
  def initRequest(self):
    codename = getCodeName(self.code)
    url = "https://eniu.com/table/lrba/%s/q/0/q/all" % (codename)
    print(url)
    params = {
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
    if len(jsondata) < 1:
      return
    result_income = dict()
    result_profit = dict()
    result_one_share_profit = dict()
    for row in jsondata:
      # 营业总收入
      # 净利润
      # 基本每股收益
      try:
        if 'keyName' in row and "营业总收入" == deleteTag(row['keyName']):
          for k in row:
            if k != 'keyName':
              result_income[k] = str(chineseNumber(row[k]))
        if 'keyName' in row and "净利润" == deleteTag(row['keyName']):
          for k in row :
            if k != 'keyName':
              result_profit[k] = str(chineseNumber(row[k]))
        if 'keyName' in row and "基本每股收益" == deleteTag(row['keyName']):
          for k in row :
            if k != 'keyName':
              result_one_share_profit[k] = str(chineseNumber(row[k]))
      except :
        print("code=%s parse error" % self.code)
        self.suss = False
    self.table = []
    for k in result_income:
      line = k +','
      line += (result_income[k] if k in result_income else '0') + ','
      line += (result_profit[k] if k in result_profit else '0') + ','
      line += (result_one_share_profit[k] if k in result_one_share_profit else '0')
      self.table.append(line)
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
      spider = BusinessIncome("businessincome", code)
      spider.initRequest()
      spider.run()
    except Exception as e:
      print("some code parse error", e)

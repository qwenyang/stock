import requests
import json
from stock.base.myfile import StockFileBase
 
class SpiderBase(object):
  # 1. 构造函数，
  def __init__(self, name, code):
    self.code = code
    self.name = name
    self.suss = False
    self.body = ""
    self.url = ""
    self.params = {}
    self.headers = {}
    self.table = []

  # 2. 初始化请求参数，code
  def initRequest(self, url, params, headers):
    self.url = url
    self.params = params
    self.headers = headers
  
  # 3. 去请求数据 request
  def request(self):
    try :
      requests.packages.urllib3.disable_warnings()
      print(self.url, self.params)
      response = requests.get(url=self.url, headers=self.headers, params=self.params, verify=False, timeout=5)
      self.body = response.text
      self.suss = True
    except :
      self.suss = False

  # 4. 解析回包数据 parse json格式的数据
  def parse(self):
    self.table = json.loads(self.body)
  
  # 5. 比较写入/增量写入
  def incWrite(self):
    file = StockFileBase(self.name, self.code)
    file.append(self.table)
    return self.body

  # 6. 爬虫跑起来
  def run(self):
    self.request()
    self.parse()
    self.incWrite()



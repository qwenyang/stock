import requests
import json
 
 
class SpiderBase(object):
  # 1. 构造函数，
  def __init__(self, code, name):
    self.code = code
    self.name = name
    self.suss = False
    self.body = ""
    self.url = ""
    self.params = {}
    self.headers = {}
    self.data = {}

  # 2. 初始化请求参数，code
  def initRequest(self, url, params, headers):
    self.url = url
    self.params = params
    self.headers = headers
  
  # 3. 去请求数据 request
  def request(self):
    try :
      response = requests.get(url=self.url, headers=self.headers, params=self.params, verify=False, timeout=5)
      self.body = response.text
      self.suss = True
    except :
      self.suss = False

  # 4. 解析回包数据 parse json格式的数据
  def parse(self):
    self.data = json.dumps(self.body, ensure_ascii=False)
    print(self.data)
  
  # 5. 比较写入/增量写入
  def incWrite(self):
    return self.body

  # 6. 爬虫跑起来
  def run(self):
    self.request()
    self.parse()
    self.incWrite()



import requests
import json
 
# 爬虫基础类
class WebBase(object):
  # 1. 构造函数
  def __init__(self, url, params, headers):
    self.url = url
    self.params = params
    self.headers = headers
  
  # 2. 去请求数据 request
  def request(self):
    try :
      requests.packages.urllib3.disable_warnings()
      response = requests.get(url=self.url, headers=self.headers, params=self.params, verify=False, timeout=30)
      return response.text
    except Exception as e:
      print(e)
      return ''
  def addParams(self, key, value):
    self.params[key] = value



import requests
import json
from stock.base.webbase import WebBase
 
# 爬虫基础类
class SpiderBase(object):
  # 1. 构造函数 web 网络基础，parser 解析类， writter 写入类
  def __init__(self, weber, parser, writter):
    self.weber = weber
    self.parser = parser
    self.writter = writter
  
  # 2. 去请求数据 request
  def request(self):
    try :
      self.parser.setData(self.weber.request())
    except Exception as e:
      print(e)

  # 3. 解析回包数据
  def parse(self):
    try :
      self.writter.setData(self.parser.parse())
    except Exception as e:
      print(e)
    
  # 4. 写入数据
  def write(self):
    try :
      self.writter.write()
    except Exception as e:
      print(e)

  # 5. 爬虫跑起来
  def run(self):
    self.request()
    self.parse()
    self.write()



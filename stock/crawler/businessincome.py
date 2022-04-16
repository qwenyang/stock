import json
from stock.base.webbase import WebBase
from stock.base.parserbase import ParserBase
from stock.base.writefile import MergeWriteFile
from stock.base.spiderbase import SpiderBase
from stock.base.database import getCodeList
from stock.base.utils import deleteTag, getCodeName, chineseNumber

# 亿牛网  https://eniu.com/ 
# 请求数据地址 https://eniu.com/table/lrba/sz002241/q/0/q/all
# Web 页面展示地址 https://eniu.com/gu/sz002241/lrb

class BusinessIncomeWeb(WebBase):
  # 1. 构造函数
  def __init__(self, code):
    codename = getCodeName(code)
    url = "https://eniu.com/table/lrba/%s/q/0/q/all" % (codename)
    params = { }
    headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    WebBase.__init__(self, url, params, headers)

class BusinessIncomeParser(ParserBase):
  def __init__(self):
    ParserBase.__init__(self)
  # 解析回包数据 parse json格式的数据
  def getDictValue(self, jsondata, keyNameList):
    incomes = dict()
    for keyName in keyNameList:
      for row in jsondata:
        try:
          if 'keyName' in row and keyName == deleteTag(row['keyName']):
            for k in row:
              if k != 'keyName':
                incomes[k] = str(chineseNumber(row[k]))
            if len(incomes) >= 1:
              return incomes
        except Exception as e:
          return incomes

  def parse(self):
    results = []
    if not self.data or self.data == "" or self.data == "{ }" or self.data == "{}":
      return results
    jsondata = json.loads(self.data)
    if len(jsondata) < 1:
      return results
    result_income = self.getDictValue(jsondata, ['营业总收入', '营业收入'])
    result_profit = self.getDictValue(jsondata, ['净利润', '利润总额', '营业利润'])
    result_one_share_profit = self.getDictValue(jsondata, ['基本每股收益'])
    for k in result_income:
      item1 = k
      item2 = (result_income[k] if k in result_income else '0')
      item3 = (result_profit[k] if k in result_profit else '0')
      item4 = (result_one_share_profit[k] if k in result_one_share_profit else '0')
      results.append([item1, item2, item3, item4])
    return results

class BusinessIncomeMergeWriteFile(MergeWriteFile):
  def __init__(self, code):
    MergeWriteFile.__init__(self, self.getFilename('businessincome/' + code))

class BusinessIncomeSpider(SpiderBase):
  # 1. 构造函数
  def __init__(self, code):
    SpiderBase.__init__(self, BusinessIncomeWeb(code), BusinessIncomeParser(), BusinessIncomeMergeWriteFile(code))

if __name__ == '__main__':
  codes = getCodeList()
  for code in codes:
    try:
      print(code)
      spider = BusinessIncomeSpider(code)
      spider.run()
    except Exception as e:
      print("some code parse error", e)

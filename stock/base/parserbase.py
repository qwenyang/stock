import os

class ParserBase(object):
  def __init__(self):
    return

  def setData(self, data):
    self.data = data

  def parse():
    table = json.loads(self.body)
    return table
  
  # 从字典中获取默认的值
  def getKeyValueStr(self, dictv, ky, defv = ''):
    try:
      val = str(dictv[ky])
      if val == 'None' or val == '':
        return defv
      return val
    except:
      return defv
    return defv

import os
import re

# 从字典中获取默认的值
def getKeyValueStr(dictv, ky, defv = ''):
  try:
    val = str(dictv[ky])
    if val == 'None' or val == '':
      return defv
    
    return val
  except:
    return defv
  return defv

def getCodeName(code):
  if code.startswith("3") or code.startswith("0"):
      return "sz" + code
  else :
      return "sh" + code

def getNumberCodeName(code):
  if code.startswith("3") or code.startswith("0"):
      return "1" + code
  else :
      return "0" + code

def deleteTag(text):
  pattern = re.compile(r'<[^>]+>',re.S)
  result = pattern.sub('', text)
  return result

def chineseNumber(text):
  res = 0.0
  try :
    if '千亿' in text:
        numbers = text.split('千亿')
        res = float(numbers[0])*100000000000
        return res
    if '百亿' in text:
        numbers = text.split('百亿')
        res = float(numbers[0])*10000000000
        return res
    if '亿' in text:
        numbers = text.split('亿')
        res = float(numbers[0])*100000000
        return res
    if '千万' in text:
        numbers = text.split('千万')
        res = float(numbers[0])*10000000
        return res
    if '百万' in text:
        numbers = text.split('百万')
        res = float(numbers[0])*1000000
        return res
    if '万' in text:
        numbers = text.split('万')
        res = float(numbers[0])*10000
        return res
    if '元' in text:
        numbers = text.split('元')
        res = float(numbers[0])
        return res
    res = float(text)
    return res
  except:
    return res
  return res
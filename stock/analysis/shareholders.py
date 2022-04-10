from datetime import datetime
from smartbase import SmartBase
from filterbase import atLeastOneYear

# 最近至少30天股东数减少值比例
class LatestMaximumDecrementShareHolders(SmartBase):
  # 1. 构造函数
  def __init__(self):
    SmartBase.__init__(self, "shareholders")
  # 2. 解析code文件的的内容，放在table中
  def parse(self, code):
    self.table = []
    lines = self.read(code)
    for line in lines:
      try:
        items = line.split(",")
        items[1] = int(items[1])
        self.table.append(items)
      except err:
        return
  # 3. 启动分析
  def analysis(self, code):
    if len(self.table) <= 6:
      return 0
    todaystr = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    today = datetime.strptime(todaystr, '%Y-%m-%d %H:%M:%S')
    latest = datetime.strptime(self.table[0][0], '%Y-%m-%d %H:%M:%S')
    delta = today - latest
    if delta.days >= 15:
      return 0
    print(code)
    for i in range(1, len(self.table)-1):
      current = datetime.strptime(self.table[i][0], '%Y-%m-%d %H:%M:%S')
      delta = latest - current
      if delta.days >= 30:
        percent = 1.0*(self.table[i][1] - self.table[0][1])/self.table[i][1]
        return percent
    return 0
  # out 运行起来
  def process(self):
    results = self.run()
    return results
  # out 只取Top 20的
  def top(self):
    results = self.run()
    results = list(filter(atLeastOneYear, results))
    results = results[0 : 20]
    [print(r.format()) for r in results]
  
# 市值大于500亿的公司
class LargeCompaniesMaximumDecrementShareHolders(SmartBase):
  # 1. 构造函数，
  def __init__(self):
    SmartBase.__init__(self, "shareholders")
  # 3. 启动分析
  def analysis(self, code):
    if len(self.table) <= 6:
      return 0
    todaystr = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    today = datetime.strptime(todaystr, '%Y-%m-%d %H:%M:%S')
    latest = datetime.strptime(self.table[0][0], '%Y-%m-%d %H:%M:%S')
    delta = today - latest
    if delta.days >= 30:
      return 0
    if self.table[0][4] < 50000000000:
      return 0
    print(code)
    for i in range(1, len(self.table)-1):
      current = datetime.strptime(self.table[i][0], '%Y-%m-%d %H:%M:%S')
      delta = latest - current
      if delta.days >= 30:
        percent = 1.0*(self.table[i][1] - self.table[0][1])/self.table[i][1]
        return percent
    return 0
  def top(self):
    results = self.run()
    results = results[0 : 10]
    [print(r.format()) for r in results]
  
# 股东连续减少的股票
class ContinueDecrementShareHolders(SmartBase):
  # 1. 构造函数，
  def __init__(self):
    SmartBase.__init__(self, "shareholders")
  # 3. 启动分析
  def analysis(self, code):
    if len(self.table) <= 6:
      return 0
    todaystr = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    today = datetime.strptime(todaystr, '%Y-%m-%d %H:%M:%S')
    latest = datetime.strptime(self.table[0][0], '%Y-%m-%d %H:%M:%S')
    delta = today - latest
    if delta.days >= 30:
      return 0
    index, month = 0, 0
    for i in range(1, len(self.table)-1):
      current = datetime.strptime(self.table[i][0], '%Y-%m-%d %H:%M:%S')
      delta = latest - current
      if delta.days >= 30:
        latest = current
        percent = 1.0*(self.table[i][1] - self.table[index][1])/self.table[i][1]
        index, month = i, month + 1
        if percent < 0.0000001:
          break
    if month >= 6:
      percent = 1.0*(self.table[index][1] - self.table[0][1])/self.table[index][1]
      print("code=%s top share holeder decrement month=%d percent=%f" % (code, month, percent))
    return percent

  def top(self):
    results = self.run()
    results = list(filter(atLeastOneYear, results))
    results = results[0 : 10]
    [print(r.format()) for r in results]

if __name__ == '__main__':
  # smart = LatestMaximumDecrementShareHolders()
  # smart.top()

  # largecompanies = LargeCompaniesMaximumDecrementShareHolders()
  # largecompanies.top()
  continuedec = ContinueDecrementShareHolders()
  continuedec.top()
  

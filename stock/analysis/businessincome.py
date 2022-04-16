from datetime import datetime
from smartbase import SmartBase, SmartValue
from filterbase import atLeastFiveYear
# 验证地址   https://eniu.com/gu/sz002352/lrb 

# 连续3年收入增量平均值排序
class ContinueBusinessIncome(SmartBase):
  # 1. 构造函数，
  def __init__(self):
    SmartBase.__init__(self, "businessincome")
  # 2. 解析code文件的的内容，放在table中
  def parse(self, code):
    self.table = []
    lines = self.read(code)
    # print(lines)
    for line in lines:
      try:
        items = line.split(",")
        items[1] = float(items[1])
        items[2] = float(items[2])
        items[3] = float(items[3])
        self.table.append(items)
      except Exception as e:
        continue
  def getYearData(self):
    return list(filter(lambda line: '12-31' in line[0], self.table))
  # 3. 启动分析
  def analysis(self, code):
    if len(self.table) <= 6:
      return SmartValue(code, 0, 'data to less')
    yeartable = self.getYearData()
    if yeartable[0][2]<1000000000:
      return SmartValue(code, 0, 'profile less 1 billion')
    count, idx, total = 0, 0, 0.0
    for i in range(1, len(yeartable)):
      percent = 1.0*(yeartable[idx][1] - yeartable[i][1])/yeartable[i][1]
      if yeartable[i][2]<1000000000 or yeartable[idx][2]<1000000000 or percent <= 0.2:
        return SmartValue(code, 0, 'profile less 1 billion')
      total += percent
      idx, count = i, count + 1
      if count>=3:
        break

    if count < 3:
      return SmartValue(code, 0, 'percent to less')
    return SmartValue(code, total/count, 'ok total=%f count=%d' % (total, count))

  def top(self):
    results = self.run()
    results = results[0 : 20]
    [print(r.format()) for r in results]

# 连续3年收入增量利润平均值排序
class ContinueProfitBusinessIncome(SmartBase):
  # 1. 构造函数，
  def __init__(self):
    SmartBase.__init__(self, "businessincome")
  # 2. 解析code文件的的内容，放在table中
  def parse(self, code):
    self.table = []
    lines = self.read(code)
    # print(lines)
    for line in lines:
      try:
        items = line.split(",")
        items[1] = float(items[1])
        items[2] = float(items[2])
        items[3] = float(items[3])
        self.table.append(items)
      except Exception as e:
        continue
  def getYearData(self):
    return list(filter(lambda line: '12-31' in line[0], self.table))
  # 3. 启动分析
  def analysis(self, code):
    if len(self.table) <= 6:
      return SmartValue(code, 0, 'data to less')
    yeartable = self.getYearData()
    if yeartable[0][2]<100000000:
      return SmartValue(code, 0, 'profile less 1 billion')
    count, idx, total = 0, 0, 0.0
    for i in range(1, len(yeartable)):
      percent = 1.0*(yeartable[idx][2] - yeartable[i][2])/yeartable[i][2]
      if yeartable[i][1]<10000000000 or yeartable[idx][1]<10000000000 or percent <= 0.2:
        return SmartValue(code, 0, 'profile less 50 billion')
      total += percent
      idx, count = i, count + 1
      if count>=3:
        break

    if count < 3:
      return SmartValue(code, 0, 'percent to less')
    return SmartValue(code, total/count, 'ok total=%f count=%d' % (total, count))

  def top(self):
    results = self.run()
    results = results[0 : 20]
    [print(r.format()) for r in results]

# 每股收益
class ShareBusinessIncome(SmartBase):
  # 1. 构造函数，
  def __init__(self):
    SmartBase.__init__(self, "businessincome")
  # 2. 解析code文件的的内容，放在table中
  def parse(self, code):
    self.table = []
    lines = self.read(code)
    # print(lines)
    for line in lines:
      try:
        items = line.split(",")
        items[1] = float(items[1])
        items[2] = float(items[2])
        items[3] = float(items[3])
        self.table.append(items)
      except err:
        return
  # 3. 启动分析
  def analysis(self, code):
    print(self.table)
    if len(self.table) <= 6:
      return
    return self.table[0][3]
  def process(self):
    results = self.run()
   
    results = results[0 : 20]
    [print(r.format()) for r in results]

if __name__ == '__main__':
  # b = ContinueBusinessIncome()
  # b.parse('002241')
  # print(b.analysis('002241').format())
  # income = ContinueBusinessIncome()
  # income.top()
  profit = ContinueProfitBusinessIncome()
  profit.top()
  # shareincomde = ShareBusinessIncome()
  # shareincomde.process()
  

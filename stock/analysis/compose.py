from datetime import datetime
from smartbase import SmartBase

# 验证地址   https://eniu.com/gu/sz002352/lrb 

# 连续收入增量排序
class BusinessIncome(SmartBase):
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
    count = 0
    for i in range(4, len(self.table)):
        percent1 = 1.0*(self.table[i-4][1] - self.table[i][1])/self.table[i][1]
        percent2 = 1.0*(self.table[i-4][2] - self.table[i][2])/self.table[i][2]
        print(code, percent1, percent2)
        if ('12-31' in self.table[i-4][0]) and ('12-31'in self.table[i][0]) :
            if percent1 > 0.2 or percent2 > 0.2:
                count = count + 1
            else :
                break
    print(code, count)
    if count >= 6:
        print("code=%s income count=%d" % (code, count))
    return count
  def process(self):
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
  # income = BusinessIncome()
  # income.process()
  shareincomde = ShareBusinessIncome()
  shareincomde.process()
  

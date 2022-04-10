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
      except Exception as e:
        continue
  # 3. 启动分析
  def analysis(self, code):
    if len(self.table) <= 6:
      return 0
    count, idx, total = 0, 0, 0.0
    for i in range(0, len(self.table)):
      if ('12-31' in self.table[i][0]) :
        if count > 1:
          percent = 1.0*(self.table[idx][1] - self.table[i][1])/self.table[i][1]
          if percent < 0.1:
            break
          total += percent
        idx, count = i, count + 1
        print("code=%s income count=%d" % (code, count))
    return total

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
  income = BusinessIncome()
  income.top()
  # shareincomde = ShareBusinessIncome()
  # shareincomde.process()
  

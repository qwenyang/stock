import os
from stock.base.filebase import FileBase

class WriteFile(FileBase):
  def __init__(self, filename):
    self.filename = filename
    self.data = []

  def setData(self, data):
    self.data = data

  def write(self):
    self.echo(self.filename)
    with open(self.filename, 'w') as f:
      for i in range(len(self.data)):
        line = ''.join(str(item)+self.getDefaultToken() for item in self.data[i])
        f.write(line+'\n')

class AppendWriteFile(WriteFile):
  def __init__(self, filename):
    WriteFile.__init__(self, filename)

  def write(self):
    self.echo(self.filename)
    with open(self.filename, 'a') as f:
      for i in range(0, len(self.data)):
        line = ''.join(str(item)+self.getDefaultToken() for item in self.data[i])
        f.write(line+'\n')

class MergeWriteFile(WriteFile):
  def __init__(self, filename):
    AppendWriteFile.__init__(self, filename)

  def write(self):
    dicts = dict()
    self.echo(self.filename)
    with open(self.filename, 'r') as f:
      lines = f.readlines()
      lines = [line.rstrip('\n') for line in lines]
      for i in range(len(lines)):
        items = lines[i].split(self.getDefaultToken())
        dicts[items[0]] = items
    results = []
    for i in range(0, len(self.data)):
        dicts[self.data[i][0]] = self.data[i]
    for key in dicts:
      results.append(dicts[key])
    if len(results) <= 0:
      return
    self.setData(self.data)
    WriteFile.write(self)
    
      
import os
from pathlib import Path

BASE_STOCK_DATA_DIR = '/data/stock/'
DEFAULT_SPLIT_TOKEN = ','

class FileBase(object):
  def __init__(self):
    return
  def getFilename(self, filename):
    return BASE_STOCK_DATA_DIR + filename
  def getDefaultToken(self):
    return DEFAULT_SPLIT_TOKEN
  def echo(self, filename):
    mypath = Path(filename)
    if not os.access(filename, os.F_OK):
      fp = open(self.filename, "w")
import os
from pathlib import Path
from myfile import StockFileBase

class StockDataBase(StockFileBase):
  def __init__(self, name, code):
    StockFileBase.__init__(self, name, code)
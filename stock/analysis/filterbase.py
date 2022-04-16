import os
from stock.base.myfile import StockFileBase
from smartbase import SmartValue

def atLeastOneYear(val):
    myfile = StockFileBase("historytrade", val.code)
    lines = myfile.readAll()
    if len(lines) > 200:
        return True
    return False

def atLeastFiveYear(val):
    myfile = StockFileBase("historytrade", val.code)
    lines = myfile.readAll()
    if len(lines) > 200:
        return True
    return False

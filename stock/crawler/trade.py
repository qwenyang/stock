import json
from pathlib import Path

BASE_STOCK_DATA_DIR = '/data/stock/'

def parse():
    lines = ''
    with open(BASE_STOCK_DATA_DIR+'/'+'codelist.txt', 'r') as f:
      lines = f.readlines()
    rows = lines[0].split('}')
    fi = open(BASE_STOCK_DATA_DIR+'/'+'codelist', 'w')
    for row in rows:
      line = row[1:]+"}"
      # print(line)
      try :
        val = json.loads(line)
        # print(val)
        fi.write(val['f12'] + '=' + val['f14'] + "\n")
      except:
        print(line)
        

parse()
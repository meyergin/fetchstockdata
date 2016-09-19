import requests
import pandas as pd

url = "http://114.215.202.25:8082/stockCode?ex=sh,sz" 

#r = requests.get(url)
#stockCode = r.text.splitlines()

stockCode = pd.read_csv(url, dtype={'code':object})
symbols = stockCode.code.values.tolist()
#print(symbols)
#print(stockCode)
#print(stockCode.code)
#print(stockCode[( stockCode.code < 100000) & (stockCode.ex.isin(["sz"]) )])
for item in symbols :
	print item
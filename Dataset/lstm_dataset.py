import yfinance as yf
import pandas
from datetime import datetime


now = datetime.now()
ymd_format = '%Y%m%d'

now = now.strftime(ymd_format)

symbol = 'DIS'

# Use a função download para obter os dados
df = yf.download(symbol)

df.to_csv("./dataset_market_dis_{0}.csv".format(now), sep = ",", encoding = "utf-8", decimal = ".")
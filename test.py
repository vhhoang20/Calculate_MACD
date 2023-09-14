from vnstock import *
import pandas as pd

csv = pd.read_csv('ema.csv')

K12 = 2 / (12 + 1) 
ema12 = (4070 - csv['EMA12']) * K12 + csv['EMA12'] 
print("ema12: ",ema12)


K26 = 2 / (26 + 1)
ema26 = (4070 - csv['EMA26']) * K26 + csv['EMA26'] 
print("ema26: ",ema26)

print("MACD: ", ema12 - ema26)
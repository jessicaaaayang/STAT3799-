import pandas_datareader.data as web
import datetime
import pandas as pd

start = datetime.datetime(2013, 1, 1) # Time period for obtaining data-start time
end = datetime.datetime(2017, 12, 31) # Time period for data acquisition-end time
f = open(r"HKcode.txt",'r')
s=f.readlines()
f.close()
s=list(map(lambda x :x.replace("\n", ""),s))
#s=list(map(lambda x :'0{}'.format(x),s))
print(s)
print(list(map(lambda x:web.DataReader(x, "yahoo", start, end).to_csv('HKdata/{}.csv'.format(x)),s)))

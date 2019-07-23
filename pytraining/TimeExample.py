import time
import calendar
print(time.time())  #time in millesecond from 1970
print(time.localtime(time.time()))  #return time with different param
print(time.asctime(time.localtime(time.time()))) #display standard time
print(calendar.month(2019,10))

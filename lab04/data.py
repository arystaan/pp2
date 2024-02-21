# 1)
from datetime import date, timedelta
dt = date.today() - timedelta(5)
print('Current Date :',date.today())
print('5 days before Current Date :',dt)

# 2)
# from datetime import date, timedelta
# yesterday = date.today() - timedelta(1)
# tomorrow = date.today() + timedelta(1)
# today = date.today()
# print('Today :',today)
# print('Tomorrow :',tomorrow)
# print('Yesterday :',yesterday)

# 3)
# import datetime
# dt = datetime.datetime.today().replace(microsecond=0)
# print(dt)

# 4)
# from datetime import datetime, timedelta
# dt = datetime.now()
# print ("First date:", str(dt))
# dt2 = dt + timedelta(seconds = 40)
# print ("Second date:", str(dt2))
# print("Time difference:", str(dt2 - dt))
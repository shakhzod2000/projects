from datetime import datetime
import time

dt1 = datetime(2025, 7, 1)
dt2 = datetime.now()
dt = datetime.strptime("2025/07/11", "%Y/%m/%d") # str to datetime object
dt = datetime.fromtimestamp(time.time()) # same as datetime.now()

print(f"{dt.year}/{dt.month}")
print(dt.strftime("%Y/%m")) # datetime to str

print(dt2 > dt1)
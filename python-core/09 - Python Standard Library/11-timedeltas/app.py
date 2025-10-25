from datetime import datetime, timedelta


dt1 = datetime(2025, 1, 10) + timedelta(days=1, seconds=16)
print(dt1) # Output: 2025-01-11 00:00:16
dt2 = datetime.now()

duration = dt2 - dt1
print(duration)
print("days:", duration.days)
print("seconds:", duration.seconds)
print("total seconds:", duration.total_seconds())
from datetime import datetime
from datetime import date

my_date_time = datetime(2024,1,3,17,24,14)
print(my_date_time)

my_date_time = my_date_time.replace(day=5)
print(my_date_time)

# DATE MANIPULATIONS
date1 = date(2025,3,9)
date2 = date(2024,3,9)
result = date1-date2
print(result)
print(type(result))
print(result.days)

# DATETIME MANIPULATIONS
datetime1 = datetime(2025,1,3,20,10,9)
datetime2 = datetime(2023,1,3,10,10,9)
result = datetime1-datetime2
print(result)
print(type(result))
print(result.days)
print(result.seconds)
print(result.total_seconds())

import datetime

my_time = datetime.time(2,20)
print(my_time.minute)
print(my_time.hour)
print(my_time)
print(my_time.microsecond)

my_time = datetime.time(13,20,1,20)
print(my_time)

print(type(my_time))

# Date object
today = datetime.date.today()
print(today)

print(f"Let us grab day, month and year attributes : day is {today.day}, month is {today.month} and year is {today.year}")

print(f'ctime => {today.ctime()}')

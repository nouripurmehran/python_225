import datetime

today = datetime.date.today()
print(today)
date = datetime.date(2019,1,13)
print(date)

if today==date:
    print("hello world")
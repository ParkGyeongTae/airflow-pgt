from datetime import datetime, timedelta

today        = datetime.today().replace(day = 1)
before1month = (today - timedelta(days = 1)).replace(day = 1)

print('-------------')
print(today)

print(today.year)
print(str(today.month).zfill(2))
print(str(today.day).zfill(2))

print('-------------')
print(before1month)

print(before1month.year)
print(str(before1month.month).zfill(2))
print(str(before1month.day).zfill(2))
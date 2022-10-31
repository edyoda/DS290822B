# datetime module - helps to code wrt to date and time

import datetime as dt

current = dt.datetime.now()
print(current)

# year = current.year
# print(year)

# month = current.month
# print(month)

# day = current.day
# print(day)

# hr = current.hour
# print(hr)

# mins = current.minute
# print(mins)

# sec = current.second
# print(sec)

print(current.strftime("%A"))

print(current.strftime("%a"))

print(current.strftime("%B"))

print(current.strftime("%b"))

print(current.strftime("%c"))

print(current.strftime("%w"))

print(current.strftime("%C"))


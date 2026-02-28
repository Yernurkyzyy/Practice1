import datetime

# 1
current_date = datetime.datetime.now()
print("Current Date:", current_date)

# 2
formatted_date = current_date.strftime("%Y-%m-%d %A")
print("Formatted Date:", formatted_date)

# 3
five_days_ago = current_date - datetime.timedelta(days=5)
print("Five days ago was:", five_days_ago.strftime("%B %d, %Y"))

# 4
next_new_year = datetime.datetime(2027, 1, 1)
days_remaining = next_new_year - current_date

print(f"Days until 2027 New Year: {days_remaining.days} days")



#1 Write a Python program to subtract five days from current date.
from datetime import datetime, timedelta

# Current date
current_date = datetime.now()

# Subtract 5 days using timedelta
five_days_ago = current_date - timedelta(days=5)

print("Current Date:", current_date.strftime("%Y-%m-%d"))
print("Five Days Ago:", five_days_ago.strftime("%Y-%m-%d"))


#2 Write a Python program to print yesterday, today, tomorrow.
from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:    ", today.strftime("%Y-%m-%d"))
print("Tomorrow: ", tomorrow.strftime("%Y-%m-%d"))


#3 Write a Python program to drop microseconds from datetime.
from datetime import datetime

dt_with_ms = datetime.now()
dt_no_ms = dt_with_ms.replace(microsecond=0)

print("With Microseconds:", dt_with_ms)
print("No Microseconds:  ", dt_no_ms)

#4 Write a Python program to calculate two date difference in seconds
from datetime import datetime


date1 = datetime(2026, 2, 28, 14, 0, 0) 
date2 = datetime(2026, 2, 20, 10, 30, 0) 

difference = date1 - date2

seconds_diff = difference.total_seconds()

print(f"Difference: {int(seconds_diff)} seconds")
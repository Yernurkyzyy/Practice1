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
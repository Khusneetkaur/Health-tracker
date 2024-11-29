# Simple Cycle Tracker
cycle_start_date = input("Enter the start date of your last period (YYYY-MM-DD): ")
cycle_length = int(input("Enter your usual cycle length in days: "))

print("\nYour next period is expected around:")
from datetime import datetime, timedelta
next_period = datetime.strptime(cycle_start_date, "%Y-%m-%d") + timedelta(days=cycle_length)
print(next_period.strftime("%Y-%m-%d"))

hourly_server_cost = 0.51
budget_amount = 918

hours_per_day = 24
days_per_week = 7
days_per_month = 30

daily_cost = hourly_server_cost * hours_per_day
weekly_cost = daily_cost * days_per_week
monthly_cost = daily_cost * days_per_month

affordable_days = budget_amount / daily_cost

print("How much does it cost to operate one server per day?")
print(f"${daily_cost:.2f}\n")

print("How much does it cost to operate one server per week?")
print(f"${weekly_cost:.2f}\n")

print("How much does it cost to operate one server per month?")
print(f"${monthly_cost:.2f}\n")

print("How many days can I operate one server with $918?")
print(f"{affordable_days:.0f} days")

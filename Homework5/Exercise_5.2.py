from datetime import datetime, timedelta

def print_working_days(date1, date2):
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")
    
    current = d1
    
    while current < d2:
        if current.weekday() < 5:
            print(current.strftime("%Y-%m-%d"))
        current += timedelta(days=1)


print_working_days("2024-01-01", "2024-01-10")

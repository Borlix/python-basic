# 7. Days to Years: Convert a given number of days into years, weeks, and days. 

Days = int(input("Enter days : "))

years = Days// 365
reminder = Days%365
weaks = reminder//7
days = reminder%7
print(f"Year = {years},weaks = {weaks}, Days = {days}")
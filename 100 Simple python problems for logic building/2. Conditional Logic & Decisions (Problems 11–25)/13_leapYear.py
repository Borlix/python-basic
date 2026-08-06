# 12. Leap Year: Check if a given year is a leap year.

year = int(input("Enter year : "))

if (year%4==0 and year%100 != 0) or year%400==0 :
    print(f"Yes Year {year} is Leap year.")
else :
    print(f"No year {year} is Not Leap year")
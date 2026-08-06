# 23. Electricity Bill: Calculate total bill based on units consumed using tiered pricing.

unit = float(input("Enter Unit of electricity : "))
bill = 0
if unit >= 200 :
    bill = ( 100 * 4 ) + ( 100 * 5) + ((unit -200) * 6)
    print("Your Bill is Rs :",bill)
elif unit >= 100 :
    bill = ( 100 * 4 ) + ( (unit-100) * 5) 
    print("Your Bill is Rs :",bill)
else :
    bill = unit * 4
    print("Your Bill is Rs :",bill)
# 4. Simple Interest: Calculate simple interest using Principal, Rate, and Time.

Principal = float(input("Enter your Ammount : "))
Rate = float(input("Enter the Rate : "))
Time = int(input("Enter your Time : "))

sim_interest = (Principal*Rate*Time)/100

print("Your simple interest is : ",sim_interest)
# 	18. Profit or Loss: Input cost price and selling price to calculate profit or loss.

cp = int(input("Enter Cost price : "))
sp = int(input("Enter Selling price : "))

profit = sp - cp
loss = cp - sp

if cp > sp :
    print(f"We got {loss}Rs Loss!")
else :
    print(f"We got {profit}Rs Profit!")
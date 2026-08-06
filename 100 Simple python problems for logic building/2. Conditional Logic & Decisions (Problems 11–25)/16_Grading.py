# 16. Grading System: Input a score (0–100) and output the letter grade (A, B, C, D, F).

Grade = float(input("Enter your Mark :"))

if Grade >= 80 :
    print("You Got 'A' ")
elif Grade >= 60 :
    print("You Got 'B' ")
elif Grade >= 40 :
    print("You Got 'C' ")
elif Grade >= 20 :
    print("You Got 'D' ")
else :
    print("Try again 'F' ")
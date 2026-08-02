# Recursion - when function call it self repeatdly , it is related to loop

def draw(n) :
    if n == 11:     # Base case
        return
    print(n)
    draw(n+1)

draw(1)
# list max num 3
a = float(input("Enter the a value"))
b = float(input("Enter the b value"))
c = float(input("Enter the c value"))
if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)
    
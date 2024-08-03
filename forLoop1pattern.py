#inverted diamond patern for loop
for i in range(5,0,-1):
    for j in range(1,6):
        if j<=5-i:
            print("",end = " ")
        else:
            print("*", end = " ")
    print()
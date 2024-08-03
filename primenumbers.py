# x = 5
for x in range(2,25):
    is_prime = True
    for  i in range(2,x):
        is_prime_inner = True
        if x % i == 0:
            is_prime_inner = False
            is_prime = False
            break
    
    if is_prime_inner:
        print("inner loop variable")
    if is_prime:
        print(x)
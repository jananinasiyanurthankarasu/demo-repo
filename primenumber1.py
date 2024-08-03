is_prime = True
for x in range(10):

    for i in range(2,x):
        if x % i == 0:
            is_prime = False
            break 
if is_prime:
    print(x)
    
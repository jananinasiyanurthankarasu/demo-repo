# python program to interchange first and last elements in the list

n = [55,88,22,11,45,67]
temp = n[0]
n[0] = n[-1]
n[-1] = temp
print(n)
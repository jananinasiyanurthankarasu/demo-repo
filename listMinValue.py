x = [11,2,5,7,4,3]
n= len(x)
min_value = x[0]
for i in range(0,n):
    if x[i] < min_value:
        min_value = x[i]
print(min_value)
# sum of square of n natural numbers
n = int(input("Enter the n value"))
sum = 0
for i in range(1,n+1):
    sum = sum + pow(i,2)
print(sum)

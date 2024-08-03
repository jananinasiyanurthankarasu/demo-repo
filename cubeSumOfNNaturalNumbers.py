# program for cube sum of first n natural numbers

n = int(input("Enter the n value"))
sum = 0
for i in range(1,n+1):
    sum = sum + pow(i,3)
print(sum)
list1 = [10,20,30,20,10,40,50,50,60,70,70]
n = len(list1)
new_list = []
for i in range(n):
    for j in range(i+1,n):
        if list1[i] == list1[j]:
            new_list.append(list1[i])
print(new_list)
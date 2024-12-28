list1 = []

for i in range(9):
    num = int(input())
    list1.append(num)

print(max(list1))
print(list1.index(max(list1))+1)
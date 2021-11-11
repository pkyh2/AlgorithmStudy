
list1 = ['aa', 'bbb', 'cc', 'b']
set1 = set()
cnt = 0
for i in range(len(list1)):
    set1.add(list1[i][0])
    cnt +=1

if len(set1) == cnt:
    print(1)
else:
    print(0)

set1 = set()
for i in range(10):
    A = int(input())
    set1.add(A % 42)

print(len(set1))
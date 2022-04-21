a, b = map(int, input().split())

if a >= b:
    for i in range(1, b+1):
        if a % i == 0 and b % i == 0:
            maxFactor = i
else:
    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            maxFactor = i
minFactor = (a // maxFactor) * (b // maxFactor) * maxFactor

print(maxFactor)
print(minFactor)

a = int(input())
b = int(input())

temp = b
print(a * (temp % 10))
temp = int(temp / 10)
print(a * (temp % 10))
temp = int(temp / 10)
print(a * temp)
print(a * b)
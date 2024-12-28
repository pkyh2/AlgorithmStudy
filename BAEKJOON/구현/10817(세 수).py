numbers = list(map(int, input().split()))
numbers.remove(max(numbers))
print(max(numbers))
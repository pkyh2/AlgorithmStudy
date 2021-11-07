import sys

T = int(input()) #Test case는 input()을 사용해도 된다.
for i in range(T):
		a, b = map(int, sys.stdin.readline().split())
		print(a+b)
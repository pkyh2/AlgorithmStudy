# 영화감독 숌

'''
영화제목에 666, 1666, 2666, 3666, ...
187 -> 66666
500 -> 166699

앞의 자리수가 1부터 올라가다가 6을 만나면 뒤에 자리수 0부터 9까지 올라간다

'''
# 풀이1 문자열
import sys
for _ in range(20):
    N = int(sys.stdin.readline())

    def numberSix(n):
        six = '666'
        for i in range(n):
            if i % 10 == 6:
                for j in range(10): # 0~9
                    result = six + str(j)
                return result
            else:
                result = str(i) + six
        
        return result

    print(numberSix(N))

# 풀이2
import sys
for _ in range(int(input())):
    
    N = int(sys.stdin.readline())

    def numberSix(n):
        six = '666'
        cnt = 1
        idx = 0
        nine_ten = 0
        num = 7
        i = 1
        while i <= n:
            if i <= 16:
                if i == 1:
                    result = '666'
                elif i <= 6:
                    result = str(i-1) + six
                else:
                    result = six + str(idx)
                    idx += 1
                i += 1
            else:
                nine_ten = 0
                for _ in range(9):
                    if num % 10 == 6:
                        num += 1
                    result = str(num) + six
                    num += 1

                    if i >= n: return result, i, num
                    i += 1
                    
                for _ in range(10):
                    result = str(cnt) + six + str(nine_ten)
                    nine_ten += 1
                    if i >= n: return result, i
                    i += 1
                cnt += 1

        return result, i

    print(numberSix(N))

# 1의 자리가 10의자리로 바뀌었을때 해결이 힘듬 ㅜㅜ..
            
'''
N : 1 ~ 5까지는
그냥 출력
'''
# 5  10  9  10  9   10  9   10  9 10  9   10  9   10    9   10  9   10  9
# 5  15  24 34  43  53  62  72 81 91  100 110 119 129   138 148 157 167 176

'''
666   1
1666 2
2666
3666
4666
5666
ㅡㅡㅡ
6660 7
6661
6662
6663 10
6664
6665
6666
6667
6668 15
6669 16
ㅡㅡㅡ
7666 17
8666
9666
10666 20
11666 21
12666 22
13666 23
14666 24
15666 25
ㅡㅡㅡ
16660 26
16661 27
16662
16663
16664 30
16665 31
16666 32
16667 33
16668 34
16669 35
ㅡㅡㅡ
17666 36
18666 37
19666 38
20666
21666 40
22666
23666
24666
25666 44
ㅡㅡㅡ
26660 45
26661
26662
26663
26664 
26665 50
26666
26667
26668
26669 54
ㅡㅡㅡ
27666 55
28666
29666
30666 58
31
32
33
34
35666 63
ㅡㅡㅡ
36660
.
.
.
96669
ㅡㅡㅡ
97666
98666
99666
100666
101666
102666
103
104
105
ㅡㅡㅡ
106660

106669
ㅡㅡㅡ
107666
108666
109666
110
'''


# 풀이3

import sys

N = int(sys.stdin.readline())
tripleSix = 666
while N != 0:
    if '666' in str(tripleSix):
        N -= 1
        if N == 0:
            break
    tripleSix += 1

print(tripleSix)

#29200KB 984ms
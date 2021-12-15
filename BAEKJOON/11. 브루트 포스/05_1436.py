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
N = int(sys.stdin.readline())

def numberSix(n):
    six = '666'
    cnt = 0
    idx = 0
    nine_ten = 0
    num = 7
    for i in range(n):
        cnt += 1
        if i <= 16:
            if i == 1:
                return 666
            elif i < 7:
                result = str(i) + six
            else:
                result = six + str(idx)
                idx += 1
        else:
            if nine_ten < 9:
                result = str(num) + six
                nine_ten += 1
                num += 1
            
            cnt = 7
            for i in range(9):
                result = str(cnt + i) + six
        return result
            
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
18666
19666
20666
21666 40
22666
23666
24666
25666 45
ㅡㅡㅡ
26660 46
26661
26662
26663
26664 50
26665 
26666
26667
26668
26669 55
ㅡㅡㅡ
27666 56
28666
29666
30666 58
31
32
33
34
35
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
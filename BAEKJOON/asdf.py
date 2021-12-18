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
                #while nine_ten < 9:
                # print(num)
                # print(i)
                a = num
                a %= 10 # 6



                for _ in range(9):
                    if num % 10 == 6:
                        num += 1
                    result = str(num) + six
                    num += 1

                    if i >= n: return result, i, num
                    i += 1
                    
                #while nine_ten < 10:
                for j in range(10):
                    result = str(cnt) + six + str(nine_ten)
                    nine_ten += 1
                    if i >= n: return result, i
                    i += 1
                cnt += 1

        return result, i

    print(numberSix(N))

# 1의 자리가 10의자리로 바뀌었을때 해결이 힘듬 ㅜㅜ..
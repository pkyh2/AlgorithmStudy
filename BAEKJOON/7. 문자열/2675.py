T = int(input())
QRcode = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:"

for i in range(T):                      # testcase 입력
    list1 = []
    R, S = input().split()              # 반복횟수, 반복단어 입력
    for j in S:                         # 반복단어 ex) ABC
        if j in QRcode:
            for k in range(int(R)):     # 입력한 횟수만큼 반복하여 list에 저장
                list1.append(j) #aaabbbccc

    print(''.join(list1))               # '구분자'.join(리스트)
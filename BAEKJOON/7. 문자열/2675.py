T = int(input())
QRcode = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:"

for i in range(T):
    list1 = []
    R, S = input().split()
    for j in S:
        if j in QRcode:
            for k in range(int(R)):
                list1.append(j)

    print(''.join(list1))
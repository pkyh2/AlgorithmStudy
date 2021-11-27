# ACM 호텔

'''
한 층에 W개의 방이 있는 H층 호텔에서 N번째 손님에게 배정하는 방 호수
선호하는 가까운 거리의 방은 낮은 층의 1번째 방을 선호한다. ex) 102호 < 301호
방 배정 ex) 101, 201, 301, ... 102, 202, 302,
'''

# 풀이 1(반복문)
'''
1. W, H 값을 입력받고 호텔의 방 호수를 선호 순서대로 리스트에 저장
2. N번째 해당하는 원소값을 출력
'''
T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    hotelRoom = []                              # 방번호 입력
    for i in range(1, W+1):                     # 호수 반복
        if i < 10:
            i = '0' + str(i)                    # 1 ~ 9호까지는 앞에 0을 붙여준다.
        for j in range(1, H+1):                 # 층수 반복
            hotelRoom.append(str(j) + str(i))   # 층수 + 호수
    
    print(hotelRoom[N-1])

# 풀이 2(일반식)
'''
1. 
'''
a = int(N/H)
b = N%H
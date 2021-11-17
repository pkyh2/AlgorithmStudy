# ACM 호텔

'''
한 층에 W개의 방이 있는 H층 호텔에서 N번째 손님에게 배정하는 방 호수
선호하는 가까운 거리의 방은 낮은 층의 1번째 방을 선호한다. ex) 102호 < 301호
'''

# 풀이 1
'''
1. W, H 값을 입력받고 호텔의 방 호수를 선호 순서대로 리스트에 저장
2. N번째 해당하는 원소값을 출력
'''
#T = int(input())

#for _ in range(T):
H, W, N = map(int, input().split())
hotelRoom = []
for i in range(1, W+1):
    for j in range(1, H+1):

        hotelRoom.append(str(j) + str(i))

print(hotelRoom)


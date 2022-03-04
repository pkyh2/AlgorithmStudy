# 스타트와 링크
'''
스타트팀 N//2명을 뽑고 나머지는 링크팀으로
팀 시너지 합을 계산후 차이가 최소인지 확인.

팀이 생길 수 있는 경우의 수를 나열
ex) 6명중 3명을 골라 나머지 3명은 뽑힌 3명이랑 중복x 순서o
commbination(range(1~6), 3)
'''
import sys
from itertools import combinations as combi
input = sys.stdin.readline

N = int(input())
player = [x for x in range(N)]
team = list(combi(player, int(N/2)))    # 팀 선발
for i in range(N):
    player[i] = list(map(int, input().split()))

min_value = N*N*100     # 최소 격차 초기값
for team_a in team:     # 1팀씩
    power_A = 0
    power_B = 0
    for x in team_a:    # 1명씩
        for y in team_a:
            power_A += player[x][y]                     # 11x, 12, 13, 21, 22x, 23, 31, 32, 33x
    team_b = [i for i in range(N) if i not in team_a]   # team_a에 없는 번호들
    for x in team_b:
        for y in team_b:
            power_B += player[x][y]
    min_value = min(min_value, abs(power_A - power_B))
print(min_value)
# 56000 6192
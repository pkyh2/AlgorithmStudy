'''
입출력 예시
money   costs(생산단가)              result
4578    [1, 4, 99, 35, 50, 1000]    2308
1999    [2, 11, 20, 100, 200, 600]  2789

화폐단위
1, 5, 10, 50, 100, 500

문제 풀이
1. 생산단가가 제일 낮은 순으로 화폐를 나눈다.

2. 즉 수익률이 가장 좋은 순서로 나눈다.
3. 그 순서대로 입력받는 money를 나누면서 화폐의 개수를 구한다.
4. 각각의 화폐개수와 생산단가를 곱해 생산 비용을 구한다.
'''
'''
new_dict = sorted(score_dict.items(), key=lambda x:x[1], reverse=True)
print(new_dict)
# [('aadi', 31), ('john', 30), ('mathew', 29), ('sachin', 28), ('riti', 27), ('sam', 23)]
'''

def solution(money, costs):
    answer = 0
    units = [1, 5, 10, 50, 100, 500]
    units_dict = {}
    for i in range(len(costs)):
        units_dict[units[i]] = (costs[i], costs[i]/units[i])
    rank = sorted(units_dict.items(), key=lambda x:x[1][1])
    moneyCnt = []
    
    for i in rank:
        moneyCnt.append((i[1][0], money//i[0]))
        money -= i[0]*moneyCnt[-1][1]
    print(moneyCnt)
    for i in moneyCnt:
        answer += i[0]*i[1]

    return answer

costs = [1, 4, 99, 35, 50, 1000]
print(solution(4578, costs))

costs = [2, 11, 20, 100, 200, 600]
print(solution(1999, costs))
def solution(dist):
    answer = [[]]
    disPos = {}
    maxDis = dist.index(max(dist))
    for i in range(len(dist[maxDis])):
        disPos[dist[maxDis][i]] = i

    sorted_dict = sorted(disPos.items(), key = lambda item: item[0])
    for i in sorted_dict:
        answer[0].append(i[1])
    answer.append(answer[0][::-1])
    answer.sort()
    return answer

dist = [[0,5,2,4,1],[5,0,3,9,6],[2,3,0,6,3],[4,9,6,0,3],[1,6,3,3,0]]
print(solution(dist))
dist = [[0,2,3,1],[2,0,1,1],[3,1,0,2],[1,1,2,0]]
print(solution(dist))
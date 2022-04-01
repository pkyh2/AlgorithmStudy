# level2
def deployFunc(deploy, answer):
    cnt = 0
    if len(deploy) > 1:
        for i in range(1, len(deploy)):
            if deploy[0] >= deploy[i]:
                cnt += 1
            else:
                deploy = deploy[i:]
                break
        print(deploy)
    else:
        return
    answer.append(cnt) 
    return deployFunc(deploy, answer)

def solution(progresses, speeds):
    answer = []
    deploy = []
    for i in range(len(progresses)):
        deploy.append((100 - progresses[i])/speeds[i])

    deployFunc(deploy, answer)
    # 100 - 93 / 1 == 7
    # 100 - 30 / 30 == 2.333
    # 100 - 55 / 4 == 9
    

    
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))
progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))
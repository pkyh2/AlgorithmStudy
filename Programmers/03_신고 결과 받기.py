def solution(id_list, report, k):
    answer = []
    warning = {}
    
    for i in id_list:
        for j in report:
            if i == j.split(' ')[0]:
                warning[j.split(' ')[1]] += 1

    # for key, val in warning.items():
    #     if val >= k:

    # return answer
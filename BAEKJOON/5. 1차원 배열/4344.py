'''
1. testcase 입력
2. 각 TC마다 각 Student 입력
3. 학생수까지 반복하면서 점수입력받을 list선언
4. 입력받는 점수의 평균 = 총합 / 학생의수
5. 평균과 학생의 점수를 비교하여 높은 학생의 수를 구한다.
6. {:.3f}.format(평균보다 높은 학생수 / 전체 학생수 * 100)
'''

T = int(input())

for i in range(T):
    list1 = list(map(int, input().split()))
    student = list1[0]
    scoreSum = sum(list1[1:])
    average = scoreSum / student
    cnt = 0
    for i in range(1, len(list1)):
        if list1[i] > average:
            cnt += 1
    result = (cnt / student) * 100
    print('{:.3f}%'.format(result))
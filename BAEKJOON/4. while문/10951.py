while True:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except:    # 더이상 입력은 안하고 Enter를 치면 break문이 실행된다.
        break
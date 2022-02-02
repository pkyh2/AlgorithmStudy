notSelfNum = list(range(1, 10000))

i = 1
selfnum = 0
while selfnum < 10000:
    if i < 10 and i+i in notSelfNum:
        notSelfNum.remove(i+i)
    else:
        selfnum += i
        while i > 0:
            selfnum += i % 10
            i // 10
        notSelfNum.remove(selfnum)
    i += 1


def solution(s):
    numbers = {"zero":'0', "one":'1', "two":'2', "three":'3', "four":'4', "five":'5', "six":'6', "seven":'7', "eight":'8', "nine":'9'}
    for key, val in numbers.items():
        if key in s:
            s = s.replace(key, val)
    return int(s)

s = "one4seveneight"
print(solution(s))
s = "123"
print(solution(s))
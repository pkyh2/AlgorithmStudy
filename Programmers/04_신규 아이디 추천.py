import re

def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    new_id = re.sub("\~|\!|\@|\#|\$|\%|\^|\&|\*|\(|\)|\=|\+|\[|\{|\]|\}|\:|\?|\,|\<|\>|\/", "", new_id)

    new_id = re.sub("\.\.+", ".", new_id)

    new_id = list(new_id.strip("."))

    if len(new_id) == 0:
        new_id.append('a')
    
    if len(new_id) >= 16:
        new_id = new_id[:15]
        while new_id[-1] == '.':
            new_id.pop()

    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id.append(new_id[-1])
    
    answer += ''.join(new_id)
    return answer

new_id = "...!@BaT#*..y.abcdefghijklm"
print(solution(new_id))
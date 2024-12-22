def solution(id_pw, db):
    for i in db:
      if i[0] == id_pw[0] and i[1] == id_pw[1]:
        return "login"
      elif i[0] == id_pw[0] and i[1] != id_pw[1]:
        return "wrong pw"
    return "fail"

id_pw = ["meosseugi", "1234"]
db = [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]
print(solution(id_pw, db))
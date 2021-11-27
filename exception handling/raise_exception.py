#defining and reaising exception
class tooyoung(Exception):
    def __init__(self,msg):
        self.msg=msg
class tooold(Exception):
    def __init__(self,msg):
        self.msg=msg
age=int(input("enter you age"))
if age > 60:
    raise tooold("too old for marrige")
elif age < 18:
    raise tooyoung("too young for marriage")
else:
    print("thanks for registration")


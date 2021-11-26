class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("hello", self.name,"your marks are",self.marks)
    def grades(self):
        if self.marks>=60:
            print("you have first grade")
        elif self.marks>=50:
            print("you have second grade")
        elif self.marks>=35:
            print("you have third grade")
        else:
            print("you are failed")

name=input("enter your name")
marks=int(input("enter your marks"))
s=student(name,marks)
s.display()
s.grades()

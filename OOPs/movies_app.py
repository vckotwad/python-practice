class movie:
    '''this class developed by vaibhav for demo'''
    def __init__(self,title,hero,heroin):
        self.title=title
        self.hero=hero
        self.heroin=heroin

    def info(self):
        print("movie name",self.title)
        print("movie name",self.hero)
        print("movie name",self.heroin)

l=[]
while True:
    t=input("enter name of the movie")
    h=input("enter hero of the movie")
    hr=input("enter heroine of the movie")
    m=movie(t,h,hr)
    l.append(m)
    print("movie added succesfully\n")
    p=input("do you wish to add another movie[y/n]")
    if p.lower()=='n':
        break

print("movies available are\n")
for x in l:
    print(x.info())
    print("\n")





    

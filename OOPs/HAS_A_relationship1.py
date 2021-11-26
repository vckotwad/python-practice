#has a relationship
class sportnews:
    def sportinfo(self):
        print("this is sport news")
class movienews:
    def movieinfo(self):
        print("this is movie news")
class politicsnews:
    def politicsinfo(self):
        print("this is politics news")

class totalnews:
    def __init__(self):
        self.sport=sportnews() 
        self.movie=movienews() 
        self.politics=politicsnews() 
    def totalinfo(self):
        print("showing total news as below")
        self.sport.sportinfo()
        self.movie.movieinfo()
        self.politics.politicsinfo()

total=totalnews()
total.totalinfo()
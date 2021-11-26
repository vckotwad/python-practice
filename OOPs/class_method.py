class bird:
    wings=2
    @classmethod
    def fly(cls,name):
        print("{} fly with {} wings".format(name,cls.wings))

bird.fly('parrot')
bird.fly('eagle ')
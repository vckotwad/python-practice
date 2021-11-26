class math:

    @staticmethod
    def add(a,b): # no reference variable is needed
        print('sum is',a+b)

    @staticmethod
    def prod(a,b):
        print('product is',a*b)
s=math()
s.add(10,20)
s.prod(10,20)

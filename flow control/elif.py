#elif statement
brand=input('enter your favorite brand')
if brand=='kf':
    print("it is children's brand")
elif brand=='ko':
    print('this is also too light')
elif brand=='rc':
    print('not much kick')
elif brand=='tuborg':
    print("it is also not good")
else:
    print('{} brands is not recommended'.format(brand))

def add(*n):
    # print(n[5])
    sum=0
    for i in n:
        sum += i

    print(sum)


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in n.items():
    #     print(key)
    #     print(value)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

class Car:

    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.color = kw.get('color')
        self.seat = kw.get('seat')

my_car=Car(make='Nissan', model='Skyline', color='green', seat=4)
print(my_car.make)
print(my_car.model)
print(my_car.color)
print(my_car.seat)

fruit=['a', 'b', 'c', 'd']
print(fruit.index('c'))
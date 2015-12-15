class Singleton(type):
    _instance = {}


'''
meta class is different in python3, fix code below later
'''


def __call__(cls, *args, **kwargs):
    if cls not in cls._instances:
        cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        cls.x = 5
    return cls._instances[cls]


class myclass(object):
    __metaclass__ = Singleton


m = myclass()
v = myclass()
print(m.x)
m.x = 10
print(v.x)

class MySingleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MySingleton, cls).__new__(cls)
            cls.number = 10
        return cls._instance


x = MySingleton()
print(x.number)
x.number = 20
y = MySingleton()
y.number = 30
print(x.number)

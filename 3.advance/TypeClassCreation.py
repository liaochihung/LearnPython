def printHam(self):
    print('ham')


class myclass(object):
    def __init__(self):
        self.x = 5


TypeClass = type("TypeClass", (), {"x": 5, "printHam": printHam})

m = myclass()
t = TypeClass()

print(m.x, t.x)
print(m == t)
print(type(m))

t.printHam()

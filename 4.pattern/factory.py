baseclass = type("baseclass", (object,), {})


@classmethod
def Check1(self, mystr):
    return mystr = "ham"


@classmethod
def Check2(self, mystr):
    return mystr="sandwich"


c1 = type("c1", (baseclass,), {"x": 1, "Check": Check1})
c2 = type("c2", (baseclass,), {"x": 2, "Check": Check2})

'''
def myfactory(mybool):
    return c1() if mybool else c2()

m = myfactory(True)
v = myfactory(False)

print(m.x, v.x)
'''


def myfactory(mystr):
    for cls in baseclass.__subclasses__():
        if cls.Check(mystr):
            return cls()


m = myfactory("ham")
v = myfactory("sandwich")

print(m.x, v.x)

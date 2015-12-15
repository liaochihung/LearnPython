'''
while True:
    try:
        number = int(input("Wat's your age?\n"))
        print(100/number)
        break
    except ValueError:
        print("Not a number")
    except ZeroDivisionError:
        print("Don't pick zero")
    except:
        print("Unknown error")
        break;
    finally:
        print("Loop complete")
'''

'''
class Tuna:
    def __init__(self):
        print("init")

    def swim(self):
        print("swim")

flipper = Tuna()
flipper.swim()
'''

''' Inheritance
class Parent():

    def printLastName(self):
        print('Roberts')

class child(Parent):

    def printFirstName(self):
        print('Bucky')

    def printLastName(self):
        print('snit')


bucky = child()
bucky.printFirstName()
bucky.printLastName()
'''

'''
#Multiple Inheritance
class Mario():

    def move(self):
        print("moving")


class Shroom():

    def eatShroom(self):
        print("I'm big")


class BigMario(Mario, Shroom):
    pass

bm = BigMario()
bm.move()
bm.eatShroom()
'''

'''
# zip
first = ['bucky', 'tom', 'taylor']
last = ['roberts', 'hanks', 'swift']

names = zip(first, last)

for a, b in names:
    print(a, b)
'''

'''
#Lambda
answer = lambda x: x*8
print(answer(5))
'''

stocks = {
    'goog': 555.55,
    'fb': 77.77,
    'yhoo': 39.32,
    'amzn': 333.32,
    'aapl': 66.663
}

# print(min(zip(stocks.values(), stocks.keys())))
# print(min(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.values(), stocks.keys())))

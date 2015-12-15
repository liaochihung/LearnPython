import random
import threading


def splitter(words):
    mylist = words.split()
    newlist = []
    while (mylist):
        newlist.append(mylist.pop(random.randrange(0, len(mylist))))
    print(' '.join(newlist))


if __name__ == '__main__':
    sentance = 'Hello world, this is a good day'
    numofthreads = 5
    threadlist = []

    print("starting...\n")
    for _ in range(numofthreads):
        t = threading.Thread(target=splitter, args=(sentance,))
        t.start()
        threadlist.append(t)

    print("\nThread Count: " + str(threading.active_count()))
    print("exitting...\n")

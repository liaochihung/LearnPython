import asyncio
import sys


@asyncio.coroutine
def goodbye_world():
    for i in range(10):
        print("goodbye world! {}".format(i))
        yield from asyncio.sleep(1)


@asyncio.coroutine
def hello_world():
    for i in range(10):
        print("hello world! {}".format(i))
        yield from asyncio.sleep(1)


def wait_input(loop, tasks):
    print('stopping')
    # for t in tasks:
    # t.cancel()
    loop.stop()


loop = asyncio.get_event_loop()
hello = asyncio.async(hello_world())
goodbye = asyncio.async(goodbye_world())

print("press any key to stop")
loop.add_reader(sys.stdin, wait_input, loop, [hello, goodbye])
loop.run_forever()

loop.close()

print("Finished!")

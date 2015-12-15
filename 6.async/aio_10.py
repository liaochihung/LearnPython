import asyncio


@asyncio.coroutine
def goodbye_world():
    for i in range(10):
        print("goodbye world")
        yield from asyncio.sleep(1)


@asyncio.coroutine
def hello_world():
    for i in range(10):
        print("hello world")
        yield from asyncio.sleep(1)


loop = asyncio.get_event_loop()
hello = asyncio.async(hello_world())
goodbye = asyncio.async(goodbye_world())

loop.run_forever()

loop.close()

print("Finished!")

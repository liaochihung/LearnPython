import asyncio


def hello(loop):
    for i in range(10):
        print('hello world')
    loop.stop()


loop = asyncio.get_event_loop()
loop.call_soon(hello, loop)
loop.run_forever()

loop.close()

print("Finished!")

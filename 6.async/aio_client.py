import asyncio

"""
can have more than one client
"""


@asyncio.coroutine
def callserver():
    n = 0
    while True:
        reader, writer = yield from asyncio.open_connection('127.0.0.1', 1234)
        print('sending msg...')
        msg = b'hello from client! ' + bytearray(str(n).encode())
        n += 1
        writer.write(msg)
        data = yield from reader.read(100)
        print('got msg from server: {}'.format(data.decode()))
        yield from asyncio.sleep(0.5)
    writer.close()


loop = asyncio.get_event_loop()
client = asyncio.async(callserver())

loop.run_forever()

loop.close()

print("client finished!")

import asyncio

"""
only one server
"""


@asyncio.coroutine
def handle_client(reader, writer):
    data = yield from reader.read(100)
    msg = data.decode()
    print('got msg: {}'.format(msg))

    writer.write(b'hello from server!')
    yield from writer.drain()
    writer.close()


loop = asyncio.get_event_loop()
server = asyncio.start_server(handle_client, '127.0.0.1', 1234)
print('running server...')
loop.run_until_complete(server)
loop.run_forever()

loop.close()

print("client finished!")

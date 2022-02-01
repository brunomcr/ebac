def coroutine_xyz():
    x = yield
    print(f'First yield a: {x}')
    y = yield
    print(f'\nSecond  yield b: {y}')
    yield
    print(f'\nSum yield = {x + y}')
    yield


def coroutine_abc():
    yield
    print('...')
    yield
    print('...')
    yield
    print('...')
    yield


try:
    z = coroutine_xyz()
    c = coroutine_abc()

    c.__next__()  # Start c
    z.__next__()  # Start z
    c.__next__()  # First yield from c
    z.send(100)   # Send first yield value to z
    c.__next__()  # Second yield from c
    z.send(299)   # Send second yield value to z
    c.__next__()  # Third yield from c
    z.__next__()  # Third yield from z

except StopIteration:
    pass

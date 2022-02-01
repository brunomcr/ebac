def generator():
    n = 1
    print(f'Print {n}')
    first_yield = yield n
    n += 1
    print(f'Print {n}')
    yield n
    n += 1
    print(f'Print {n}')
    yield n

my_list = [1, 2, 3, 4, 5]


# For Loop
for element in my_list:
    print(element)


# Iter Loop
iter_list = iter(my_list)
try:
    while True:
        print(next(iter_list))
except StopIteration:
    print('Finish!!!')

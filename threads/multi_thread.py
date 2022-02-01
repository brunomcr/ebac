import time
import threading


def calc_square(numbers):
    print(f'Calculating square numbers:\n')
    for num in numbers:
        time.sleep(2)
        print('square: {} \n'.format(str(num**2)))


def calc_cube(numbers):
    print(f'Calculating cube numbers:\n')
    for num in numbers:
        time.sleep(2)
        print('cube: {} \n'.format(str(num**3)))


if __name__ == '__main__':

    print('Main Thread Start')

    num_list = [2, 5, 7, 12]

    t1 = threading.Thread(target=calc_square, args=(num_list,))
    t2 = threading.Thread(target=calc_cube, args=(num_list,))

    print(f'First Thread Start')
    t1.start()
    print(f'Second Thread Start')
    t2.start()
    print(str(num_list))

    t1.join()
    t2.join()

    print('Main Thread Finish')
    print('Success!!!')

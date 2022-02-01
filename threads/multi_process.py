import multiprocessing

# Global Variable
results = []


def calc_square(numbers):
    global results
    print(f'Calculating square numbers:\n')
    for num in numbers:
        print('square: {} \n'.format(str(num**2)))
        results.append(num**2)
        print(f'within a results: '+str(results))


if __name__ == '__main__':

    print('....Start')

    num_list = [2, 5, 7, 12]

    p1 = multiprocessing.Process(target=calc_square, args=(num_list,))

    print(f'Process Start')
    p1.start()

    p1.join()

    print('result '+str(results))
    print('Success!!!')

import threading

from multithreading.count_three_sum import read_ints, count_three_sum
from multithreading.decorators import measure_time


@measure_time
def run_in_parallel(ints):
    t1 = threading.Thread(target=count_three_sum, args=(ints, 't1'), daemon=True)
    t2 = threading.Thread(target=count_three_sum, args=(ints, 't2'), daemon=True)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


@measure_time
def run_sequentially(ints):
    count_three_sum(ints, 'main')
    count_three_sum(ints, 'main')


if __name__ == '__main__':
    print('Started main')

    ints = read_ints(r'..\data\1Kints.txt')

    run_in_parallel(ints)
    run_sequentially(ints)

    print('Ended main')

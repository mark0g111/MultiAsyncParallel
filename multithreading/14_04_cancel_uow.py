import threading
import time

from multithreading.count_three_sum import read_ints


class ThreeSumUnitOfWorks(threading.Thread):
    def __init__(self, ints, name='TestThread'):
        super().__init__(name=name)
        self.ints = ints
        self.stop_event = threading.Event()

    def run(self):
        self.count_three_sum(self.ints)

    def cancel(self):
        self.stop_event.set()

    def count_three_sum(self, ints):
        print(f'started count_three_sum')

        n = len(ints)
        counter = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if self.stop_event.is_set():
                        print('Task was canceled')
                        print(f'Ended count_three_sum. Triplets counter={counter}')
                        return counter

                    if ints[i] + ints[j] + ints[k] == 0:
                        counter += 1
                        print(f'Triple found: {ints[i]}, {ints[j]}, {ints[k]}')

        print(f'Ended count_three_sum. Triplets counter={counter}')
        return counter


if __name__ == '__main__':
    print('Started main')

    ints = read_ints(r'..\data\1Kints.txt')

    task = ThreeSumUnitOfWorks(ints)
    task.start()

    time.sleep(5)

    task.cancel()

    task.join()

    print('Ended main')

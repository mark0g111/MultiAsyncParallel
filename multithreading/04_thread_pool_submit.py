import concurrent.futures
import time


def div(divisor, limit):
    print(f'Started div={divisor}')

    for x in range(1, limit):
        if x % divisor == 0:
            print(f'Divisor={divisor}, x={x}')
        time.sleep(0.2)
    print(f'Ended div={divisor}', end='\n')


if __name__ == '__main__':
    print('Started main')

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(div, 3, 25)
        executor.submit(div, 5, 25)

    print('After with block')

    # executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
    # executor.submit(div, 3, 25)
    # executor.submit(div, 5, 25)
    #
    # executor.shutdown(wait=True)
    #
    # print('Main Ended')

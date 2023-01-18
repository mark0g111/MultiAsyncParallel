import concurrent.futures
import time


def div(divisor, limit):
    print(f'Started div={divisor}')

    result = 0
    for x in range(1, limit):
        if x % divisor == 0:
            result += x
            print(f'Divisor={divisor}, x={x}')
        time.sleep(0.2)
    print(f'raise exception')
    raise Exception('bad things happen!')
    return result


# if __name__ == '__main__':
#     print('Started main')
#
#     with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
#         res_list = executor.map(div, (3, 5), (15, 25))
#         while res_list:
#             try:
#                 cur_list = next(res_list)
#             except StopIteration:
#                 print('Stop iteration excepted')
#                 break
#             except Exception as ex:
#                 print('General exception')
#                 print(repr(ex))
#         print('Ended main')


if __name__ == '__main__':
    print('Started main')
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(div, 3, 15)
        time.sleep(5)

        try:
            res = future.result()
        except Exception as ex:
            print(repr(ex))

    print('Ended main')

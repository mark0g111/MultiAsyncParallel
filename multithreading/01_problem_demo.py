from count_three_sum import read_ints, count_three_sum

if __name__ == '__main__':
    print('Started main')

    ints = read_ints(r'..\data\1Kints.txt')
    count_three_sum(ints)

    print('Ended main')

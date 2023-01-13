def read_ints(path):
    lst = []
    with open(path, 'r') as file:
        while line := file.readline():
            lst.append(int(line))

    return lst


def count_three_sum(ints):
    print('started count_three_sum')

    n = len(ints)
    counter = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if ints[i] + ints[j] + ints[k] == 0:
                    counter += 1
                    print(f'Triple found: {ints[i]}, {ints[j]}, {ints[k]}')

    print(f'Ended count_three_sum. Triplets counter={counter}')

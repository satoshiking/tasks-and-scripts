import itertools
def primes():
    counter = 2

    while True:
        for i in range(2, counter):
            if counter % i == 0:
                break
        else:
            yield counter
        counter += 1

print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
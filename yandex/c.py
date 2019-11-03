import itertools


"""
tests = []
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    tests.append(a)

print()
print(tests)
"""

tests= [[2,4,6,8]]

diff = []


for a in tests:
    # все пары лежаков из общего числа N
    combos = list(itertools.combinations(a,2))

    # для каждой пары вычисляем непохожесть
    for pair in combos:
        diff.append(pair[0]^pair[1])

    print(min(diff))

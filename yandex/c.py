import itertools


tests = []
diff = []

# считываем входные данные
with open("c_in.txt") as f:
    for i in range(int(f.readline())):
        n = f.readline().split()
        a = list(map(int, f.readline().split()))
        tests.append(a)


for a in tests:
    # все пары лежаков из общего числа N
    combos = list(itertools.combinations(a,2))

    # для каждой пары вычисляем непохожесть
    for pair in combos:
        diff.append(pair[0]^pair[1])

    print(min(diff))

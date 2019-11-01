import random
queries = []
chunks = []

# считывание параметров из файла
def data_from_file():
    with open("d_in.txt") as f:
        n, m, q = map(int, f.readline().split())
        chunks = list(map(int, f.readline().split()))
        for i in range(q):
            query = list(map(int, f.readline().split()))
            queries.append(query)

# генерация случайных параметров
def data_random():
    n = random.randint(5, 100000)
    m = random.randint(5, 5)
    q = random.randint(1, 100)

    for i in range(n):
        chunks.append(random.randint(1, m))

    for i in range(q):
        query = []
        query.append(random.randint(1, m))
        query.append(random.randint(1, m))
        while query[0] == query[1]:
            query[1] = random.randint(1, m)

        query.append(random.randint(1, n))
        #query.append(random.randint(query[2], query[2]))
        query.append(random.randint(query[2], n))
        queries.append(query)

data_random()

#print("n={} m={} q={}".format(n,m,q))
#print("N of chunks=", len(chunks), chunks)
#print("N of queris=", len(queries))



for q in queries:
    #print('запрос q=', q)
    s = chunks[ q[2]-1 : q[3] ]
    #print('   s=',s, 'q[0]=',q[0])
    if set(s) == set([q[0]]):
        print('1')
        chunks[ q[2]-1 : q[3] ] = [q[1]] * (q[3]-q[2]+1)
        #print("new CHUNKS = ", chunks)
    else:
        print('0')


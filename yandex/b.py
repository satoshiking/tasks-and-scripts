# описание задачи смотри в фале "B. Закрытый ключ.txt"
#x, y = map(int, input().split())

# разложение числа на простые множители
def primfacs(n):
    i = 2
    primfac = []

    while i * i <= n:
       while n % i == 0:
           primfac.append(i)
           n = n / i
       i = i + 1

    if n > 1:
       primfac.append(int(n))
    return primfac

# проверка имеют ли 2 числа общие делители отличные от 1
def is_common_divider(a,b):
    return True if set(primfacs(a)).intersection(set(primfacs(b))) else False

"""
 x*y = NOD(p,k) * NOK(p,k)
 x = NOD(p,k) * a
 y = NOD(p,k) * b,  a и b не имеют общих делителей кроме 1
 нужно найти все такие a и b
"""
def get_pk_num(x,y):
    if y % x == 0:
        n = int(y/x)
        nums = []
        for i in range(1,n+1):
            if n % i == 0:
                if not is_common_divider(i,int(n/i)):
                    nums.append([i,int(n/i)])
        print(len(nums))
        print(nums)
    else:
        print(0)


# testing block
import random
for i in range(3):
    a = random.randint(1,10000)
    b = random.randint(1,10000)

    print('testing num=', a, a*b)
    get_pk_num(a, a*b)
    print()

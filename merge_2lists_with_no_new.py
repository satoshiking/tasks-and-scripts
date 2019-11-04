"""
Даны два отсортированных массива A и B. В конце массива A достаточно свободного места, чтобы вместить массив B. 
Напишите метод слияния массивов A и B, сохраняющий сортировку.
"""
a = [1, 3, 5, 7, 8, 12, 15]
b = [2, 3, 9, 12]
print("на старте:")
print("a=", a)
print("b=", b)

# put inside of list a value n on m position
def shift(a,n,m):
    a.append(0);
    for i in range(len(a)-1, m, -1):
        a[i] = a[i-1]
    a[m] = n
    return a

def merge(a,b):
    for i in range(len(b)):
        for j in range(len(a)):
            if a[j] > b[i] and b[i] not in a:
                shift(a,b[i],j)
                break
merge(a,b)

print("на выходе a=", a)

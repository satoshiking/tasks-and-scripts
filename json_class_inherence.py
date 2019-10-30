import json
"""
student1 = {
    'first_name': 'Nikita',
    'last_name': 'Samoilov',
    'scores': [70,80,90]
}

student2 = {
    'first_name': 'Igor',
    'last_name': 'Smirnof',
    'scores': [20,30,40]
}

data = [student1, student2]
# формирование json
data_json = json.dumps(data, indent=4, sort_keys=True)
data_again = json.loads(data_json)
print(data_again)

# запись в файл
with open("students.json", "w") as f:
    json.dump(data, f, indent=4, sort_keys=True)


Вам дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть поле name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.

Пример:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

﻿Эквивалент на Python:

class A:
    pass

class B(A, C):
    pass

class C(A):
    pass

Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется явно от одного класса более одного раза.

Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.

<имя класса> : <количество потомков>

Выводить классы следует в лексикографическом порядке.

Sample Input:

[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
Sample Output:

A : 3
B : 1
C : 2
"""


#a_json = input()
#a = json.loads(a_json)

with open('classes.json', 'r') as f:
    a = json.load(f)

p = {}
for i in range(len(a)):
    p[a[i]["name"]] = a[i]["parents"]


def get_all_babies(c_name):
    all_babies = []
    for c in p:
        if (c_name in p[c]) and (c_name not in all_babies):
            if c not in all_babies:
                all_babies.append(c)

            lst_babies = get_all_babies(c)
            if lst_babies:
                for baby in lst_babies:
                    if baby not in all_babies:
                        all_babies.append(baby)

    return all_babies


sorted_types = sorted(p.items(), key=lambda kv: kv[0])
for i in range(len(sorted_types)):
    c_name = sorted_types[i][0]
    print(c_name, ':', len(get_all_babies(c_name))+1)

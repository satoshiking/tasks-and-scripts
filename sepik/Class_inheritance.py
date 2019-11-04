"""
Вам дано описание наследования классов в следующем формате.
<имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.
Класс A является прямым предком класса B, если B отнаследован от A:
Класс A является предком класса B, если
A = B;
A - прямой предок B
существует такой класс C, что C - прямой предок B и A - предок C
Вам необходимо отвечать на запросы, является ли один класс предком другого класса

Важное примечание:
Создавать классы не требуется.
Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого.

Формат входных данных
В первой строке входных данных содержится целое число n - число классов.

В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число q - количество запросов.

В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.

Формат выходных данных
Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2, и "No", если не является.
"""

input_list = []
output_list = []
parents_list = []

# Dictionary with key = class and value = parents of class
parents_dict = {}

# import sys
# sys.stdin = open("input.txt", "r")


for i in range(int(input())):
    input_list.append(input())

for i in range(int(input())):
    output_list.append(input())


def get_all_parents(class_name):
    all_parents = []
    parents = parents_dict.get(class_name)

    if parents:
        for parent in parents:
            if parent not in all_parents:
                all_parents.append(parent)
                all_parents.extend(get_all_parents(parent))
    return all_parents


def is_direct_parent(older_class, younger_class):
    parents = parents_dict.get(younger_class)
    if parents:
        return True if class_name in parents else False
    else:
        return False


def is_parent(class_name, parent):
    if (class_name == parent) and (parents_dict.get(class_name) is not None):
        return 'Yes'

    if is_direct_parent(class_name, parent):
        return 'Yes'

    all_parents_list = get_all_parents(parent)
    if class_name in all_parents_list:
        return 'Yes'

    return 'No'


for string in input_list:
    string_list = string.split(':')
    class_name = string_list[0].strip()

    if len(string_list) == 1:
        parents_dict[class_name] = []
    else:
        parents_list = string_list[1].strip().split()
        parents_dict[class_name] = parents_list

for string in output_list:
    class_name, parent = string.split()
    print(is_parent(class_name, parent))

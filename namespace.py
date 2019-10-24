"""
Реализуйте программу, которая будет эмулировать работу с пространствами имен. Необходимо реализовать поддержку создания пространств имен и добавление в них переменных.

В данной задаче у каждого пространства имен есть уникальный текстовый идентификатор – его имя.

Вашей программе на вход подаются следующие запросы:

create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
add <namespace> <var> – добавить в пространство <namespace> переменную <var>
get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из пространства <namespace>, или None, если такого пространства не существует

результатом работы get <namespace> <var> является

<namespace>, если в пространстве <namespace> была объявлена переменная <var>
get <parent> <var> – результат запроса к пространству, внутри которого было создано пространство <namespace>, если переменная не была объявлена
None, если не существует <parent>, т. е. <namespace>﻿ – это global
Формат входных данных
В первой строке дано число n (1 ≤ n ≤ 100) – число запросов.
В каждой из следующих n строк дано по одному запросу.
Запросы выполняются в порядке, в котором они даны во входных данных.
Имена пространства имен и имена переменных представляют из себя строки длины не более 10, состоящие из строчных латинских букв.

Формат выходных данных
Для каждого запроса get выведите в отдельной строке его результат.
"""

parents = {}
variables = {}
string_list = []


n = int(input())
for i in range(n):
    string_list.append(input())


def check(namespace, my_var):
    var_list = variables.get(namespace)

    if ((var_list is not None) and (my_var in var_list)):
        return namespace
    else:
        parent = parents.get(namespace)
        return None if parent is None else check(parent, my_var)


for string in string_list:
    command = string.split(' ')
    cmd = command[0]
    namespace = command[1]

    if cmd == 'add':
        variable = command[2]
        var_list = variables.get(namespace)

        if var_list is None:
            var_list = []
        var_list.append(variable)

        variables[namespace] = var_list
    elif cmd == 'create':
        parent = command[2]
        parents[namespace] = parent
    elif cmd == 'get':
        variable = command[2]
        print(check(namespace, variable))
    else:
        print('Ошибка')

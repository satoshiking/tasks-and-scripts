# print(re.search)
# print(re.findall)
# print(re.sub)   - замена

# [] множество подходящих символов
# . ^ $ * + ? { } [ ] \ | ( ) - метасимволы
# /d ~ [0-9]
# /D ~ [^0-9]
# /s ~ [ \t\n\r\fv] - пробельные символы
# /S ~ [^ \t\n\r\fv]
# /w ~ [a-zA-Z0-9_]
# /W ~ [^a-zA-Z0-9_]

# * повторы
# ? 0-1 вхождение
# + 1+ вхождений

# () - создание групп
# \1 - переиспользование группы номер 1

# Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор)

import re
import sys
sys.stdin = open("in.txt", "r")

s = r"\b(\w{1,30})\1\b"
pattern = re.compile(s)


for line in sys.stdin:
    line = line.rstrip()
    if pattern.search(line) is not None:
        print(line.rstrip())

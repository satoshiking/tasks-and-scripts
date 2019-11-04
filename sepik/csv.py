"""
Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

Файл с данными:
Crimes.csv
"""
import csv

types = {}

with open('crimes.csv','r') as f:
    reader = csv.reader(f)
    
    for row in reader:
        types[row[5]] = types.get(row[5], 0) + 1


sorted_types = sorted(types.items(), key=lambda kv: kv[1])
for i in range(len(sorted_types)):
    print("{: <35}   {: <10}".format(sorted_types[i][0], sorted_types[i][1]))


"""
lst = [
    ['value11', 'value21', 5, 6],
    ['value21', 'value22', 3, 4]
]

with open('out.csv', 'w') as f2:
    writer = csv.writer(f)
    #writer.writerows(lst)
    for each in lst:
        writer.writerow(each)
"""
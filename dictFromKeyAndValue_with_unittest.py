# coding: utf-8

import unittest

"""
Есть два списка разной длины. В первом содержатся ключи, а во втором значения.
Напишите функцию, которая создаёт из этих ключей и значений словарь.
Если ключу не хватило значения, в словаре должно быть значение None.
Значения, которым не хватило ключей, нужно игнорировать.
 Подробнее: http://company.yandex.ru/job/vacancies/dev_python_mysql.xml
"""
def dictFromKeyAndValue(key, value):
    #return dict(zip(key, value)) if (len(key) <= len(value)) else dict(map(None, key, value))
    if (len(key) <= len(value)):
        return dict(zip(key, value))
    else:
        return dict(map(None, key, value))


# Класс с юнит тестами
class createDict(unittest.TestCase):
    def testLenKeyEqLenValue(self):
        key = [1,2,3]
        value = ['q','w','e']

        result = {
          1: 'q',
          2: 'w',
          3: 'e'
        }

        self.assertEqual(dictFromKeyAndValue(key, value), result)

    def testLenKeyGtLenValue(self):
        key = [1,2,3,4,5]
        value = ['q','w','e']

        result = {
          1: 'q',
          2: 'w',
          3: 'e',
          4: None,
          5: None
        }

        self.assertEqual(dictFromKeyAndValue(key, value), result)

    def testLenKeyLteLenValue(self):
        key = [1,2,3]
        value = ['q','w','e', 'r', 't']

        result = {
          1: 'q',
          2: 'w',
          3: 'e'
        }

        self.assertEqual(dictFromKeyAndValue(key, value), result)


if __name__ == "__main__":
    unittest.main()

""""
Вам дано описание пирамиды из кубиков в формате XML.
Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue﻿).
Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.

Пример:
<cube color="blue">
  <cube color="red">
    <cube color="green">
    </cube>
  </cube>
  <cube color="red">
  </cube>
</cube>
 
Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 1. Кубики, расположенные прямо под ним, имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками, имеют ценность 3. И т. д.
Ценность цвета равна сумме ценностей всех кубиков этого цвета.

Выведите через пробел три числа: ценности красного, зеленого и синего цветов.
"""
from xml.etree import ElementTree

#xml = input()
xml = '<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>'
#tree = ElementTree.Parse("example.xml")
#root = tree.getroot() 
root = ElementTree.fromstring(xml)


def setChildLevel(path=".", lvl=1):
    for element in root.findall(path):
        element.set("lvl", lvl)

    path += "/cube"
    if root.findall(path):
        setChildLevel(path, lvl+1)


setChildLevel()
r, g, b = 0, 0, 0

for e in root.iter():
    if e.attrib["color"] == "red":
        r += e.attrib["lvl"]
    elif e.attrib["color"] == "green":
        g += e.attrib["lvl"]
    elif e.attrib["color"] == "blue":
        b += e.attrib["lvl"]

print(r, g, b)

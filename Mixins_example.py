import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, element):
        super(LoggableList, self).append(element)
        super(LoggableList, self).log(element)


b = LoggableList()
b.append(1)
b.append(2)

print(b)
b.clear()
print(b)
b.append(999)

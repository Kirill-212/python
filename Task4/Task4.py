import math


# Task4_1
class Iter:
    a = 1
    b = 1
    c = 1

    def __init__(self, size):
        self.count = 0
        self.size = size

    def __iter__(self):
        return self

    def __next__(self):
        allsum1 = self.a + self.b + self.c
        self.a = self.b
        self.b = self.c
        self.c = allsum1
        self.count += 1
        if self.count > self.size:
            raise StopIteration
        else:
            print(str(self.count) + " Эл " + str(self.c))
            return self.count


# Task4_2
class Rowlabe:
    sumall = 0
    count = 1
    first = ((-1) ** 0) / (2 * 0 + 1)
    e = 0.01

    def __iter__(self):
        self.sumall += self.first
        return self

    def __next__(self):
        left = self.retleft()
        res = self.retres()
        self.sumall += res
        if math.fabs(res - left) > self.e:
            print("Элемент ряда " + str(self.count) + "  " + str(res))
            self.count += 1
            return self.count
        else:
            print("Сумма ряда с точностью e=0.01----->" + str(self.sumall))
            raise StopIteration

    def retres(self, ):
        res = ((-1) ** self.count) / (2 * self.count + 1)
        return res

    def retleft(self):
        res = ((-1) ** (self.count - 1)) / (2 * (self.count - 1) + 1)
        return res


# Task4_1 test
it = Iter(35)
for i in it:
   print("*"*i)
print("^" * 10)
# Task4_2 test
labe = Rowlabe()
for i in labe:
    print("*"*i)
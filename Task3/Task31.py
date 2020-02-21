import math


# Task3_1 Start Variant1
class Trigon:
    __point1 = [0, 0]
    __point2 = [0, 0]
    __point3 = [0, 0]
    allsum = 0
    __side1 = 0
    __side2 = 0
    __side3 = 0
    name = "Произвольный"

    def __init__(self, x1=0, y1=0, x2=0, y2=0, x3=0, y3=0):
        print("Вызван конструктор с параметрами")
        self.__point1[0] = x1
        self.__point1[1] = y1
        self.__point2[0] = x2
        self.__point2[1] = y2
        self.__point3[0] = x3
        self.__point3[1] = y3

    def __del__(self):
        print("Объект удалён")

    def __setattr__(self, key, value):
        self.__dict__[key] = value
          # if key == "name" :
           #      self.__dict__[key] = value
           # else:
           #      raise AttributeError

    def get__point1(self):
        return self.__point1

    def get__point2(self):
        return self.__point2

    def get__point3(self):
        return self.__point3

    def set__point1(self, value):
        if 100 < value[0] < 0:
            value[0] = 0
        if 100 < value[1] < 0:
            value[1] = 0
        self.__point1 = value

    def set__point2(self, value):
        if 100 < value[0] < 0:
            value[0] = 0
        if 100 < value[1] < 0:
            value[1] = 0
        self.__point2 = value

    def set__point3(self, value):
        if 100 < value[0] < 0:
            value[0] = 0
        if 100 < value[1] < 0:
            value[1] = 0
        self.__point3 = value

    def Print(self):
        print("Был вызван метод вывода коорд.")
        print(self.__point1)
        print(self.__point2)
        print(self.__point3)

    def Perimetrandside(self):
        print("Был вызван метод определения сторон треугольника и определения периметра")
        self.allsum = round(
            math.sqrt(pow(self.__point1[0] - self.__point2[0], 2) + pow(self.__point1[1] - self.__point2[1], 2)))
        if self.allsum == 0:
            self.allsum = 1
            print("Это не треугольник сторона не может быть равно 0")
        elif self.allsum < 0:
            self.allsum = abs(self.allsum)
        self.__side1 = self.allsum
        print("Сторона 1->" + str(self.allsum))
        res = round(
            math.sqrt(pow(self.__point1[0] - self.__point3[0], 2) + pow(self.__point1[1] - self.__point3[1], 2)))
        if res == 0:
            res = 1
            print("Это не треугольник сторона не может быть равно 0")
        elif res < 0:
            res = abs(res)
        self.__side2 = res
        self.allsum += res
        print("Сторона 2->" + str(res))
        res = round(
            math.sqrt(pow(self.__point2[0] - self.__point3[0], 2) + pow(self.__point2[1] - self.__point3[1], 2)))
        if res == 0:
            res = 1
            print("Это не треугольник сторона не может быть равно 0")
        elif res < 0:
            res = abs(res)
        self.__side3 = res
        self.allsum += res
        print("Сторона 3->" + str(res))
        print("Периметр->" + str(self.allsum))

    def TriangleDefinition(self):
        print("Был вызван метод определния треугольника")
        if self.__side1 > self.__side2 and self.__side1 > self.__side3:
            if pow(self.__side2, 2) + pow(self.__side3, 2) == pow(self.__side1, 2):
                self.name = "Прямоугольный"
        elif self.__side2 > self.__side1 and self.__side2 > self.__side3:
            if pow(self.__side1, 2) + pow(self.__side3, 2) == pow(self.__side2, 2):
                self.name = "Прямоугольный"
        elif self.__side3 > self.__side2 and self.__side3 > self.__side1:
            if pow(self.__side2, 2) + pow(self.__side1, 2) == pow(self.__side3, 2):
                self.name = "Прямоугольный"
        elif self.__side1 == self.__side2 or self.__side1 == self.__side3 or self.__side2 == self.__side2:
            self.name = "Равнобедренный"
        if self.__side1 == self.__side2 and self.__side1 == self.__side3:
            self.name = "Равносторонний"


b = Trigon(1, 1, 5, 2, 4, 4)
b.Perimetrandside()
b.TriangleDefinition()
c = Trigon(1, 3, 1, 3, 4, 5)
c.Perimetrandside()
c.TriangleDefinition()
v = Trigon(1, 1, 3, 3, 4, 4)
v.Perimetrandside()
v.TriangleDefinition()
m = Trigon(1, -1, 2, 2, 4, 10)
m.Perimetrandside()
m.TriangleDefinition()
b.Print()
print(b.get__point2())
b.Perimetrandside()
b.TriangleDefinition()
print(b.name)
lst = [b, c, v, m]
count1 = 0
count2 = 0
count3 = 0
count4 = 0
for i in range(len(lst) - 1):
    if lst[i].name == "Равносторонний":
        count1 += 1
    elif lst[i].name == "Прямоугольный":
        count2 += 1
    elif lst[i].name == "Равнобедренный":
        count3 += 1
    elif lst[i].name == "Произвольный":
        count4 += 1
print("Равносторонних-" + str(count1))
print("Прямоугольных-" + str(count2))
print("Равнобедренных-" + str(count3))
print("Произвольных-" + str(count4))
count1 = 0
count2 = 0
count3 = 0
count4 = 0
for i in range(len(lst) - 1):
    if lst[i].name == "Равносторонний":
        if count1 < lst[i].allsum:
            count1 = lst[i].allsum
    elif lst[i].name == "Прямоугольный":
        if count2 < lst[i].allsum:
            count2 = lst[i].allsum
    elif lst[i].name == "Равнобедренный":
        if count3 < lst[i].allsum:
            count3 = lst[i].allsum
    elif lst[i].name == "Произвольный":
        if count4 < lst[i].allsum:
            count4 = lst[i].allsum

print("Наибольший периметр Равносторонних треугольников " + str(count1))
print("Наибольший периметр Прямоугольных треугольников " + str(count2))
print("Наибольший периметр Равнобедренных треугольников " + str(count3))
print("Наибольший периметр Произвольных треугольников " + str(count4))
for i in range(len(lst) - 1):
    if lst[i].name == "Равносторонний":
        if count1 > lst[i].allsum:
            count1 = lst[i].allsum
    elif lst[i].name == "Прямоугольный":
        if count2 > lst[i].allsum:
            count2 = lst[i].allsum
    elif lst[i].name == "Равнобедренный":
        if count3 > lst[i].allsum:
            count3 = lst[i].allsum
    elif lst[i].name == "Произвольный":
        if count4 > lst[i].allsum:
            count4 = lst[i].allsum

print("min периметр Равносторонних треугольников " + str(count1))
print("min периметр Прямоугольных треугольников " + str(count2))
print("min периметр Равнобедренных треугольников " + str(count3))
print("min периметр Произвольных треугольников " + str(count4))
# Task3_1 end


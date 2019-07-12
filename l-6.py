# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math
class Triangle:
    def __init__(self, a_x, a_y, b_x, b_y, c_x, c_y):
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        self.c_x = c_x
        self.c_y = c_y
        self.ab = round(math.sqrt(int(math.fabs(((b_x - a_x) ** 2) + ((b_y - a_y) ** 2)))))
        self.bc = round(math.sqrt(int(math.fabs(((c_x - b_x) ** 2) + ((c_y - b_y) ** 2)))))
        self.ca = round(math.sqrt(int(math.fabs(((a_x - c_x) ** 2) + ((a_y - c_y) ** 2)))))

    def perimeter(self):
        self.perimeter = (self.ab + self.bc + self.ca)
        return self.perimeter

    def square(self):
        self.square = round(math.sqrt((self.perimeter / 2) * ((self.perimeter / 2) - self.ab) * ((self.perimeter / 2) - self.bc) * ((self.perimeter / 2) - self.ca)))
        return self.square

    def hight(self):
        self.hight = round(((2 * self.square) / self.ab), 2)
        return self.hight

triangle_1 = Triangle(1, 1, 1, 3, 4, 1)

print(f"Периметр {triangle_1.perimeter()}")
print(f"Площадь {triangle_1.square()}")
print(f"Высота {triangle_1.hight()}")


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

import math
class Trapezoid:
    def __init__(self, a_x, a_y, b_x, b_y, c_x, c_y, d_x, d_y):
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        self.c_x = c_x
        self.c_y = c_y
        self.d_x = d_x
        self.d_y = d_y
        self.ab = round(math.sqrt(int(math.fabs(((b_x - a_x) ** 2) + ((b_y - a_y) ** 2)))))
        self.bc = round(math.sqrt(int(math.fabs(((c_x - b_x) ** 2) + ((c_y - b_y) ** 2)))))
        self.cd = round(math.sqrt(int(math.fabs(((c_x - d_x) ** 2) + ((c_y - d_y) ** 2)))))
        self.da = round(math.sqrt(int(math.fabs(((d_x - a_x) ** 2) + ((d_y - a_y) ** 2)))))

    def perimeter(self):
        self.perimeter = (self.ab + self.bc + self.da + self.cd)
        return self.perimeter

    def hight(self):
        self.hight = round(math.sqrt(int((self.ab ** 2) -
                                     (((((self.da - self.bc) ** 2) + (self.ab ** 2) - (self.cd ** 2))
                                       / (2 * (self.da - self.bc))) ** 2))))
        return self.hight

    def square(self):
        self.square = round((self.bc + self.da) / 2 * self.hight())
        return self.square

trapezoid_1 = Trapezoid(1, 1, 2, 3, 3, 3, 4, 1)

print(f"Периметр {trapezoid_1.perimeter()}")
print(f"Площадь {trapezoid_1.square()}")
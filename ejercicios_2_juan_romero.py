# POO exercises
import math


class figura():
    _side1 = 0
    _side2 = 0
    _side3 = 0

    def __init__(self, side1, side2, side3):
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3

    def area(self):
        pass

    def perimeter(self):
        pass


class rectangle(figura):
    def __init__(self, side1, side2):
        self._side1 = side1
        self._side2 = side2

    def area(self):
        return self._side1 * self._side2

    def perimeter(self):
        return (self._side1 * 2) + (self._side2 * 2)


class triangle(figura):
    def __init__(self, side1, side2, side3):
        super().__init__(side1, side2, side3)

    def perimeter(self):
        return self._side1 + self._side2 + self._side3

    def semiPerimeter(self):
        return self.perimeter() / 2

    def area(self):
        return math.sqrt(self.semiPerimeter() * (self.semiPerimeter() - self._side1) *
                         (self.semiPerimeter() - self._side2) * (self.semiPerimeter() - self._side3))


test = rectangle(4, 3)
area = test.area()
perimeter = test.perimeter()
print('El area es rectangulo es: ', area)
print('El perimetro es rectangulo es: ', perimeter)

test2 = triangle(3, 3, 3)
perimeter1 = test2.perimeter()
area1 = test2.area()
print('\nEl area es Triangulo es: ', area1)
print('El perimetro es Triangulo es: ', perimeter1)


class student():
    __name = ''
    __email = ''
    __password = ''

    def __init__(self, name, email, password):
        self.__name = name
        self.__email = email
        self.__password = password

    def getName(self):
        return self.__name

    def getEmail(self):
        return self.__email

    def getPassword(self):
        return self.__password


est = student('Juan Romero', 'jjose.reomero@ejemplo.com', 'ejemplopassword')
name = est.getName()
email = est.getEmail()
password = est.getPassword()
print('\nNombre: ', name)
print('Correo: ', email)
print('Password: ', password)

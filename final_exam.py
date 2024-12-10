# 12장 상속

import math


class Car:  # 부모 클래스 or 슈퍼 클래스
    def __init__(self, make, model, color, price):
        self.make = make
        self.model = model
        self.color = color
        self.price = price

    def setMake(self, make):
        self.make = make

    def getMake(self):
        return self.make

    def getDesc(self):
        return f"차량 = {self.make}, {self.model}, {self.color}, {self.price}"


class ElectricCar(Car):  # 자식 클래스 or 서브 클래스 <- 부모 클래스를 변수로 받음
    def __init__(self, make, model, color, price, battarySize):
        super().__init__(make, model, color, price)
        self.battarySize = battarySize

    def setBatterySize(self, battarySize):
        self.battarySize = battarySize

    def getBatterySize(self):
        return self.battarySize


def main():
    myCar = ElectricCar("Tisla", "Model S", "white", 10000, 0)  # 인스턴스 변수 선언
    myCar.setMake("Tesla")  # 부모클래스에 있는 메소드 이용
    myCar.setBatterySize(60)  # 자식 클래스에 있는 메소드 이용
    print(myCar.getDesc())  # 부모클래스에 있는 메소드 이용하여 값을 문자열로 호출


main()


class Animal:  # 부모 클래스
    def __init__(self, age=0):  # 클래스 선언시 age가 없다면 default = 0으로 저장
        self.age = age

    def eat(self):  # 메소드 호출시 아래 문장 출력
        print("동물이 먹고 있습니다.")


class Dog(Animal):  # 자식 클래스
    def __init__(self, age=0, name=""):
        super().__init__(age)
        self.name = name

    def getAnimal(self):
        return self.name

    def setAge(self, age):
        self.age = age


d = Dog()  # d를 dog클래스로
print(d.age)  # 0출력
d.setAge(10)  # 나이 10으로 설정
print(d.age)  # 10 출력
print(d.getAnimal())  # 이름 선언하면 출력될 예정~~

print(type(d))  # main 스크립트의 dog 클래스이다. __main__.Dog
c = Animal()

print(isinstance(d, Animal))  # True
print(isinstance(d, Dog))  # True
print(isinstance(c, Animal))  # True
print(isinstance(c, Dog))  # False


class Parent(object):
    def __init__(self):
        self.__money = 100  # private 변수

    def getMoney(self):
        return self.__money


class Child(Parent):
    def __init__(self):
        super().__init__()


# obj = Child()
# print(obj.__money) -> 오류 private를 가져오니까..!
obj = Parent()
# print(obj.__money) -> 마찬가지로 오류
print(obj.getMoney())  # return 사용해서 받아오기 가능


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)


class Student:
    def __init__(self, id):
        self.id = id

    def getId(self):
        return self.id


class CollegeStudent(Person, Student):  # 다중 상속
    def __init__(self, name, age, id):
        Person.__init__(
            self, name, age
        )  # super 쓰면 하나가 못받음 아마도 Student의 데이터 변수를 못받음
        Student.__init__(self, id)


obj = CollegeStudent("Kim", 22, "100036")
obj.show()
print(obj.id)


class Shape:
    def __init__(self):
        pass

    def draw(self):
        print("draw 메소드 호출")

    def get_area(self):
        print("get_area 메소드 호출")


class Circle(Shape):
    def __init__(self, radius=0):
        super().__init__()
        self.radius = radius

    def draw(self):
        super().draw()  # 부모클래스의 메소드 호출
        print("원을 그립니다.")  # override

    def get_area(self):
        return math.pi * self.radius**2


c = Circle(10)  # 반지름이 10인 원을 자식 클래스에 선언
c.draw()  # 원을 그립니다가 호출
print(c.get_area())  # 원의 면적 출력


class Book:
    def __init__(self, title, isbn):
        self.__title = title
        self.__isbn = isbn

    def __repr__(self):
        return f"ISBN : {self.__isbn}; TITLE : {self.__title}"


book = Book("Python", "0123456")
print(book)  # __repr__없으면 객체 형태로 주소값 출력


class MyTime:
    def __init__(self, hour, minute, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return "%.2d:%.2d:%.2d" % (self.hour, self.minute, self.second)


time = MyTime(10, 25)
print(time)


class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f"{self.a + other.a}, {self.b + other.b}"


a = Point(1, 5)
b = Point(2, 4)

print(a + b)

# 14장 넘파이
import numpy as np
import matplotlib.pyplot as plt

# plt.plot([15.6,14.2,16.3,18.2,17.1,20.2,22.4]) # x축 정의 x -> 자동으로 index가 x축
# plt.show()

X = [1, 2, 3, 4, 5, 6, 7]
X = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

Y1 = [15.6, 14.2, 16.3, 18.2, 17.1, 20.2, 22.4]
Y2 = [20.1, 23.1, 23.8, 25.9, 23.4, 25.1, 26.3]

# plt.xlabel("day")
# plt.ylabel("temp")
# plt.plot(X, Y1, X, Y2)
# plt.show()

ftemp = [63,73,80,86,84,78,66,54,45,63]

F=np.array(ftemp)
C=(F-32)*5/9

print(C)
plt.plot(F)
plt.plot(C)
plt.show()
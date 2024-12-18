# 8장 객체와 클래스(기말고사 파트)

class Television:
    serialNumber = 0  # 클래스 변수, 대체적으로 상수, 클래스 내에서 변수 선언

    def __init__(self, channel, volume, on):  # 인스턴스 변수, 외부에서 변수 선언
        self.channel = channel
        self.volume = volume
        self.on = on
        Television.serialNumber += 1  # 클래스 변수 숫자 증가
        self.number = (
            Television.serialNumber
        )  # 클래스 변수의 값을 인스턴스 변수에 값을 저장

    def show(self):  # 출력
        print(self.channel, self.volume, self.on, self.number)


def setSilentMode(t):
    t.volume = 2


t = Television(11, 10, True)
s = t
setSilentMode(t)
t.show()

if s is t:
    print("s와 t는 동일한 객체를 참조")

if s is not t:
    print("s와 t는 동일한 객체를 참조하지 X")


# 10장 파일과 예외처리
try:
    mylist = [0] * 10

    num = mylist[10]
    print(num)
except IndexError:
    print("인덱스 오류")
finally:
    print("10장 끄으읕")


# 11장 내장함수
a = [1, 2, 3, 4, 5]
b = [-6, 7, -8, 9, -10]

print(list(enumerate(a)))
print(list(zip(a, b)))

invitations = ["Kim", "Lee", "Park", "Choi"]
persons = [1, 3, 0, 6]
print(sum(persons))
print(any(persons))
print(all(persons))
print(max(persons))


print(sorted(b))
print(b.sort())  # 반환값 None
b.sort()
print(b)

print(
    sorted(
        "The health Know not of their health, but only the sick".split(), key=str.upper
    )
)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<이름: {self.name}, 나이: {self.age}>"


A = [Person("홍길동", 20), Person("최자영", 38), Person("김철수", 35)]

print(sorted(A, key=lambda person: person.age, reverse=True))

f_temp = [0, 10, 20, 30, 40, 50]

f = lambda temp: (5.0 / 9.0) * (temp - 32.0)

c_temp = map(f, f_temp)
print(list(c_temp))

orders = [
    ["1", "재킷", 5, 120000],
    ["2", "셔츠", 6, 24000],
    ["3", "바지", 3, 50000],
    ["4", "코드", 6, 300000],
]

t = lambda x: (x[0], x[2] * x[3])

C = list(map(t, orders))
print(C)

mylist = [True, True, True]
print(all(mylist))

mytuple = (0, 1, False)
print(any(mytuple))

t = ["BBB", "AAA", "aaa", "bbb"]

print(sorted(t))

lst_1 = ["A", "B", "C"]
lst_2 = [1, 2, 3]

print(list(zip(lst_1, lst_2)))

result = (lambda x: x * 2)(2)
print(result)
result = (lambda x: (x + 3) * 5 / 2)(3)
print(result)


numbers = [1, 2, 3, 4, 5, 6]
print(list(map(lambda x: x + 1, numbers)))
print(list(filter(lambda x: x % 2, numbers)))

# class X:
#     def __init__(self):
#         print("X: __init__()")

# class Y(X):
#     def  __init__(self):
#         print("Y:__init__()")

# print(y=Y())

class X:
    def __init__(self, a):
        self.a = a

    def inc(self):
        self.a+=1

    def __repr__(self):
        return f"VALUE: {self.a}"
    
print(X(20))

"""
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


# 15장 판다스

import pandas as pd

titanic = pd.read_csv("C://Users//User//Desktop//중앙대//2학년//2학기//객지프//과제//titanic.csv")

# print(max(titanic.Age))
# print(titanic.Age.max())
# print(titanic["Age"].max())

titanic.to_excel("C://Users//User//Desktop//중앙대//2학년//2학기//객지프//과제//titanic.xlsx", sheet_name='passengers',index=False)

# print(titanic[titanic.Age < 20].head())
# print(titanic[titanic.Pclass.isin([1,3])])
print(titanic.loc[titanic.Age < 20, "Name"])
print(titanic.sort_values(by=["Pclass", "Age"], ascending=False).head())

print(titanic[["Sex", "Pclass", "Age"]].groupby("Sex").mean())
print(titanic.groupby(["Sex","Pclass"])[["Fare","Age"]].mean())
"""


import numpy as np

my_vector = np.array([1,2,3,4,5,6])
selection = my_vector % 2 == 0

print(my_vector[selection])

first_matrix = np.array([[1,2,3],[4,5,6]])
second_matrix = np.array([1,2,3])

print(first_matrix+second_matrix)

A=np.zeros(10)

A[4] += 1

print(A)

B=np.arange(10,20)
print(B)

C=np.arange(0,10)
C=C[::-2]

print(C)
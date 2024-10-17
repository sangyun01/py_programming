# 8주차 객체와 클래스

# Lab: TV 클래스 정의

class TVsettings:
    def __init__(self):
        self.channel = 0
        self.volume = 0
        self.turnon = False

    def show(self):
        self.turnon = True
        print(f"{self.channel} {self.volume} {self.turnon}")
    
    def setChannel(self, channel):
        self.channel = channel
    
    def getChannel(self, channel):
        self.channel = channel
        return self.channel
    
    def setVolume(self, volume):
        self.volume = volume

samsung = TVsettings()
samsung.show()
samsung.setChannel(11)
samsung.setVolume(10)
samsung.show()

# Lab: 원 클래스 정의

import math

class Circle:
    def __init__(self, radius):
        self.r = radius

    def getArea(self):
        self.area = math.pi * self.r**2
        return self.area

    def getPrimeter(self):
        self.Primeter = math.pi * 2 * self.r
        return self.Primeter

circle = Circle(10)

a = circle.getArea()
p = circle.getPrimeter()

print(f"원의 면적 {a}")
print(f"원의 둘레 {p}")

# Lab: 자동차 클래스 정의

class Car:
    def __init__(self, maker_model, color, year, price, speed):
        self.model = maker_model
        self.carcolor = color
        self.caryear = year
        self.carprice = price
        self.speed = speed

    def carspeed(self):
        self.speed = 60

myCar = Car("E-class", "black", 10, "$100,000", 0)

print("자동차 객체를 생성하였습니다.")
print(f"자동차의 속도는 {myCar.speed}")
print(f"자동차의 색상은 {myCar.carcolor}")
print(f"자동차의 모델은 {myCar.model}")
print(f"자동차의 연식은 {myCar.caryear}")
print(f"자동차의 가격은 {myCar.carprice}")

myCar.carspeed()
print(f"자동차의 속도는 {myCar.speed}")

# Lab: 은행 계좌

class Account:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, money):
        if money > 0:
            self.__balance += money
            print(f"통장에 {money}가 입금되었음")
        else:
            print("입금 금액은 0원을 초과하여야합니다.")

    def withdraw(self, money):
        if money > 0:
            if self.__balance >= money:
                self.__balance -= money
                print(f"통장에서 {money}가 출금되었음")
            else:
                print("잔액 부족")
        else:
            print("출금 금액은 0원을 초과하여야합니다.")

    def get_balance(self):
        return self.__balance

Kookmin = Account(50000)
Kookmin.deposit(10000)
Kookmin.withdraw(5000)

print(f"현재 잔액 {Kookmin.get_balance()}")

# Lab: 클래스 변수

class Dog:
    kind = "Bulldog"  # 품종이 모두 동일하니까 클래스 변수로만 두기

    def __init__(self, name, age):  # 이름 나이는 다를 수 있기 때문에 인스턴스 변수
        self.name = name
        self.age = age

dogdetail = Dog("ZZANGGU", 5)

print(f"{dogdetail.name}의 나이는 {dogdetail.age}, 품종은 {dogdetail.kind}")


# Lab: 2차원 벡터

class Cal:
    def __init__(self, a, b):
        self.x1 = a
        self.y1 = b

    def __add__(self, other):
        self.addx = self.x1 + other.x1
        self.addy = self.y1 + other.y1
        return Cal(self.addx, self.addy)

    def __sub__(self, other):
        self.subx = self.x1 - other.x1
        self.suby = self.y1 - other.y1
        return Cal(self.subx, self.suby)

    def __str__(self):  # 튜플 형태로 반환 -> 안쓰면 메모리 주소가 출력
        return f"({self.x1}, {self.y1})"

vector1 = Cal(0, 1)
vector2 = Cal(1, 0)

add_result = vector1 + vector2
sub_result = vector1 + vector2
print(f"{vector1} + {vector2} = {add_result}")
print(f"{vector1} - {vector2} = {sub_result}")

# Lab: 주사위 클래스

import random

class Dice:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.value = 0

    def roll_dice(self):
        self.value = random.randint(1, 6)

    def read_dice(self):
        return self.value

    def print_dice(self):
        print(f"주사위의 위치는 x:{self.x}, y:{self.y}에 있다.")
        print(f"주사위의 크기는 {self.size}이며 굴린 주사위의 값은 {self.value}이다.")

dice = Dice(10, 10, 10)

dice.roll_dice()
dice.print_dice()

dice.roll_dice()
value = dice.read_dice()  # 다시 굴려서 값 변동 확인
print(f"주사위의 값 : {value}") # 처음과 값이 다르게 나올 수 있음 


print("가현아 지민아 공부해라~")
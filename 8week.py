# 8주차 객체와 클래스
"""
# Lab: TV 클래스 정의

class TVsettings:
    def __init__(self, channel, volume, ON):
        self.setChannel = channel
        self.getvolume = volume
        self.turnon = ON

    def show(self):
        print(f"{self.setChannel} {self.getvolume} {self.turnon}")

samsung = TVsettings(11, 20, True)
samsung.show()

# Lab: 원 클래스 정의

import math

class Circle:
    def __init__(self, radius):
        self.r = radius
        self.area = 0
        self.Primeter = 0

    def getArea(self):
        self.area = math.pi * self.r**2

    def getPrimeter(self):
        self.Primeter = math.pi * 2 * self.r

circle = Circle(10)

circle.getArea()
circle.getPrimeter()

print(f"원의 면적 {circle.area}")
print(f"원의 둘레 {circle.Primeter}")

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
"""

# Lab: 클래스 변수


# Lab: 2차원 벡터


# Lab: 주사위 클래스

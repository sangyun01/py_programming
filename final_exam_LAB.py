# Lab: 2차원 벡터
class Cal:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        self.calx = self.x + other.x
        self.caly = self.y + other.y
        return Cal(self.calx, self.caly)

    def __sub__(self, other):
        self.calx = self.x - other.x
        self.caly = self.y - other.y
        return Cal(self.calx, self.caly)

    def __str__(self):
        return f"({self.x}, {self.y})"
    
val1 = Cal(0,1)
val2 = Cal(1,0)

addval = val1 + val2
subval = val1 - val2

print(f"{val1}+{val2}={addval}")
print(f"{val1}-{val2}={subval}")

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

# 10장

# Lab: CVS 파일 처리
import csv

f = open(
    "C://Users//SamSung//OneDrive//바탕 화면//대학교//제10장 파일과 예외처리(2024) - data//weather.csv"
)
data = csv.reader(f)
header = next(data)

#채우기

print(f"가장 추웠던 날의 기온은 {low_temp}ºC입니다.")

# Lab : 디렉토리 안의 파일 처리

import os
arr = os.listdir()

for f in arr:
    print(f)
    if not os.path.isfile(f):
        print("not file")
        continue
    infile = open(f, "r", encoding="utf-8", errors="ignore")
    lines = infile.readlines()

    for line in lines:
        e = line.rstrip()
        if "Python" in e :
            print(f, ":", e)
    infile.close()

#Lab : 이미지 파일 복사하기
infile = open("C://Users//SamSung//OneDrive//바탕 화면//대학교//제10장 파일과 예외처리(2024) - data//123.png", "rb") #read binary rb인 이유 -> 이미지 파일이라서/ txt, csv 파일은 r
outfile = open("C://Users//SamSung//OneDrive//바탕 화면//대학교//제10장 파일과 예외처리(2024) - data//copy_file.png", "wb") #write binary

data = infile.read()
outfile = outfile.write(data)

#Lab: 정규식 이용하기
infile = open("C://Users//SamSung//OneDrive//바탕 화면//대학교//제10장 파일과 예외처리(2024) - data//number.txt", "r")

course_name = []

for line in infile:
    text_content = line.split()
    course_name.append(text_content[0])

print(course_name)

# Lab: 패스워드 검사 프로그램

import re

pw = input("패스워드를 입력하시오 : ")
decidepw = False

while True:
    if len(pw) < 8:
        break
    elif not re.search("[a-z]", pw):
        break
    elif not re.search("[A-Z]", pw):
        break
    elif not re.search("[0-9]", pw):
        break
    elif not re.search("[_@$]", pw):
        break
    else:
        decidepw = True
        break

if decidepw == True:
    print("올바른 PW")
else:
    print("PW 재설정")



# 12장 상속

# Lab : Bank 클래스
class Bank:
    def getInterestRate(self):
        return 0.0

# 채우기 : 순서대로 이자율 10 / 5 / 3

b1 = BadBank()
b2 = NormalBank()
b3 = GoodBank()

print(f"BadBank의 이자율:{str(b1.getInterestRate())}")
print(f"NormalBank의 이자율:{str(b2.getInterestRate())}")
print(f"GoodBank의 이자율:{str(b3.getInterestRate())}")

# Lab : 직원과 매니저
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getsalary(self):
        return self.salary
    
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        #채우기

    def getsalary(self):
        #채우기
    
    def __repr__(self):
        return f"이름: {str(self.name)}; 월급: {str(self.salary)}; 보너스: {str(self.bonus)}"

kim = Manager("김철수", 2000000, 1000000)
print(kim)

# Lab: 은행 계좌
class BankAccount:
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, name, number, balance, interest_rate):
        #채우기 이자율 -> 실수형

    def add_interest(self):
        #채우기 -> 호출될때마다 예금에 이자 더하기

class CheckingAccount(BankAccount):
    def __init__(self, name, number, balance):
        #채우기

    def withdraw(self, amount):
        #채우기
    
a1 = SavingsAccount("홍길동", 123456, 10000, 0.05)
a1.add_interest()
print(f"저축예금의 잔액 = {a1.balance}")

a2 = CheckingAccount("김철수", 123457, 2000000)
a2.withdraw(100000)
print(f"당좌예금의 잔액 = {a2.balance}")

# Lab : Card와 Deck

class Card:
    suitNames = ["클럽", "다이아몬드", "하트", "스페이드"]
    rankNames = [None, "에이스", "2", "3", "4", "5",
        "6", "7", "8", "9", "10", "잭", "퀸", "킹"]

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f"{Card.suitNames[self.suit]} {Card.rankNames[self.rank]}"

class Deck:
    def __init__(self):
        #채우기

    def __str__(self):
        #채우기

deck = Deck()
print(deck)

#Lab: 학생과 강사
class Person:
    def __init__(self, name, number):
        self.name = name
        self.number =  number

class Student(Person):
    UNDERGRADUATE = 0
    POSTGRADUATE = 1

    def __init__(self, name, number, studentType):
        super().__init__(name, number)
        self.studentType = studentType
        self.gpa = 0
        self.classes = []

    def enrollCourse(self, course):
        self.classes.append(course)

    def __str__(self):
        return f"이름={self.name}\n주민번호={self.number}\n수강과목={str(self.classes)}\n평점={str(self.gpa)}"

class Teacher(Person):
    def __init__(self, name, number):
        #채우기

    def assignTeaching(self, course):
        #채우기
        
    def __str__(self):
        #채우기

hong = Student("홍길동", "12345678", Student.UNDERGRADUATE)
hong.enrollCourse("자료구조")
print(hong)

kim = Teacher("김철수", "123456790")
kim.assignTeaching("Python")
print(kim)

#Lab: Vehicle와 Car, Truck

class Vehicle:
    def __init__(self, name):
        self.name = name

    def drive(self):
        raise NotImplementedError("이것은 추상메소드입니다.")
    
    def stop(self):
        raise NotImplementedError("이것은 추상메소드입니다.")

class Car(Vehicle):
    def drive(self):
        return "승용차를 운전합니다."
    
    def stop(self):
        return "승용차를 정지합니다."
    
class Truck(Vehicle):
    def drive(self):
        return "트럭을 운전합니다."
    
    def stop(self):
        return "트럭을 정지합니다."
    
cars = [Truck("truck1"), Truck("truck2"), Car("car1")]

for car in cars:
    print(f"{car.name} : {car.drive()}")

# for car in cars:
#     print(f"{car.name} : {car.stop()}")


# 14장 넘파이

# Lab: BMI 계산하기
import numpy as np

heights = [1.83, 1.76, 1.69, 1.86, 1.77, 1.73]
weights = [86, 74, 59, 95, 80, 68]

#채우기

print(bmi)

# Lab: 잡음이 들어간 직선 그리기

import matplotlib.pyplot as plt
import numpy as np

purse = #채우기
noise = #채우기

signal = #채우기

plt.plot(signal)
plt.show()

# Lab: 정규 분포 그래프 그리기
import numpy as np
import matplotlib.pyplot as plt

m, sigma = 10, 2

#채우기


# Lab: sin함수 그리기

import numpy as np
import matplotlib.pyplot as plt

#채우기


#Lab: MSE 오차 계산하기
import numpy as np

ypred = np.array([1,0,0,0,0])
y=np.array([0,1,0,0,0])

#채우기

#Lab: 직원들의 월급 인상하기
#채우기


#Lab: 그래프 그리기
import matplotlib.pyplot as plt
import numpy as np
#채우기


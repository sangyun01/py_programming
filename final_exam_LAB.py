"""
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

low_temp = 100

for temp in data:
    if float(temp[3]) < low_temp:
        low_temp = float(temp[3])

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

# 11주차 내장 함수

# Lab: 내장 함수 예제
invitations = ["Kim", "Lee", "Park", "Choi"]
persons = [1, 3, 0, 6]
print(sum(persons))

if any(persons):
    print("파티에 한 사람이라도 옵니다.")
else:
    print("파티에 모든 그룹이 오지 않습니다.")

if all(persons):
    print("파티에 초대받은 모든 그룹이 옵니다.")
else:
    print("파티에 초대받은 그룹 중 일부만 옵니다.")

print(f"파티에 가장 많이 오는 그룹의 인원 수는 {max(persons)}")

# Lab : 키를 이용한 정렬 예제
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<이름 : {self.name}, 나이 : {self.age}>"


persons = [Person("홍길동", 20), Person("김철수", 35), Person("최자영", 38)]

def keyage(Person):
    return Person.age

print(sorted(persons, key=keyage))

# Lab : 람다식으로 온도 변환하기
f_temp = [0, 10, 20, 30, 40, 50]

c_temp = map(lambda T: (5.0 / 9.0) * (T - 32), f_temp)

print(list(c_temp))

# Lab : 람다식으로 데이터 처리하기
orders = [
    ["1", "재킷", 5, 120000],
    ["2", "셔츠", 6, 24000],
    ["3", "바지", 3, 50000],
    ["4", "코드", 6, 300000],
]

func = lambda mon : (mon[0],mon[2]*mon[3])

print(list(map(func, orders)))

# Lab: 피보나치 이터레이터
class Fiblterator:
    def __init__(self, a=1, b=0, maxValue=50):
        self.a = a
        self.b = b
        self.max = maxValue

    def __iter__(self):
        return self

    def __next__(self):
        sum = self.a + self.b
        if sum > self.max:
            raise StopIteration
        else:
            self.a = self.b
            self.b = sum
            return sum

for i in Fiblterator():
    print(i, end=" ")


# Lab: Book 클래스
class Book:
    def __init__(self, title="", page=0):
        self.title = title
        self.page = page

    def __repr__(self):
        return self.title

    def __gt__(self, other):
        return self.title > other.title

    def __add__(self, other):
        return self.page + other.page

book1 = Book("Magic or Python", 600)
book2 = Book("Master or Python", 700)

print(book1 > book2)
print(book1 + book2)

# Lab: 동전 던지기 게임
import random

myList = ["head", "tail"]

while True:
    ans = input("동전 던지기를 계속하시겠습니까?(yes, no)")

    if ans == "yes":
        print(random.choice(myList))
    else:
        break

# 12장 상속

# Lab : Bank 클래스
class Bank:
    def getInterestRate(self):
        return 0.0

class BadBank:
    def __init__(self, rate = 10.0):
        self.rate = rate
    def getInterestRate(self):
        return self.rate
    
class NormalBank:
    def __init__(self, rate = 5.0):
        self.rate = rate
    def getInterestRate(self):
        return self.rate
    
class GoodBank:
    def __init__(self, rate = 3.0):
        self.rate = rate
    def getInterestRate(self):
        return self.rate

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
        super().__init__(name, salary)
        self.bonus = bonus

    def getsalary(self):
        return self.salary + self.bonus
    
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
        super().__init__(name, number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance*0.05

class CheckingAccount(BankAccount):
    def __init__(self, name, number, balance):
        super().__init__(name, number, balance)

    def withdraw(self, amount):
        self.balance -= amount + 10000
    
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
        self.cards = []
        for suit in range(0,4):
            for rank in range(0,14):
                self.cards.append(Card(suit, rank))

    def __str__(self):
        l= [str(card) for card in self.cards]
        return str(l)

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
        super().__init__(name, number)

    def assignTeaching(self, course):
        self.course = course
        self.salary = 3000000
        
    def __str__(self):
        return f"이름={self.name}\n주민번호={self.number}\n강의과목={str(self.course)}\n월급={str(self.salary)}"

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
"""

# 14장 넘파이

# Lab: BMI 계산하기
import numpy as np

heights = [1.83, 1.76, 1.69, 1.86, 1.77, 1.73]
weights = [86, 74, 59, 95, 80, 68]

bmi = np.array(weights) / (np.array(heights) ** 2)

print(bmi)

# Lab: 잡음이 들어간 직선 그리기

import matplotlib.pyplot as plt
import numpy as np

purse = np.linspace(1, 10, 100)
noise = np.random.normal(size=100)

signal = purse + noise

# plt.plot(signal)
# plt.show()


# Lab: 정규 분포 그래프 그리기
import numpy as np
import matplotlib.pyplot as plt

m, sigma = 10, 2

number1 = np.random.randn(10000)
number2 = m + sigma * np.random.randn(10000)

# plt.hist(number1)
# plt.hist(number2)
# plt.show()


# Lab: sin함수 그리기

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)

y1 = np.sin(x)
y2 = 3 * np.sin(x)
# plt.plot(x,y1,x,y2)
# plt.show()

# Lab: MSE 오차 계산하기
import numpy as np

ypred = np.array([1, 0, 0, 0, 0])
y = np.array([0, 1, 0, 0, 0])

mse = np.mean((ypred - y) ** 2)
print(mse)

# Lab: 직원들의 월급 인상하기
salary1 = np.array([220,250,230])
salary2 = np.array([220,250,230])
salary3 = np.array([220,250,500])
salary1 += 100
salary2 *= 2

print(salary1)
print(salary2)
print(salary3[salary3>450])

# Lab: 그래프 그리기
import matplotlib.pyplot as plt
import numpy as np

x= np.linspace(0,10,1000)

y=np.ones(len(x))
y1=x
y2=x**2

plt.plot(x,y,x,y1,x,y2)
plt.show()

x=np.zeros(10)
x[4]=1

x=np.arange(10,20)
x=np.linspace(0,9,10)

x=x[::-1]

print(x)
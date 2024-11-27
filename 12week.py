# 12장 상속

# Lab : Bank 클래스
class Bank:
    def getInterestRate(self):
        return 0.0

class BadBank:
    def getInterestRate(self):
        return 10.0

class NormalBank:
    def getInterestRate(self):
        return 5.0

class GoodBank:
    def getInterestRate(self):
        return 3.0

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
        return super().getsalary() + self.bonus
    
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
        self.balance += self.balance * self.interest_rate

class CheckingAccount(BankAccount):
    def __init__(self, name, number, balance):
        super().__init__(name, number, balance)
        self.withdraw_charge = 1000

    def withdraw(self, amount):
        self.balance = self.balance - amount - self.withdraw_charge
    
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
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

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
        self.salary = 3000000
        self.courses = []

    def assignTeaching(self, course):
        self.courses.append(course)
        
    def __str__(self):
        return f"이름={self.name}\n주민번호={self.number}\n강의과목={str(self.courses)}\n월급={str(self.salary)}"

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
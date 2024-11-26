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

"""
# Lab : 직원과 매니저
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getsalary(self):
        return self.salary
    
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def getsalary(self):
        return super().getsalary()
    
    def __repr__(self):
        return f"이름: {str(self.name)}; 월급: {str(self.salary)}; 보너스: {str(self.bonus)}"

kim = Manager("김철수", 2000000, 1000000)
print(kim)

#Lab: 은행 계좌
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
"""
"""
# Lab : Card와 Deck


class Card:
    suitNames = ["클럽", "다이아몬드", "하트", "스페이드"]
    rankNames = [
        None,
        "에이스",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "잭",
        "퀸",
        "킹",
    ]

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return Card.suitNames[self.suit] + "" + Card.rankNames[self.rank]

class Deck:
    def __init__(self):

    def __str__(self):
        l=[]
        for card in self.cards:
            l.append(str(card))

        l= [str(card) for card in self.cards] -> 동일

deck = Deck()
print(deck)
"""





class Teacher(Person):
    def __init__(self, name, number):
        super().__init(name, number)
        self.salary = 1000
        self.courses = []

    def assignTeaching(self, course):
        self.courses.append(course)
        










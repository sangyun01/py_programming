# 12장 상속

# Lab : Bank 클래스
class Bank:
    def getInterestRate(self):
        return 0.0


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
    
    




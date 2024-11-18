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
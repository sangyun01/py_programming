# 살려줘요

# 2week

# Lab: 별까지의 거리 계산하기
c = 3 * 10**5
distance = 40 * 10**12
time = distance / c
year = time / (60 * 60 * 24 * 365)

print(f"{year}")

# Lab: 원기둥의 부피 계산

import math

r = 5
h = 10
v = math.pi * r**2 * h

print(f"반지름 = {r} 높이는 {h} 원기둥의 부피 = {v}")

# Lab: 복리 계산

first_money = 24
year = 382
money = first_money * 1.06**year

print(f"원리금{money}")

# Lab: 로봇 기자 만들기

place = input("경기장은 어디입니까? ")
win = input("이긴팀은 어디입니까? ")
lose = input("진팁은 어디입니까? ")
mvp = input("우수선수는 누구입니까? ")
score = input("스코어는 몇대몇입니까? ")

print("=" * 20)
print(f"오늘 {place}에서 야구 경기가 열렸습니다.")
print(f"{win}과 {lose}는 치열한 공방전을 펼쳤습니다.")
print(f"{mvp}이 맹활약을 하였습니다.")
print(f"결국 {win}rk {lose}를 {score}로 이겼습니다.")
print("=" * 20)

# Lab: 대화하는 프로그램 만들기

print("안녕하세요?")

name = input("이름이 어떻게 되시나요? ")
print(f"만나서 반갑습니다. {name}씨")
print(f"이름의 길이는 다음과 같군요: {len(name)}")

age = int(input("나이가 어떻게 되나요?"))
print(f"내년이면 {age+1}이 되시는군요.")

# Lab: BMI 계산하기

weight = int(input("몸무게를 kg 단위로 입력하시오: "))
height = float(input("키를 미터 단위로 입력하시오: "))
print(f"당신의 BMI = {weight/height**2}")

# Lab: 구의 부피 계산하기
import math

radius = float(input("반지름을 입력하시오"))
volume = math.pi * radius**3 * 4 / 3

print(f"구의 부피는 {volume}")

# Lab: 자동판매기 프로그램

price = int(input("물건값을 입력하시오 : "))

ten = int(input("1000원의 지폐 개수: "))
five = int(input("500원의 동전 개수: "))
one = int(input("100원의 동전 개수: "))

total_price = 1000 * ten + 500 * five + 100 * one
total_price = total_price - price

re_500 = total_price // 500
total_price -= re_500 * 500
re_100 = total_price // 100
total_price -= re_100 * 100
re_10 = total_price // 10
re_1 = total_price % 10

print(f"500원 = {re_500}, 100원 = {re_100}, 10원 = {re_10}, 1원 = {re_1}")

# 3week

# Lab: 산술 퀴즈 프로그램 - +)도전

import random

a = random.randint(1, 100)
b = random.randint(1, 100)

if a % 2 == 0:
    sum = a + b
    ans = int(input(f"{a} + {b} = "))

    if sum == ans:
        print("True")
    else:
        print("false")
else:
    sub = a - b
    ans = int(input(f"{a} - {b} = "))

    if sub == ans:
        print("True")
    else:
        print("false")

# Lab: 산술 퀴즈 프로그램

num1 = int(input("정수를 입력하시오 :"))
num_d = ("짝수입니다." if (num1 % 2 == 0) else "홀수입니다.")

print(num_d)

# Lab: 산술 퀴즈 프로그램 - 도전문제 1

num1 = int(input("정수를 입력하시오 :"))
num_d = ("양수입니다." if (num1 > 0) else "음수입니다.")
print(num_d)

# Lab: 산술 퀴즈 프로그램 - 도전문제 2

score = int(input("성적을 입력해주세요 : "))
score_d = ("합격입니다." if score >= 60 else "불합격입니다.")

print(score_d)

# Lab : 세일 가격 계산

price = int(input("정가를 입력하시오 : "))

if price >= 100:
    print("10층에서 사은품을 받아가세요.")
    print(f"할인된 가격 = {price * 0.85}")
else:
    print(f"할인된 가격 = {price * 0.9}")

# Lab: 물의 상태 출력하기

temp = int(input("온도를 입력하시오: "))

if temp >= 100:
    print("기체상태입니다.")
elif temp >= 0:
    print("액체상태입니다.")
else:
    print("고체상태입니다.")

#Lab: 동전 던지기 게임
import random

print("동전 던기기 게임을 시작합니다.")

coin = random.randint(0,1)
x = ("앞면입니다." if coin == 0 else "뒷면입니다.")
print(x)
print("게임이 종료되었습니다.")

#Lab: 리히티 규모
scale = float(input("리히터 규모를 입력하시오: "))

if scale < 2.0:
    print("지진계에 의해서만 탐지 가능합니다.")
elif scale <=3.9:
    print("물건들이 흔들리거나 떨어집니다.")
elif scale < 6.9:
    print("빈약한 건물에 큰 피해가 있습니다.")
elif scale < 7.9:
    print("지표면에 균열이 발생합니다.")
else:
    print("대부분의 구조물이 파괴됩니다.")

# Lab: 사용자 입력 검증하기

print("=" * 25)
print("메뉴 1번 : 치즈 버거")
print("메뉴 2번 : 치킨 버거")
print("메뉴 3번 : 불고기 버거")
print("=" * 25)
menu = int(input("메뉴를 선택하세요: "))

if menu == 1:
    print("치즈 버거")
elif menu == 2:
    print("치킨 버거")
elif menu == 3:
    print("불고기 버거")
else:
    print("잘못입력하셨습니다.")

# Lab: 축구게임
import random

defence = int(input("어디를 수비하시겠어요?(왼쪽: 1, 중앙: 2, 오른쪽: 3)"))

num1 = random.randint(1, 3)
if num1 == defence:
    print("페널티킥에 실패했습니다.")
else:
    print("페널티킥이 성공하였습니다.")

# Lab: 올바른 삼각형 구분
a = int(input("삼각형의 한 변을 입력하시오 : "))
b = int(input("삼각형의 한 변을 입력하시오 : "))
c = int(input("삼각형의 한 변을 입력하시오 : "))

if (a + b > c) & (a + c > b) & (b + c > a):
    print("올바른 삼각형")

# 4week

# Lab: 팩토리얼 계산하기
num = int(input("정수를 입력하시오: "))
fac = 1

for i in range(1, num):
    fac *= i
print(f"{num}!은 {fac}입니다.")

# Lab: 팩토리얼 계산하기 - 도전문제
num1 = int(input("정수를 입력하시오: "))
fac = 1

for i in range(num1, 0, -1):
    fac *= i

print(f"{num}!은 {fac}입니다.")

# Lab: 방정식의 해 구하기 - 이분법
count = 100
xu = 2
xl = 1

for i in range(count):
    xmid = (xu + xl) / 2
    f = xmid**2 - xmid - 1

    if f > 0:
        xu = xmid
    elif f < 0:
        xl = xmid
    count += 1
print(f"방정식의 해는 {xmid}")

# Lab: 구구단 출력
num = int(input("원하는 단은 : "))

for i in range(1,10):
    print(f"{num}*{i}={num*i}")

# Lab: 숫자 맞추기 게임
import random

num = random.randint(1, 100)
count = 0
print("1부터 100사이의 숫자를 맞추시오")

while True:
    num1 = int(input("숫자를 입력하시오: "))
    count += 1

    if num1 > num:
        print("너무 높음!")
    elif num1 < num:
        print("너무 낮음!")
    else:
        print(f"축하합니다. 시도횟수는 {count}")

# Lab: 초등생을 위한 산수 문제 발생기
import random

while True:
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    sum = int(input(f"{a}+{b}="))
    if a + b == sum:
        print("잘했어요!!")
    else:
        print("틀렸어요. 하지만 다음번에는 잘할 수 있죠?")

# Lab: 로그인 프로그램
password = "pythonisfun"

while True:
    pw = input("암호를 입력하시오: ")

    if password == pw:
        print("로그인 성공")
        break
        
# Lab: 주사위 합이 6이 되는 경우

for i in range(1,7):
    for j in range(1, 7):
        if i +j ==6:
            print(f"첫 번째 주사위 = {i}, 두 번째 주사위 = {j}")

#Lab: 모든 조합 출력하기
persons = ["Kim", "Park", "Lee", "Choi"]
restaurants = ["Korean", "American", "French", "Chinese"]

for person in persons:
    for restaurant in restaurants:
        print(f"{person}이 {restaurant}식당을 방문")

#Lab: 소수 찾기
count = 0
num = 2

while count < 50:
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime == True:
        print(num)
        count +=1
    num +=1

#Lab: 파이 계산하기

rept = int(input("반복횟수: "))
pi = 0

for i in range(1, rept+1):
    pi += 4*(1/(2*i-1))*(-1)**(i+1)

print(f"Pi = {pi}")

#Lab: 도박상의 확률
import random

print("초기 금액 $50")
print("목표 금액 $250")

initial = 50
goal = 250
count = 0

for i in range(100):
    price = initial

    while True:
        num = random.randint(0,1)
        if num == 1:
            price -= 1
        else:
            price += 1
            
        if price == goal:
            count +=1
            break
        elif price == 0:
            break

print(f"100번 중에서 {count}번 성공")

# Lab: 피자 크기 비교
import math


def area(x):
    return x * x * math.pi


print(f"20cm 피자 2개의 면적 : {area(20)*2}")
print(f"30cm 피자 1개의 면적 : {area(30)}")


# Lab: 환영 문자열 출력 함수
def display(msg, count):
    for i in range(count):
        print(msg)


display("환영합니다.", 5)


# Lab: 환영 문자열 출력 함수 - 도전
def display(msg="Welcome", count=5):
    for i in range(count):
        print(msg)


display()


# Lab: 환영 문자열 출력 함수 - 도전
def display(count, *msg):
    for i in range(count):
        for m in msg:
            print(m)

display(3, "123", "456")

# Lab: 이분법

def func(x):
    return x**2 - x - 1

def root(x1, x2):
    xl = x1
    xu = x2
    count = 0

    if func(xl) * func(xu) > 0:
        print("범위 내 근 X")

    while True:
        count += 1
        mid = (xl + xu) / 2

        if func(xl) * func(mid) < 0:
            xu = mid
        elif func(xl) * func(mid) > 0:
            xl = mid
        else:
            return mid

        if count > 50:
            break

print(f"{root(1,3)}")

# Lab : 주급 계산 프로그램

def weeklyPay(rate, hour):
    if hour > 30:
        money = rate * 30 + (hour - 30) * rate * 1.5
    else:
        money = rate * hour
    return money

money = int(input("시급을 입력하시오: "))
hour = int(input("근무 시간을 입력하시오: "))

print(f"주급은 {weeklyPay(money, hour)}")

# Lab: 여러 개의 값 반환
def pri():
    name = input("이름: ")
    age = int(input("나이: "))
    return name, age

name, age = pri()

print(f"이름은 {name}이고 나이는 {age}살입니다.")

# Lab : 구조화 프로그래밍 실습

def print_menu():
    print("1. 섭씨 온도 -> 화씨 온도")
    print("2. 화씨 온도 -> 섭씨 온도")
    print("3. 종료")
    menu_num = int(input("메뉴를 선택하세요: "))

    return menu_num

def trans_temp(temp, menu):
    if menu == 1:
        temp = temp * 9 / 5 + 32
    elif menu == 2:
        temp = (temp - 32) * 5 / 9

    return temp

while True:
    a = print_menu()

    if a == 1:
        cel = float(input("섭씨온도를 입력하시오: "))
        f = trans_temp(cel, a)

        print(f"화씨 온도 = {f}")
    elif a == 2:
        f = float(input("화씨온도를 입력하시오: "))
        cel = trans_temp(f, a)

        print(f"화씨 온도 = {cel}")
    elif a == 3:
        break
    else:
        print("잘못입력하셨습니다.")

        


# 해치웠나? ~ 5장
# 4주차 반복문


# Lab: 팩토리얼 계산하기
num = int(input("정수를 입력하시오: "))
fac = 1

for i in range(1, num + 1):
    fac *= i

print(f"{num}!은 {fac}이다.")

# Lab: 팩토리얼 계산하기 - 도전문제
num = int(input("정수를 입력하시오: "))
fac = 1

for i in range(num, 0, -1):
    fac *= i

print(f"{num}!은 {fac}이다.")

# Lab: 방정식의 해 구하기
count = 100
START = 1.0
END = 2.0

for i in range(count):
    x = START + i * ((END - START) / count)
    f = x**2 - x - 1
    if abs(f - 0.0) < 0.01:
        print(f"방정식의 해는 {x}")

# Lab: 방정식의 해 구하기 - 도전문제1
count = 100000
START = 1.0
END = 2.0

for i in range(count):
    x = START + i * ((END - START) / count)
    f = x**2 - x - 1
    if abs(f - 0.0) < 0.0001:
        print(f"방정식의 해는 {x}")
# 방정식의 해가 여러개 발생하며, 해의 유효숫자의 개수가 증가한다. 하나의 해만을 출력하기 위해서는 break함수를 사용해야한다.

# Lab: 방정식의 해 구하기 - 도전문제2
count = 100
START = 1.0
END = 2.0

for i in range(count):
    x = (START + END) / 2
    f = x**2 - x - 1

    if f > 0.0:
        END = x
    elif f < 0.0:
        START = x
    else:
        print(f"방정식의 해는 {x}")
        break  # 하나의 해만 출력

# Lab: 구구단 출력
dan = int(input("원하는 단은: "))
i = 1

while i <= 9:
    print(f"{dan} X {i} = {dan*i}")
    i += 1

# Lab: 숫자 맞추기 게임
import random

num = random.randint(1, 100)
number = 0
cnt = 0
print("1부터 100사이의 숫자를 맞추시오")

while number != num:
    number = int(input("숫자를 입력하시오: "))
    cnt += 1
    if number > num:
        print("너무 높음!")
    elif number < num:
        print("너무 낮음!")
    else:
        break

print(f"축하합니다. 시도횟수 = {cnt}")

# Lab: 초등생을 위한 산수 문제 발생기
import random

x = 0
y = 0
ans = 0

while True:
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    ans = int(input(f"{x} + {y} = "))
    if ans == (x + y):
        print("잘했어요!!")
    else:
        print("틀렸어요. 하지만 다음번에는 잘할 수 있죠?")
        break

# Lab: 로그인 프로그램
pw = "pythonisfun"

while True:
    password = input("암호를 입력하시오: ")
    if pw == password:
        print("로그인 성공")
        break

# Lab: 주사위의 합이 6이 되는 경우
for x in range(1, 7):
    for y in range(1, 7):
        if x + y == 6:
            print(f"첫 번째 주사위 = {x}, 두 번째 주사위 = {y}")

# Lab: 모든 조합 출력하기
persons = ["Kim", "Park", "Lee", "Choi"]
restaurants = ["Korean", "American", "French", "Chinese"]

for person in persons:
    for restaurant in restaurants:
        print(f"{person}이 {restaurant} 식당을 방문")

# Lab: 소수 찾기
cnt = 0
num = 2

while cnt < 50:
    prime_num = True
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            prime_num = False
            break
    if prime_num:
        print(num)
        cnt += 1
    num += 1

# Lab: 파이 계산하기
rep = int(input("반복횟수: "))
pi = 0

for i in range(0, rep):
    num = 4 / (2 * i + 1)
    pi += num * (-1) ** i

print(f"Pi = {pi:.6f}")


# Lab: 도박상의 확률
import random

initial_mon = 50
goal_mon = 250
cnt = 0

print("초기 금액 $50")
print("목표 금액 $250")

for rep in range(0, 100):
    this_mon = initial_mon
    while True:
        luck = random.randint(0, 1)
        if luck == 0:
            this_mon -= 1
        else:
            this_mon += 1

        if this_mon == goal_mon:
            cnt += 1
            break
        elif this_mon == 0:
            break

print(f"100번 중에서 {cnt}번 성공")

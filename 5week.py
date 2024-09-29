# 5주차 함수

# Lab: 피자 크기 비교
import math

def get_area(radius):
    area = math.pi * radius**2
    return area


print(f"20cm 피자 2개의 면적 : {2*get_area(20):.1f}")
print(f"30cm 피자 1개의 면적 : {get_area(30):.1f}")


# Lab: 환영 문자열 출력 함수
def display(msg, count):
    for i in range(1, count + 1):
        print(msg)


display("환영합니다.", 5)


# Lab: 환영 문자열 출력 함수 - 도전문제1
def display(count, msg="환영합니다."):
    for i in range(1, count + 1):
        print(msg)


display(5)


# Lab: 환영 문자열 출력 함수 - 도전문제2
def display(count, **kwargs):
    result = ""
    for i in range(count):
        for kwarg in kwargs.values():
            result += kwarg
    return result


print(display(5, msg1="환영합니다.", msg2="123"))


# Lab: 이분법
def func(x):
    ans = x * x - x - 1
    return ans


def ans_root(a, b):
    ans = 0
    cnt = 0
    if func(a) * func(b) > 0:
        print("범위내 근이 없음")

    while True:
        mid = (a + b) / 2
        if func(a) * func(mid) < 0:
            b = mid
        elif func(a) * func(mid) > 0:
            a = mid
        else:
            ans = mid
            return ans

        if cnt < 50:
            cnt += 1
        else:
            break


print(f"x**2-x-1 의 근은 {ans_root(1,3)}")


# Lab: 주급 계산 프로그램
def weeklyPay(rate, hour):
    if hour > 30:
        week_mon = 300000 + rate * (hour - 30) * 1.5
    else:
        week_mon = rate * hour

    return week_mon


x = int(input("시급을 입력하시오: "))
y = int(input("근무 시간을 입력하시오: "))

print(f"주급은 {weeklyPay(x, y)}")


# Lab: 여러 개의 값 반환
def input_name_age():
    name = input("이름: ")
    age = int(input("나이: "))

    return name, age


x, y = input_name_age()

print(f"이름은 {x}이고 나이는 {y}살입니다.")


# Lab: 구조화 프로그래밍 실습
def mode_menu_bar():
    print("1. 섭씨 온도 -> 화씨 온도")
    print("2. 화씨 온도 -> 섭씨 온도")
    print("3. 종료")
    set_mode = int(input("메뉴를 선택하세요: "))

    return set_mode


def change_temp(mode):
    if mode == 1:
        temp = float(input("섭씨 온도를 입력하시오: "))
        ch_temp = temp * 9 / 5 + 32
        print(f"화씨 온도 = {ch_temp}")
    elif mode == 2:
        temp = float(input("화씨 온도를 입력하시오: "))
        ch_temp = (temp - 32) * 5 / 9
        print(f"섭씨 온도 = {ch_temp}")
    else:
        return 0


while True:
    mode = mode_menu_bar()

    if mode == 3:
        break

    change_temp(mode)

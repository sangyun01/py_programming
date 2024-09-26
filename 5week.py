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

print(display(5, msg1="환영합니다.", msg2="123", msg3="456"))


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

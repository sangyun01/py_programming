#3주차 조건문

#Lab: 산술 퀴즈 프로그램1
import random

x = random.randint(1, 100)
y = random.randint(1, 100)

num = int(input(f"{x}+{y} = "))

if x + y == num :
    print("True")
else :
    print("False")

#Lab: 산술퀴즈 프로그램2
num = int(input("정수를 입력하시오: "))

print("짝수입니다."if (num % 2) ==0 else "홀수입니다.")

#Lab: 세일 가격 계산
price = float(input("정가를 입력하시오:(만원) "))

if price < 100 :
    price *= 0.9
    print(f"할인된 가격은 {price}입니다.")
else :
    price *= 0.85
    print("10층에서 사은품을 받아가세요.")
    print(f"할인된 가격은 {price}입니다.")


#Lab: 물의 상태 출력하기
tem = int(input("온도를 입력하시오: "))

if tem > 100 :
    print("물의 상태는 기체입니다.")
elif tem > 0:
    print("물의 상태는 액체입니다.")
else :
    print("물의 상태는 고체입니다.")

#Lab: 동전 던지기 게임
import random

print("동전 던지기 게임을 시작합니다.")
coin = random.randint(0, 1)

if coin == 1 :
    print("앞면입니다.")
else :
    print("뒷면입니다.")

print("게임이 종료되었습니다.")

#Lab: 리히터 규모
scale = float(input("리히터 규모를 입력하시오: "))

if scale > 8.0 :
    print("대부분의 구조물이 파괴됩니다.")
elif scale > 7.0 :
    print("지표면에 균열이 발생합니다.")
elif scale > 4.0 :
    print("빈약한 건물에 큰 피해가 있습니다.")
elif scale > 2.0 :
    print("물건들이 흔들리거나 떨어집니다.")
else :
    print("지진계에 의해서만 탐기 가능합니다.")

#Lab: 사용자 입력 검증하기
print("="*20)
print("메뉴 1번 : 치즈 버거\n메뉴 2번 : 치킨 버거\n메뉴 3번 : 불고기 버거")
print("="*20)
menu = int(input("메뉴를 선택하세요: "))

if menu == 1 :
    print("치즈 버거를 선택하셨습니다.")
elif menu == 2 :
    print("치킨 버거를 선택하셨습니다.")
elif menu == 3 :
    print("불고기 버거를 선택하셨습니다.")
else :
    print("잘못 입력하셨습니다.")

#Lab: 축구게임
import random

defend = random.randint(1, 3)
attack = int(input("어디를 수비하시겠어요?(왼쪽: 1, 중앙: 2, 오른쪽: 3) "))

if defend == attack :
    print("페널티킥에 실패하셨습니다.")
else :
    print("페널티킥이 성공하였습니다.")

#Lab: 올바른 삼각형 구분

a = int(input("삼각형의 한 변을 입력하시오: "))
b = int(input("삼각형의 한 변을 입력하시오: "))
c = int(input("삼각형의 한 변을 입력하시오: "))

if (a + b > c) & (b + c > a) & (c + a > b) :
    print("올바른 삼각형")
else :
    print("올바르지 않음.")
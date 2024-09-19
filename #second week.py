#second week
'''
x = 100
print(x)

y = 200

print(x+y)
print(x-y)
#colab의 경우 여러줄 작성하면 마지막 줄만 출력

score = 10
score = score + 1
#변수 대입은 출력이 X, 그래서 score를 한 번 더 쳐야 나옴/colab 기준

score += 1 #score++는 존재하지 X
#type(score) -> int

print(score)

#원의 면적
import math #pi 변수 라이브러리

r = 2.5
area = math.pi * r * r

#print(area)
#type(area) -> float

print(math.sin(math.pi/2))
print(f"반지름 {r}인 원의 면적 = {area}")

print(id(r)) #변수마다 주소가 다름
'''

#Lab : 별까지의 거리 계산하기
distance = 4e13
speed = 300000

sec = distance / speed
light_year = sec / (3600 * 24 * 365)

print(f"{light_year} 광년")

#Lab : 원기둥의 부피 계산
import math

radius = 5
height = 10
volume = math.pi*radius**2*height

print(f"원기둥의 부피는 {volume}")

#Lab : 복리 계산
price = 24
interest = 0.06
year = 382
current_price = price * (1+interest)**year
print(f"{current_price} dollar")

#Lab : 로봇 기자 만들기
where = input("경기장은 어디입니까? ")
win_team = input("이긴팀은 어디입니까? ")
lose_team = input("진팀은 어디입니까? ")
mvp = input("우수선수는 누구입니까? ")
score = input("스코어는 몇대몇입니까? \n")

print("="*40)
print(f"오늘 {where}에서 야구 경기가 열렸습니다.")
print(f"{win_team}과 {lose_team}은 치열한 공방전을 펼쳤습니다.")
print(f"{mvp}이 맹활약을 하였습니다.")
print(f"결국 {win_team}가 {lose_team}를 {score}로 이겼습니다.")
print("="*40)

#Lab : 대화하는 프로그램 만들기
print("안녕하세요?\n")

name = input("이름이 어떻게 되시나요? ")
print(f"만나서 반갑습니다. {name}씨")
print(f"이름의 길이는 다음과 같군요: {len(name)}\n")
age = int(input("나이가 어떻게 되나요? "))
print(f"내년이면 {age+1}이 되시는군요.")

#Lab : BMI 계산하기
weight = float(input("몸무게를 kg 단위로 입력하시오: "))
height = float(input("키를 미터 단위로 입력하시오: "))

cal_BMI = weight / height**2

print(f"당신의 BMI = {cal_BMI}")


#Lab : 구의 부피 계산하기
import math

radius = float(input("반지름을 입력하시오: "))
sphere_volume = math.pi * (radius**3) * 4 / 3

print(f"구의 부피 = {sphere_volume}")

#Lab : 자동판매기 프로그램

price = int(input("물건값을 입력하시오: "))

print(f"1000원의지폐개수: {price // 1000}")
print(f"500원의 동전개수: {(price % 1000) // 500}")
print(f"100원의 동전개수: {((price % 1000) % 500) // 100}")
print(f"10원의 동전개수: {(price % 100) // 10}")
print(f"1원의 동전개수: {(price % 10)}")

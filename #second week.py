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
'''

#원의 면적
import math #pi 변수 라이브러리

r = 2.5
area = math.pi * r * r

#print(area)
#type(area) -> float

print(math.sin(math.pi/2))
print(f"반지름 {r}인 원의 면적 = {area}")

print(id(r)) #변수마다 주소가 다름


# 6주차 리스트

# Lab: 성적 처리 프로그램
numbers = []
count = 0

for i in range(5):
    numbers.append(int(input("성적을 입력하시오: ")))

print(f"평균 성적: {sum(numbers) / len(numbers)}")
print(f"최고 성적: {max(numbers)}")
print(f"최저 성적: {min(numbers)}")


for number in numbers:
    if number >= 80:
        count += 1

print(f"80점 이상 = {count}")


# Lab: 리스트에서 2번째로 큰 수 찾기
lst = [-7, 2, 3, 8, 6, 6, 75, 38, 3, 2]

lst.sort()
print(lst[-2])

# Lab: 콘테스트 평가
scores = [10.0, 9.0, 8.3, 7.1, 3.0, 9.0]

scores.remove(max(scores))
scores.remove(min(scores))
print(scores)

# Lab: 리스트로 스택 흉내내기
fruits = []

def push_fruit(fruit):
    fruits.append(fruit)

for i in range(3):
    fruit = input("과일을 입력하시오: ")
    push_fruit(fruit)

for fruit in reversed(fruits):
    print(fruit)

# Lab: 친구 관리 프로그램
friendslist = []

def menubar_friend():
    print("-" * 20)
    print("1. 친구 리스트 출력")
    print("2. 친구 추가")
    print("3. 친구 삭제")
    print("4. 이름 변경")
    print("9. 종료")

while True:
    menubar_friend()

    menu_num = int(input("메뉴를 선택하시오: "))

    if menu_num == 1:
        print(friendslist)
    elif menu_num == 2:
        name = input("이름을 입력하시오: ")
        friendslist.append(name)
    elif menu_num == 3:
        name = input("이름을 입력하시오: ")
        if name in friendslist:
            friendslist.remove(name)
        else:
            print(f"{name}은 목록에 없습니다.")
    elif menu_num == 4:
        ex_name = input("변경 대상의 이름을 입력하시오: ")
        if ex_name in friendslist:
            new_name = input("변경할 이름을 입력하시오: ")
            name_index = friendslist.index(name)
            friendslist[name_index] = new_name
        else:
            print(f"{name}은 목록에 없습니다.")
    elif menu_num == 9:
        break
    else:
        print("잘못입력하셨습니다.")

# Lab: 리스트 슬라이싱
numbers = []

for i in range(1, 11):
    numbers.append(i)

print(numbers[9:0:-2])
print(numbers[0:1])

# Lab: 리스트 변경 함수
month_money = [200, 250, 300, 280, 500]
print(f"인상전{month_money}")


def modify(money):
    for i in range(len(month_money)):
        money[i] *= 1.3

    return money

month_money = modify(month_money)
print(f"인상후{month_money}")

# Lab: 리스트 함축 사용하기
num_6 = [i for i in range(100) if (i % 2 == 0) and (i % 3 == 0)]
print(num_6)

# Lab: 리스트 함축 사용하기 - 도전문제
num_odd = ["짝수" if i % 2 == 0 else "홀수" for i in range(10)]
print(num_odd)

# Lab: 누적값 리스트 만들기
lst = [10, 20, 30, 40, 50]

#lst_new = [sum(lst[: i + 1]) for i in range(len(lst))]
#print(f"새로운 리스트 : {lst_new}")

lst_new = []
num = 0
for i in range(len(lst)):
    num = num + lst[i]
    lst_new.append(num)

print(f"원래 리스트 :{lst}")
print(f"새로운 리스트 : {lst_new}")

# Lab: 피타고라스 삼각형
tri = [(x,y,z) for x in range(1,31) for y in range(x,31) for z in range(y,31) if x**2 + y**2 == z**2]
print(tri)

# Lab: 전치 행렬 계산
mat = [i for i in range(1, 10)]  # 1~9의 row vector 1개 생성

matrix = [mat[j : j + 3] for j in range(0, 9, 3)]  # mat[0]->1 mat[3]->4 mat[6]->7
print(matrix)

matrix_t = [[row[i] for row in matrix] for i in range(3)]
# matrix의 행마다 순차적으로 147(i=0)/258(i=1)/369(i=2)를 뽑아내서 출력
print(matrix_t)

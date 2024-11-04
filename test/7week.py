# 7주차 튜플

# 수업시간 끄적끄적
gen = (x * x for x in range(5))
"""
print(gen)

x = tuple(gen)
print(x)
y = list(gen)
print(y)
z=list(x)
print(z)

# Lab: 문자열의 공통 문자

x = input("첫 번쨰 문자열: ")
y = input("두 번째 문자열: ")

print(f"{set(x)&set(y)}")

# Lab: 문자열의 공통 문자
s = set(input("입력 텍스트: ").split())

print(f"사용된 단어의 개수 = {len(s)}")
print(s)

# Lab: 영한 사전
en_kr_dict = {"one": "하나", "two": "둘", "three": "셋"}

en_word = input("단어를 입력하시오: ")
print(en_kr_dict[en_word])
"""
# Lab: 연락처 처리
contacts = dict()

def print_menu():
    print("1. 연락처 추가")
    print("2. 연락처 삭제")
    print("3. 연락처 검색")
    print("4. 연락처 출력")
    print("5. 종료")

while True:
    print_menu()

    menu = int(input("메뉴 항목을 선택하세요: "))
    if menu == 1:
        input_key_name = input("이름: ")
        val_phone = input("전화번호: ")

        contacts[input_key_name] = val_phone
    elif menu == 2:
        del_key_name = input("이름: ")

        contacts.pop(del_key_name)
    elif menu == 3:
        find_key_name = input("이름: ")

        if find_key_name in contacts:
            print(f"{find_key_name}의 전화번호 : {contacts[find_key_name]}")
        else:
            print("해당 연락처가 없습니다.")
    elif menu == 4:

        for key_name in contacts:
            print(f"{key_name}의 전화번호 : {contacts[key_name]}")
        else:
            print("해당 연락처가 없습니다.")
    elif menu == 5:
        break
    else:
        print("잘못입력하셨습니다.")

# Lab: 학생 성적 처리
score_dic = {
    "Kim":[99,83,95],
    "Lee":[68,45,78],
    "Choi":[25,56,69]
}

for k, v in score_dic.items(): # k -> 학생이름, v-> 성적
    print(f"{k}의 평균성적 = {sum(v)/len(v)}")

# Lab: 단어 카운터 만들기
text_data = "Create the highest, grandest vision possible for your life, because you become what you believe"
text_count = dict()  # 공백 dict


for word in text_data.split():
    word =  word.strip(",")
    if word in text_count:
        text_count[word] += 1
    else:
        text_count[word] = 1

    # text_count[word] = text_count.get(word, 0) + 1 -> 요것도 가능
    # 가져왔을 때 처음에는 0으로 가져와서 1 더하고, 이후는 이전에 저장된 값에 +1을 하기

for k, v in text_count.items():
    print(f"{k}의 등장횟수 = {v}")

# Lab: 회문 검사하기
palindrome = input("문자열을 입력하세요: ")

if palindrome == palindrome[::-1]:
    print("회문입니다.")
else:
    print("회문이 아닙니다.")

# Lab: 머리 글자어 만들기
acronym = input("문자열을 입력하시오: ")
word_CAP = acronym.split()
s = ""

for i in word_CAP:
    s += i[0]

print(s)

# Lab: 이메일 주소 분석
e_mail =  input("이메일 주소를 입력하시오: ")

id_domain = e_mail.split("@")
print(e_mail)

print(f"아이디: {id_domain[0]}")
print(f"도메인: {id_domain[1]}")

# Lab: 문자열 분석
cal = {"digits": 0, "spaces": 0, "alphas": 0}

analysis_str = input("문자열을 입력하시오: ")

for i in analysis_str:
    if i.isdigit():
        cal["digits"] += 1
    elif i.isspace():
        cal["spaces"] += 1
    elif i.isalpha():
        cal["alphas"] += 1

for k, v in cal.items():
    print(f"{k}의 개수 : {v}")





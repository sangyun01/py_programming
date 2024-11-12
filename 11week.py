# 11주차 내장 함수

"""
# Lab : 내장 함수 예제
invitations = ["Kim", "Lee", "Park", "Choi"]
persons = [1, 3, 0, 6]
print(sum(persons))

if any(persons):
    print("파티에 한 사람이라도 옵니다")
else:
    print("파티에 아무도 안옵니다.")

if all(persons):
    print("모든 초대받은 그룹이 전부 옵니다.")
else:
    print("모든 그룹이 오지는 않습니다.")

print(f"{max(persons)}")
"""

# Lab : 키를 이용한 정렬 예제
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<이름 : {self.name}, 나이 : {self.age}>"

people = [Person("홍길동", 20), Person("최자영", 38), Person("김철수", 35)]


def keyage(person):
    return person.age
"""
def keyname(person):
    return person.name

print(sorted(people, key=keyname)) #정렬기준이 key=keyname(이름순)
"""
print(sorted(people, key=keyage)) #정렬기준이 keyage

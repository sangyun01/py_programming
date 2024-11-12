# 11주차 내장 함수

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

# Lab : 키를 이용한 정렬 예제

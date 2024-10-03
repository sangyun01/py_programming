#6주차 리스트

#Lab: 성적 처리 프로그램

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
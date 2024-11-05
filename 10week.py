# 10주차 파일과 예외처리
"""
# Lab: 매출 파일 처리

infile = open(
    "C:\\Users\\SamSung\\OneDrive\\바탕 화면\\대학교\\제10장 파일과 예외처리(2024) - data\\sales.txt",
    "r",
)
lines = infile.readlines()

sum = 0
a = len(lines)

for line in lines:
    sum += int(line)

with open(
    "C://Users//SamSung//OneDrive//바탕 화면//대학교//제10장 파일과 예외처리(2024) - data//summary.txt",
    "w",
) as outfile:
    outfile.write(f"총 매출 = {sum}\n")
    outfile.write(f"평균 일매출 = {sum/a}\n")

# Lab: 각 문자 횟수 세기

name = "C://Users//SamSung//OneDrive//바탕 화면//대학교//제10장 파일과 예외처리(2024) - data//test.txt"
infile = open(name , "r")

cnt = {} #딕셔너리 형태

for line in infile:
    for alpha in line.strip():
        if alpha in cnt:
            cnt[alpha] += 1
        else:
            cnt[alpha] = 1
print(cnt)


# Lab: CVS 파일 처리
import csv

f = open(
    "C://Users//SamSung//OneDrive//바탕 화면//대학교//제10장 파일과 예외처리(2024) - data//weather.csv"
)
data = csv.reader(f)
header = next(data)

low_temp = 0

for row in data:
    if low_temp > float(row[3]):  # 최저기온 확인
        low_temp = float(row[3])

print(f"가장 추웠던 날의 기온은 {low_temp}ºC입니다.")
"""

# Lab : 디렉토리 안의 파일 처리 - 수정 중
import os

files = os.listdir()

for name in files:
    if os.path.isfile(name):  # 파일인지 확인하여 디렉토리 건너뛰기
        try:
            with open(name, "r", encoding="utf-8") as infile:  # with 구문으로 파일 열기
                for line in infile:
                    if "Python" in line:
                        print(f"{name}: {line.strip()}")
                        
        except PermissionError:
            print(f"Permission denied for file: {name}")
        except UnicodeDecodeError:
            print(f"Cannot decode file: {name}")



"""

#Lab : 이미지 파일 복사하기
infile = open("C://Users//SamSung//OneDrive//바탕 화면//대학교//제10장 파일과 예외처리(2024) - data//123.png", "rb")
outfile = open("C://Users//SamSung//OneDrive//바탕 화면//대학교//제10장 파일과 예외처리(2024) - data//copy_file.png", "wb")

data = infile.read()
outfile = outfile.write(data)

#Lab: 정규식 이용하기
infile = open("C://Users//SamSung//OneDrive//바탕 화면//대학교//제10장 파일과 예외처리(2024) - data//number.txt", "r")

course_name = []

for line in infile:
    text_content = line.split()
    course_name.append(text_content[0])

print(course_name)

# Lab: 패스워드 검사 프로그램

import re

pw = input("패스워드를 입력하시오 : ")
decidepw = False

while True:
    if len(pw) < 8:
        break
    elif not re.search("[a-z]", pw):
        break
    elif not re.search("[A-Z]", pw):
        break
    elif not re.search("[0-9]", pw):
        break
    elif not re.search("[_@$]", pw):
        break
    else:
        decidepw = True
        break

if decidepw == True:
    print("올바른 PW")
else:
    print("PW 재설정")
"""
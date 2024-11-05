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

# Lab : 디렉토리 안의 파일 처리
import os

cwd = os.getcwd()
files = os.listdir()

for name in files:
    infile = open(name)
    for line in infile.readlines():
        if line.find("Python") != -1:
            print(f"{name}:{line}")
"""
#Lab : 이미지 파일 복사하기
infile = open("C://Users//SamSung//OneDrive//바탕 화면//대학교//제10장 파일과 예외처리(2024) - data//123.png", "rb")
outfile = open("C://Users//SamSung//OneDrive//바탕 화면//대학교//제10장 파일과 예외처리(2024) - data//copy_file.png", "wb")

data = infile.read()
outfile = outfile.write(data)
"""
"""
#Lab: 정규식 이용하기
infile = open("C://Users//SamSung//OneDrive//바탕 화면//대학교//제10장 파일과 예외처리(2024) - data//number.txt")

"""
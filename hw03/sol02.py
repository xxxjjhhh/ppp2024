# 키와 몸무게가 임의로 주어졌을 때 BMI를 구하시오
# BMI = 몸무게 (kg) / 키 (m)^2
# 입력 : 콘솔

import math

weight = int(input("몸무게를 입력하세요.(kg) : "))
height = int(input("키를 입력하세요.(cm) : "))

mHeight = 170/100

bmi = weight / math.pow(mHeight, 2)
print(f"몸무게 : {weight}kg, 키 : {height}cm의 BMI는 {bmi}입니다.")

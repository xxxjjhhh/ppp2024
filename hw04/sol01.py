# 과제#04 1번
#
# 과제#03의 BMI 계산결과에 따라 아래 텍스트를 참고하여, 비만 정도를 표시하시오.
# “2020년 비만 진료지침에서는 체질량지수(BMI) △23~24.9kg/m²를 비만 전단계 △25~29.9kg/m²를 1단계 비만 △30~34.9kg/m²를 2단계 비만 △35kg/m² 이상을 3단 계 비만으로 정의했다.”

import math

#input
weight = int(input("몸무게를 입력하세요.(kg) : "))
height = int(input("키를 입력하세요.(cm) : "))

#cm -> m
m_height = 170/100

bmi = weight / math.pow(m_height, 2)
print(f"몸무게 : {weight}kg, 키 : {height}cm의 BMI는 {bmi}입니다.")

#비만 알림
if (23 <= bmi) and (bmi < 25): 
    print("비만 전단계입니다.")

elif (25 <= bmi) and (bmi < 30):
    print("1단계 비만입니다.")

elif (30 <= bmi) and (bmi < 35):
    print("2단계 비만입니다.")

elif 35 <= bmi:
    print("3단계 비만입니다.")

else:
    ...

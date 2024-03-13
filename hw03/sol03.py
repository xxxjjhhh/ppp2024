# 반지름이 주어졌을 때, 원의 면적을 구하시오.
# 입력 : 콘솔

import math

#input
radius = int(input("반지름을 입력하세요. : "))

area = radius * radius * math.pi
print(f"반지름이 {radius}일 때, 원의 넓이는 {area}입니다.")

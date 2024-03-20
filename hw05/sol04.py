# 과제 #05 4번
#
# 삼각함수 표를 만드시오.

import math

print("각 | 라디안 | sin | cos | tan")
print("-" * 30)

for angle in range(0, 91, 1):

    radian = math.radians(angle)
    sin_value = math.sin(radian)
    cos_value = math.cos(radian)
    tan_value = math.tan(radian)

    print(f"{angle}° | {radian:.2f} | {sin_value:.2f} | {cos_value:.2f} | {tan_value:.2f}")

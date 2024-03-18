# 과제#04 4번
#
# 과제#03에서 반지름을 입력받아서, 원의 둘레와 원의 면적을 출력하는 프로그램을 작성하시오.
# 단 둘레는 소수점 1자리까지, 원의 면적은 소수점 2번째 자리까지 표시하시오. round 함수를 쓸 수 있겠으나, 출력시 포맷 기능을 활용하는 것을 권장함.

import math

#input
radius = int(input("반지름을 입력하세요. : "))

#원둘레
circumference = 2 * radius * math.pi
#원넓이
area = radius * radius * math.pi

print(f"반지름이 {radius}일 때, 원의 둘레는 {circumference:.1f}입니다.")
print(f"반지름이 {radius}일 때, 원의 넓이는 {area:.2f}입니다.")

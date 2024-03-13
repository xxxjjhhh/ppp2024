# 두 지점 사이 거리 구하기
# x1, y1, x2, y2를 각각 입력 받아서 두 지점의 거리를 출력하기

import math

#input
x1 = int(input("x1의 값을 입력하세요. : "))
y1 = int(input("y1의 값을 입력하세요. : "))
x2 = int(input("x2의 값을 입력하세요. : "))
y2 = int(input("y2의 값을 입력하세요. : "))

#find x and y diff
diff_x = x2 - x1
diff_y = y2 - y1

#square
square_diff_x = math.pow(diff_x, 2)
square_diff_y = math.pow(diff_y, 2)

#find c (c^2 = x^2 + y^2)
distance = math.sqrt(square_diff_x + square_diff_y)

print(f"두 점 사이의 거리는 {distance}입니다.")

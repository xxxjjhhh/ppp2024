import math

x1 = 0
y1 = 0
x2 = 1
y2 = 1

dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(dist)
if dist <= 1:
  print("두 점이 너무 가깝습니다.")

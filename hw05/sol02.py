# 과제 #05 2번
#
# 삼각형 별 그리기

height = int(input("출력할 삼각형 별 높이를 입력하세요. : "))

for i in range(height):
    print("*" * (i + 1))

print("")

for i in range(height):
    print(" " * (height - i - 1) + "*" * (i + 1))

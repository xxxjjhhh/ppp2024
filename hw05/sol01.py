# 과제 #05 1번
#
# 숫자를 입력받아, 입력받은 숫자의 구구단을 출력하시오.

input_value = int(input("출력할 구구단 단수를 입력하세요. : "))

for i in range(1, 11, 1):
    print(f"{input_value} X {i} = {input_value * i}")

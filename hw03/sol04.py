# 윗변, 밑변, 높이가 임의로 주어졌을 때 사다리꼴의 면적을 구하시오.
# 입력 : 콘솔

top = int(input("윗변을 입력하세요. : "))
bottom = int(input("밑변을 입력하세요. : "))
height = int(input("높이를 입력하세요. : "))

area = (top + bottom) * height / 2
print(f"사다리꼴의 면적은 {area}입니다.")

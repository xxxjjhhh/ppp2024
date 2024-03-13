# 칼로리 구하기 (과일마다 섭취 g를 입력받아서 칼로리 출력하기)
# 한라봉 50kcal/100g
# 딸기(설향) 34kcal/100g
# 바나나 77kcal/100g

fruit_hala = int(input("섭취한 한라봉의 양을 입력하세요. (g) : "))
fruit_strawberry = int(input("섭취한 딸기(설향)의 양을 입력하세요. (g) : "))
fruit_banana = int(input("섭취한 바나나의 양을 입력하세요. (g) : "))

total_kcal = fruit_hala*50/100 + fruit_strawberry*34/100 + fruit_banana*77/100

print(f"섭취한 양에 대한 총 칼로리는 {total_kcal}kcal 입니다.")

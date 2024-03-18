# 과제#04 3번
#
# 과제#03에서 칼로리 계산 프로그램을 사전형(딕셔너리)를 이용하여 구현하시오.

#input
fruit_hala = int(input("섭취한 한라봉의 양을 입력하세요. (g) : "))
fruit_strawberry = int(input("섭취한 딸기(설향)의 양을 입력하세요. (g) : "))
fruit_banana = int(input("섭취한 바나나의 양을 입력하세요. (g) : "))

# data {"furit" : "kcal"}
calories = {"한라봉": 50, "딸기(설향)": 34, "바나나": 77}

#total
total_kcal = (fruit_hala*calories["한라봉"] + fruit_strawberry*calories["딸기(설향)"] + fruit_banana*calories["바나나"])/100

print(f"섭취한 양에 대한 총 칼로리는 {total_kcal}kcal 입니다.")

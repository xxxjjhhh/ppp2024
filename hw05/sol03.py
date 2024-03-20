# 과제 #05 3번
#
# 칼로리 계산 프로그램(과제#04-03)를 수정하여, 총 칼로리를 계산하시오. (반복문, 사전 활용)

#data {"furit" : "kcal"}
calories = {"한라봉": 50, "딸기(설향)": 34, "바나나": 77}

#섭취한 과일
fruit_eat = ["한라봉", "한라봉", "바나나", "한라봉", "딸기(설향)", "딸기(설향)", "바나나"]

#total
total_kcal = 0
for i in fruit_eat:

    total_kcal = total_kcal + calories[i]

print(f"섭취한 과일에 대한 총 칼로리는 {total_kcal}kcal 입니다.")

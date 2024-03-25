# 과제 #06 문제1
#
# 칼로리 계산 프로그램(과제#04-03)를 수정하여, 총 칼로리를 계산하시오. (반복문, 사전 활용)


def kcal_calculate():

    #data
    # 먹은 과일 data {"fruit" : 0}
    eat_fruit = {"한라봉" : 0, "딸기(설향)" : 0, "바나나" : 0}
    # 과일 100g kcal data {"furit" : kcal}
    calories = {"한라봉": 0.5, "딸기(설향)": 0.34, "바나나": 0.77}

    #input
    for fruit in eat_fruit:
        eat_fruit[fruit] = int(input(f"섭취한 {fruit}의 양을 입력하세요. (g) : "))

    # #total
    total_kcal = 0
    for fruit in eat_fruit:
        total_kcal = total_kcal + eat_fruit[fruit] * calories[fruit]


    print(f"섭취한 양에 대한 총 칼로리는 {total_kcal}kcal 입니다.")

def main():

    #칼로리 계산
    kcal_calculate()

if __name__ == "__main__":
    main()

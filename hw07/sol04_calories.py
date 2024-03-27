# 과제 #07 4번
#
# 딸기 300g, 한라봉 150g 섭취하였을 때, 입력자료를 사전형으로 전달하면, 총 칼 로리를 계산하는 함수를 만드시오.
# fruits={“딸기”: 300, “한라봉”: 150}, fruits_calorie_dic={"한라봉": 50, "딸기": 34, "바나나": 77}.
# 과제 #06-01 활용. 함 수명은 total_calorie(fruits, fruits_calorie_dic)

def total_calorie(fruits: dict, fruits_calorie_dic: dict) -> float:

    #total
    total_kcal = 0
    for fruit in fruits:
        total_kcal = total_kcal + fruits[fruit] * fruits_calorie_dic[fruit] / 100

    return total_kcal

def main() -> None:

    #data
    # 먹은 과일 data {"fruit" : 0}
    fruits = {"딸기" : 300, "한라봉" : 150}
    # 과일 100g kcal data {"furit" : kcal}
    fruits_calorie_dic = {"한라봉" : 50, "딸기" : 34, "바나나" : 77}

    #칼로리 계산
    total_kcal = total_calorie(fruits, fruits_calorie_dic)
    print(f"섭취한 양에 대한 총 칼로리는 {total_kcal}kcal 입니다.")

if __name__ == "__main__":
    main()

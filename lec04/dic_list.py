eat_fruits = ["딸기(설향)", "시과"]
eat_grams = [50, 120]


cal = {"한라봉": 0.5, "딸기(설향)": 0.34, "바나나": 0.77}

total_cal = 0
idx = 0
for eat_fruit in eat_fruits:
    for fruit in cal:
        if eat_fruit == fruit:
            total_cal = cal[fruit] * eat_gram[idx]
        idx = idx + 1

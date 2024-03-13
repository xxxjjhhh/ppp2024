# 섭씨를 화씨로 변환하는 프로그램을 작성하라.
# 입력 : 콘솔

c_temp = int(input("섭씨 온도를 입력하세요.(°C) : "))
f_temp = ((c_temp * 9/5) + 32)

print("섭씨 {}°C는 화씨 {}°F 입니다.".format(c_temp, f_temp))

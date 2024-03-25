# 과제 #06 문제3
#
# 섭씨를 화씨로 바꾸는 함수 c2f(t_c) 함수를 만드시오.

def c2f(t_c):

    t_f = ((t_c * 9/5) + 32)

    print(f"섭씨 {t_c}°C는 화씨 {t_f}°F 입니다.")

def main():

    #input
    t_c = int(input("섭씨 온도를 입력하세요.(°C) : "))

    #섭씨 -> 화씨 변환
    c2f(t_c)

if __name__ == "__main__":
    main()

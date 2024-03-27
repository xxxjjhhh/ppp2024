# 과제 #07 3번
#
# 연도(y)를 주면, 윤년인지(True) 아닌지를(False) 알려주는 is_leap_year(y) 함수를 만드시오. 
# 단 윤년의 조건은 주어진 조건으로 구현하시오. 4로 나누었을 때 나누어 떨 어지면 윤년. 4로 나누어떨어지더라도, 100으로 나누어 떨어진다면, 윤년 아님.

def is_leap_year(y: int) -> bool:

    if (y%4 == 0) and (y%100 != 0):
        return True
    else:
        return False

def main() -> None:
    
    year = int(input("연도를 입력하세요. : "))

    #윤년 계산
    isLeap = is_leap_year(year)

    #결과
    if isLeap:
        print("윤년입니다.")
    else:
        print("윤년이 아닙니다.")

if __name__ == "__main__":
    main()

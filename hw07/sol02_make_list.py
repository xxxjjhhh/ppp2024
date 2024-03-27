# 과제 #07 2번
#
# 1-n까지 리스트를 돌려주는 함수를 만드시오. 함수는 get_range_list(n)

def get_range_list(n: int) -> list:

    return list(range(1, n + 1, 1))

def main() -> None:
    
    #입력
    number = int(input("1부터 n까지 값을 포함하는 리스트를 만들 때 n값 입력 : "))

    #리스트 만들기
    result = get_range_list(number)

    #리스트 출력
    print(result)

if __name__ == "__main__":
    main()

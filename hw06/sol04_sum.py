# 과제 #06 4번
# 
# 숫자 n이 주어졌을 때, 1부터 n까지의 합을 구하시오. 함수명은 sum_n(n)

def sum_n(n):

    sum = n * (n+1) / 2

    print(f"1부터 {n}까지 합은 {sum}입니다.")

def main():

    #input
    n = int(input("1부터 n까지 합할 n을 입력하세요. : "))

    #1부터 n까지 합
    sum_n(n)

if __name__ == "__main__":
    main()

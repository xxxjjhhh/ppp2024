# 과제 #06 2번
#
# 숫자를 입력받아, 해당하는 구구단을 출력하는 함수 gugudan(dan)를 만드시오.

def gugudan(dan):

    for i in range(1, 11, 1):
        print(f"{dan} X {i} = {dan * i}")

def main():

    #input
    dan = int(input("출력할 구구단 단수를 입력하세요. : "))

    #구구단 출력
    gugudan(dan)

if __name__ == "__main__":
    main()

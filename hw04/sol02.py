# 과제#04 2번
#
# 과제#03를 수정하여, x, y를 입력받아서, 어느 사분면인지 출력하시오. ex) x=1, y=2 => “입력한 좌표는 1사분면입니다.”

#input
x = int(input("x의 값을 입력하세요. : "))
y = int(input("y의 값을 입력하세요. : "))

#판별 (if : 4분면 아닐 경우,  else : 4분면 판별)
if (x == 0) or (y == 0):
    if (x == 0) and (y == 0):
        print("원점에 위치합니다.")
    elif x == 0:
        print("y축에 위치합니다.")
    else:
        print("x축에 위치합니다.")

else:
    if x > 0:
        if y > 0:
            print("1사분면에 위치합니다.")
        else:
            print("4사분면에 위치합니다.")
    else:
        if y > 0:
            print("2사분면에 위치합니다.")
        else:
            print("3사분면에 위치합니다.")

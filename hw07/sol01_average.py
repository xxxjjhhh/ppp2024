# 과제 #07 1번
#
# 숫자 리스트를 매개변수로 받아서 평균을 구하시오. 함수는 average(nums)

def average(nums: list) -> float:

    if len(nums) == 0:
        return None
    
    sum = 0
    for num in nums:

        sum = sum + num

    return sum/len(nums)

def main() -> None:
    
    data = [0]

    # 합계 메소드
    avg = average(data)
    if avg != None:
        print(f"리스트에 담긴 수의 평균은 {avg}입니다.")
    else:
        print(f"리스트에 값을 담아 주세요.")

if __name__ == "__main__":
    main()

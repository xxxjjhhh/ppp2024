def largest(*args):

    temp = args[0]
    for i in args:
        if i > temp:
            temp = i

    return temp

def main():
    x1 = 5
    x2 = 7
    x3 = 3

    largest_num = largest(x1, x2, x3)

    print(f"가장 큰 수는 {largest_num}입니다.")

if __name__ == "__main__":
    main()

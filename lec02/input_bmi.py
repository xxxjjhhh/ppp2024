weight = int(input("몸무게를 입력하세요.(kg) "))
height = int(input("키를 입력하세요.(cm) "))

mHeight = 170/100

bmi = weight / (mHeight*mHeight)
print(bmi)

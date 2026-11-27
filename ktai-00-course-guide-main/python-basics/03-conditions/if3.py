#4개의 숫자를 입력
#4개의 숫자 평균을 구한다
#평균이 90점 이상이면 "A학점입니다."를 출력하고
#평균이 80점 이상이면 "B학점입니다."를 출력하고
#평균이 70점 이상이면 "C학점입니다."를 출력하고
#평균이 60점 이상이면 "D학점입니다."를 출력하고
#그외는 "F학점입니다."를 출력한다.    

num1 = float(input("첫 번째 수를 입력하세요: "))
num2 = float(input("두 번째 수를 입력하세요: "))       
num3 = float(input("세 번째 수를 입력하세요: "))
num4 = float(input("네 번째 수를 입력하세요: "))
sum = num1 + num2 + num3 + num4
average = sum / 4

if average >= 90:
    print("A학점입니다.")
elif average >= 80:
    print("B학점입니다.")
elif average >= 70:
    print("C학점입니다.")
elif average >= 60:
    print("D학점입니다.")
else:
    print("F학점입니다.")

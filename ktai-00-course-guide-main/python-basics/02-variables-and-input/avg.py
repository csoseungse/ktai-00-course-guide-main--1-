#4개의숫자를 입력받아
#평균과 합계를 계산
#출력결과는 평균10.3 합계는 41.2  출력

num1=input("Enter the first number: ")  
num2=input("Enter the second number: ")     
num3=input("Enter the third number: ")     
num4=input("Enter the fourth number: ")     

sum=float(num1)+float(num2)+float(num3)+float(num4)
average=sum/4

print(f"결과는{average} , 합계는 {sum}")
num1=int(input("정수입력>"))

if num1==0:
    print("오류입니다.")
    exit()
if num1==1:
    print("캐쉬카드입니다.")
elif num1==2:
    print("신용카드입니다.")
elif num1==3:
    print("다른은행카드입니다.")
else:
    print("카드가 아닙니다.")




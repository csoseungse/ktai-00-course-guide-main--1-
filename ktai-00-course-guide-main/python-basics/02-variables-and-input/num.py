num_1=100
num2=200
num3=300
# 정수, 실수, 문자
result = num_1 + num2 + num3
print(result)
print(num_1, num2, num3)
print("합계:", result)
print(f"숫자1: {num_1}, 숫자2: {num2}, 숫자3: {num3}") #f string
# (소) {중} [대]
s1=10
s2=3
result2=s1/s2
print(f"나눗셈 결과: {result2}")
print(type(s1))
print(type(result2)) # float

first_string="10.5"
second_string="20.5"
result3=float(first_string)+float(second_string)
print(f"문자열 더하기 결과: {result3}")
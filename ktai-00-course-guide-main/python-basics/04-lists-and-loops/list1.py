#변수집합
#list

num1=10
num2=19.2
str="안녕하세요"


num_list = [1, 2, 3, 4, 5]

print(type(num1))
print(type(num2))
print(type(str))
print(type(num_list))

print(num_list[3]) #0부터 시작 3번째
print(len(num_list))#length
print(num_list[-3])#거꾸로 3번째
print(num_list[1:4])#1부터 4까지

print(num_list[1:4])#1부터 4까지
print(num_list[1:])#1부터 끝까지

print(num_list[:4])#처음부터 4까지

print(sorted(num_list))#정렬

num2_list = [ 1, 3, 4, 5, 6, 7, 8, 9]
print(num2_list)
print(sorted(num2_list))#정렬
#내림차순정렬


#가장큰수를 출력
print(max(num2_list))
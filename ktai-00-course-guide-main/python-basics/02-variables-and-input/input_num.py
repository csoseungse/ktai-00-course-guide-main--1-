print("start1")
num1=100
print("start2")
num2= input("Enter an interger or decimal number: ")
print("start3")
if num2.isnumeric():
    num2- float(num2)   
    result=num1 + num2
print("start4")
print("The result is:", result)
else:
    print("Invalid input. Please enter a valid number.")
print("end")
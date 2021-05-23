# Faulty Calculator

print("Enter the first number")
num1 = int(input())
print("Enter the second number")
num2 = int(input())
print("The operator is, +, -, /, *")
num3 = input()
if num1==45 and num2==3 and num3=="*":
    print(555)
elif num1==56 and num2==9 and num3=="+":
    print(77)
elif num1==56 and num2==6 and num3=="/":
    print(4)
elif num3 == "+":
    num4=num1+num2
    print(num4)
elif num3 == "-":
    minus=num2-num1
    print(minus)
elif num3 == "/":
    div=num1/num2
    print(div)
elif num3 == "*":
    star=num1*num2
    print(star)
else:
    print("Unexpected Error, Please check your input")
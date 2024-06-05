num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))

if num1 > num2 and num1 > num3:
    print("first number is greater than others number that is", num1)
elif num2 > num1 and num2 > num3:
    print("second number is greater than others number that is", num2)
else:
    print("third is greater than others number that is", num3)

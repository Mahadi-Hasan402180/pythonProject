def sumArray(arry, size):
    sum = 0
    for m in range(size):
        sum = sum + arry[m]
    return sum

SIZE = 5
num = []
print(f"Please Enter {SIZE} numbers : ")
for x in range(SIZE):
    x = int(input())
    num.append(x)
sum = sumArray(num, SIZE)
print(f"Sum of five numbers is :  {sum}")







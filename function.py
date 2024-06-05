def large(a, b):
    if a > b:
        return a
    else:
        return b
# print(large(20, 90))
def add(a, b):
    sum = a + b
    return sum
result = add(14, 48)
# print(result)

# xargx - work for tupels
def student(*details):
    print(details)
student(101, 'mahadi', 200000)

# xxargx work for dictionary
def student(**details):
    print(details)
student(id = 100 , name = "mahadi", age = 18)

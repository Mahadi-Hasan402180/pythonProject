'''

# file read process
file = open("student.txt", 'r')
text = file.read()
print(text)

# file write process
f = open("student.txt", 'a')
f.write("\n i love bangladesh")
file.close()

'''

# swapping 2 number
a = 10
b = 20
a, b = b, a
print("a = ", a)
print("b = ", b)


# map er modde thakbe ekta function and list
# map(function, list)
def square(x):
    return x*x
number = [2, 6, 5, 8, 9]

y = [x*x for x in number]   # comprehensive
result = list(map(square, number))
print(result)
print(y)

# filter itarable object return kore tai list er moddhe rakhte hoi.
# filter function jodi er condition na mane tahole list take remove kore dei
z = [x for x in number if x % 2 == 0]   # comprehensive
output = list(filter(lambda x: x % 2 == 0, number))
print(output)
print(z)


# even number uses comprehensive
n = [4, 9, 8, 5, 16, 88, 23]
print("the even number is: ", [x for x in n if x % 2 == 0])



# zip function
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
str = ["mahadi", "hasan", "forhad", "fazleRabbi", "jalal", "laltu"]
out = list(zip(l, str, "abcdabcd"))
print(out)

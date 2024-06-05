# map er modde thakbe ekta function and list
# map(function, list)
def square(x):
    return x*x
number = [2, 3, 5, 8, 9]
result = list(map(square, number))
print(result)

# filter itarable object return kore tai list er moddhe rakhte hoi.
# filter function jodi er condition na mane tahole list take remove kore dei

output = list(filter(lambda x: x % 2 == 0, number))
print(output)

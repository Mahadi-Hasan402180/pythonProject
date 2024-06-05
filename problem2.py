number_of_words = 0
number_of_letters = 0
numbers_of_digits = 0
text = input("Enter a string: ")
for n in text:
    n = n.lower()
    if n >= "a" and n <= "z":
        number_of_letters += 1
    elif n >= '0' and n <= '9':
        numbers_of_digits += 1
    elif n == ' ':
        number_of_words += 1
print(number_of_letters)
print(numbers_of_digits)
print(number_of_words +1)

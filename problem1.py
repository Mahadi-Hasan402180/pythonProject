# Reverse each word of a string:

str1 = input("Enter the sentence: ")
words = str1.split(" ")
# print(words)
revers_str1 = []
for word in words:
    revers_str1.append(word[::-1])
# print(revers_str1)
revers_Sentence = " ".join(revers_str1)
print("This is reverse sentence is : ", revers_Sentence)


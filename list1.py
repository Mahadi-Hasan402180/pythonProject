subject = ["math", "biology", "chemistry", "physics", "biology", "chemistry", "physics"]
print(subject)
print(subject[0])
print(subject[2:5])
print(subject[-1])
print(subject * 3)
print(subject + ["botany", 88])
print(len(subject))
print(type(subject))
print("python" in subject)
print("python" not in subject)

# change item value
subject[2] = "watermelon"
print(subject)
subject[3:5] = ["banana", "apple", "mango"]
print(subject)

# insert item value
subject.insert(2, "mahadi")
print(subject)

# remove item use remove()
# The remove() method removes the specified item.
subject.remove("math")
print(subject)
# The pop() method removes the specified index.If you do not specify the index, the pop() method removes the last item.
# The del keyword can also delete the list completely. del list
# The clear() method empties the list, list.clear() ,The list still remains, but it has no content.


# To add an item to the end of the list, use the append() method
fruits1 = ["apple", "banana", "cherry"]
fruits1.append("orange")
print(fruits1)
# To append elements from another list to the current list, use the extend() method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# for loop of list
friends = ["rasel", "habib", "anika", "noman", "shawon", "shiam"]
for x in friends:
    print(x)

num = [22, 22, 55, 44, 5, 6, 4, 7, 8, 82 , 9]
sum = 0
for y in num:
    sum = sum + y
print(sum)




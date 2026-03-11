list1 = [1,2,3,4,5]
list2 = ["Red","Green", "Blue", "Black"]
list3 = ["C++", 19, 22.3, True]
list4 = [22.5, 12.1, 17.9]


print ("\n", list1, "\n", list2, "\n", list3, "\n", list4)
print (len(list1))
print (len(list2))
print (len(list3))
print (len(list4))
list2.append("Yellow")
print(list2)
list3.insert(1, 189.8)
print(list3)
list4.extend([0.5, 0.19, 6.9])
print(list4)
list3.remove("C++")
print(list3)
list4.pop()
print(list4)
list1.pop(2)
print(list1)
num1 = min(list1)
num2 = max(list1)
print(num1, "\n", num2)
word = min(list2)
print(word)


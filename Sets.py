SetName = {"Byte", "Level", "Score", "Level"}
SetName2 = {"33", "Night", "Son"}
List = ["Number", 33, 33.2, True]
Turtle = ("23.2", 23, 23.2)
Dict = {'HIGH': 'Not', "LOW": "Zero"}
print(SetName)
print(type(SetName))

SetName.add("Score")
print(SetName)
SetName.update(SetName2)
print(SetName)
SetName.update(List)
print(SetName)
SetName.update(Turtle)
print(SetName)
SetName.update(Dict)
print(SetName)
SetName.discard(23.2)
print(SetName)
SetName.remove("33")
print(SetName)
SetName.remove(33.2)
SetName.clear()
print(SetName)
SetList = [1,2,3,2,4,5,5,7,8,8,9,10,11,33]
SetName= set(SetList)
print(SetName)
First = {1,3, 2,7}
Second = {9, 11, 2, 7}
print(First | Second)
print(First & Second)
print(First - Second)
print(First ^ Second)

#for names in SetName:
#    print(names)
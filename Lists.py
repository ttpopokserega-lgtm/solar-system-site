List = [22,33]
Tuple = (22,33, "List", 'Game')

print(type(Tuple))
print(type(List))
print(Tuple[2])

Dict = {'List: ': "Game", 'List2': Tuple}
Dict2 = {'List1:': "Play", 'List2': List}
print(Dict)
print(len(Dict))
print(Dict.items())
print(Dict.keys())
print(Dict.values())
print("List: " in Dict)
print(Dict.get("List1", 'List is false'))
Dict['Key'] = "LEvel"
print(Dict)
Dict ['Key'] = 'Level'
print(Dict)
print(type(Dict))
Dict.update(List2 = 22, j = 'Def', h = 'LOW')
print(Dict)
Dict.update(Dict2)
print(Dict)
del Dict['j']

print(Dict)
non = Dict.pop('h')
print(Dict)
print(non)
popin = Dict.pop('g', 'Not Found')
print(popin)

print(Dict)
popout = Dict.popitem()
print(popout)
print(Dict)
sequence = 'Dicts'
value = 'game'
value1 = 'game2'

Dict = dict.fromkeys(Dict)
print(Dict)


Dict.clear()
print(Dict)
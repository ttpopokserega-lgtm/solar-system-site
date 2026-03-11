a = True
while a:
    nick = input("Enter your nick: ")
    y = nick.isnumeric()
    x = nick.isalpha()
    if (y != False or x == True):
        print("Enter your pass with numbers and letter")
    else:
        break
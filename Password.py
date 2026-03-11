password = 'Serhii2001'
while password:
    word = input("Enter your password here: ")
    WordForPass = word.startswith(('2001', 'Serhii'))
    if WordForPass:
        print("This password is true")
    else:
        print("Try agan")

number = int (input('Enter number of bilet: ' ))

Chair = number// 100
number = number - Chair * 100
Chair2 = number// 10
Chair3 = number - Chair2* 10

Lucky = Chair + Chair2 + Chair3
if (Lucky == 20) :
    print = ('Your bilet is lucky')
else:
    print ('Try again')
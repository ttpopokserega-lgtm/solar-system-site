import re
word1 = "H .e .l .l .o ., ."
word2 = "Serhii!"
letter = word1+word2

print(letter)
char = letter[6]
print(char)
number = len(letter)
print(number)

#letter = letter.replace('Hello', "Hi")
print(letter)
print(letter.count('h',0, number))
Multiply = letter*3
print(Multiply)
splitter = letter.split(".")
print(len(splitter))
#for letter in splitter:
#    print(letter)
#print(splitter[6])
#kon = re.sub("r'\s+'", '', letter)
#print(kon)

messege = """Hello, Serhii!

Hello,Sofia!

Goodbye!"""
print(messege)

messege = '''Hello, Serhii!

Hello,Sofia!

Goodbye!'''
print(messege)
long_text = ("Hello, Serhii!\n \n""Hello,Sofia!\n \n""Goodbye!")
print(long_text)
long_text = "Hello, Serhii!\n \n"\
            "Hello,Sofia!\n \n"\
            "Hello,Sofia!\n \n"
print(long_text)
withSpace = "    #$%Text for lesson"
noSpace = withSpace.lstrip()
print(withSpace)
print(noSpace)
noSimbol = noSpace.lstrip("#$%")
print(noSimbol) #Зупинилися на "Як видалити символи"

Text = "Hello/ my/ friends,/ my/ name/ is/ Chappy!"
SplitText = Text.split("/")

for i in SplitText:
    print(i)


phrase = ' Do   or do    not   there    is  no try   '
phrase_no_space = re.sub(r'\s+', ' ', phrase)
print(phrase)
print(phrase_no_space)

regular = 'My life, my rules<_>GG'
No_space = regular.rstrip("<_>GG")
print(regular)
print(No_space)

regular_text = "      Text with space       "
no_Space = regular_text.strip()
print(regular_text)
print(no_Space)

Big_text = "TEXT fOR BIG BOSS"
mini_text = Big_text.lower()
print(Big_text)
print(mini_text)

Small_text = "Letter fOr mY FriEnd"
max_text = Small_text.upper()
print(Small_text)
print(max_text)

micro_text = "a little man in big city"
Maxi_text = micro_text.title()
print(micro_text)
print(Maxi_text)
# Як використовувати заміну регістру в Python

Convert = "A sMall CyTY is New York"
TextConvert = Convert.swapcase()
print(Convert)
print(TextConvert)


#password = "Good, job!"
#if password:
#   print("Ok")


word = "Space"
tab = 9
c = "F"
word_tab = word.rjust(tab, c)
print(word)
print(word_tab)
tab = tab +4
word_without_tab = word_tab.ljust(tab, c)
print(word_without_tab)

gen = "Україна"
print(gen.isalnum())
gg = gen.isalnum()
#isalnum функціонал

gen2 = "Text with space"
print(gen2.isalnum())
gen3 = "text.More"
print(gen3.isalnum())
#isprintable(): Як перевірити наявність друкованих символів у рядку в Python
table = ""
table1 = '    '
table2 = "\n"
table3 = "n.t.22"
print( table.isprintable(), "\n", table1.isprintable(), "\n", table2.isprintable(), "\n", table3.isprintable())
space1 = " "
space2 = " \v"
space3 = " T h i s i s t e x t "
print("\t", space1.isspace(), "\n\t", space2.isspace(), "\n\t", space3.isspace())

text = "hight text"
print(text)
print(text.capitalize())
text = "HIGHT TEXT"
print(text)
print(text.capitalize())
text = "3HIGH"
print(text)
print(text.capitalize())
text = "IS UP TEXT"
print(text)
print(text.isupper())
text = "Is UP TEXT"
print(text)
print(text.isupper())
text = "IS3$"
print(text)
print(text.isupper())

my_string = "Distance"
print(text.join(my_string))

my_list = ['bmw', 'ferrari', 'mclaren']

print('; '.join(my_list))



my_string = "Get my pen \n Give my pen"
print(my_string.splitlines(False))

text = "Not small text?"
print(text)
print(text.islower())
text = "not small text?"
print(text)
print(text.islower())
text = "not small text"
print(text)
print(text.islower())
number = "12345"
print(number)
print(number.isnumeric())
number = "/1@2#3%4$5&"
print(number)
print(number.isnumeric())
number = "12345"
print(number)
print(number.isnumeric())
number = "\377"
print(number)
print("\u2085".isnumeric())

number = "12345"
print(number)
print(number.isdigit())
print(number)
print("222j".isdigit())

text = "Sosage228"
print(text)
print(text.isalpha())
text = "Sosage "
print(text)
print(text.isalpha())
text = "Sosage"
print(text)
print(text.isalpha())
#istitle(): Як перевірити, чи кожне слово починається з символу верхнього регістру в рядку в Python
text = "This"
print(text)
print(text.istitle())
text = "This is LEGO"
print(text)
print(text.istitle())
text = "This Is 6 & * !"
print(text)
print(text.istitle())
text = "Text\tprint"
print(text)
print(text.expandtabs())
text = "Texteblel\tprint"
print(text)
print(text.expandtabs(5))
text = "Text\tprint\tfall"
print(text)
print(text.expandtabs())
text = "Text print"
num = 50
char = "-"
print(text)
text_center = text.center(num)
print(text.center(num,char))
print(text_center)
text = "Print"

Left_text = text.zfill(num)
print(text)
print(Left_text)

text = "Global word of the world"
print(text)
find_text = text.find("of")
print(find_text)
find_text = text.find("world")
print(find_text)
find_text = text.find("Glob")
print(find_text)
find_text = text.find("world", 0, 12)
if find_text == -1:
    print("This word is not found")

text = "Global word of the world"
Prefix = text.removeprefix("Global")
print(Prefix)
Suffix = Prefix.removesuffix("the world")
print(Suffix)
#lstrip() проти removeprefix() і rstrip() проти removesuffix()
text = "gggggghhhhh28gh"
ltext = text.lstrip("g")
preftext = text.removeprefix("g")
print(text)
print(ltext)
print(preftext)
text = "gh28ggggghhhhh"
rtext = text.rstrip("h")
suftext = text.removesuffix("h")
print(text)
print(rtext)
print(suftext)
text = "Horizontal"
sliced = text[::2]
#sliced = text [початкова позиція відліку:кінцева точка, але не включно:крок, який ми хочемо зробити]
print(text)
print(sliced)
text = "Serhii"
destext = text[2::2]
print(text)
print(destext)




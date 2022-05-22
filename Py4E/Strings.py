text = input("Copy the text you want counted here:  ")
print_variable = 0
check = None
alphabet = 'abcdefghijklmnopqrstuvwxyz'
y = 0
a = 0
b = 0
c = 0
for x in text :
    y = y + 1
    if x == 'a' :
        a = a + 1
    if x == 'b' :
        b = b + 1
    if x == 'c' :
        c = c + 1
print("The text has a total of", y, "characters.")
print("There are", a, "occurences of the letter 'a' in the text.")
print("There are", b, "occurences of the letter 'b' in the text.")
print("There are", c, "occurences of the letter 'c' in the text.")
print("Program Finished.")

for x in text :
    for letter in alphabet :
        print(x)
        x = alphabet[x+1]
        print(x)
            print_variable = print_variable + 1
    print("There are", print_variable, "occurences of the letter", letter, "in the text.")

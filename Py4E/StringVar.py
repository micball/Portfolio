text = input('Insert the text you would like counted here:  ')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
y = 0
for letter in alphabet:
    for x in text :
        if letter == x :
            y = y + 1
    print ("There are", y, "occurences of the letter '", letter, "' in the text.")
    y = 0

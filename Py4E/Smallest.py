y = None
for x in [12, 27, 29, 124, 13326, 1, 14]:
    if y is None :
        y = x
    elif x < y :
        y = x
print("The smallest number is: ", y)
print("Finished.")

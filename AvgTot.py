Loop_iter = 0
Tot_Sum = 0
for x in [12, 19, 27, 6000, 14, 14, 14, 14, 9098, 505]:
    Loop_iter = Loop_iter + 1
    Tot_Sum = Tot_Sum + x
    if x > 500 :
        print (Loop_iter, x, "---LARGE NUMBER")
    else:
        print(Loop_iter, x)
Loop_1_Avg = Tot_Sum / Loop_iter
print('Finished')
print('The program ran', Loop_iter, "iterations of the loop.")
print('The total Sum of the inputs is', Tot_Sum,'.')
print('The Average Number is', Loop_1_Avg, '.')

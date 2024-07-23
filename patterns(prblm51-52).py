#51.print
'''*****
   *****
   *****
   *****
   *****'''
for i in range(6):
    for j in range(6):
        print("*",end="")
    print()

    
#52.print
'''* ***
   * ***
   ** **
   *** *
   ****  '''


for i in range(4):
    for j in range(4):
        if(i==j):
            print(" ",end="")
        else:
            print("*",end="")
    print()
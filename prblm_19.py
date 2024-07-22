#password verifier
#mr.x is trying to create a new password for his instagram account these are the required conditons for creating a new password
#cond1:min length is 8,max length is 15
#cond2:only @,/ is allowed in a password
#cond3:no spaces are allowed
#cond4:only alpha numerics are allowed
#your supposed to print weak if length is exact 8
#length is btwn 8-12(medium)
#if length is betwn is 12-15(strong)
n=input()
l=len(n)
a="@" or "/"
for i in a:        
    if " " not in n:
        if(l==8):
            print("week password")
        elif(l>8 or l==12):
            print("medium password")    
        elif(l>12 or l==15):
            print("strong password")
    else:
        print("please follow all the conditions")
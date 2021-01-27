#from generator-server.src.server import input_string
def isBalanced(s):
    i =0 
    x = 0
    y = 0
    z = 0
    while(i<len(s)):
        if (s[i] == '('):
            x+=1
        elif (s[i]==')'):
            x-=1
        elif (s[i]=='['):
            y+=1
        elif (s[i]==']'):
            y-=1
        elif (s[i]=='{'):
            z+=1
        elif (s[i]=='}'):
            z-=1
        else:
            print("the string contains a bad character") 
            break
        if((x<0) or (y<0) or (z<0)):
            break
        i+=1
        
    if (i<len(s))or(x!=0)or(y!=0)or(z!=0):
         print("False: the string is not balanced")
    else :
        print("True: the string is balanced")
s=input_string()
print(s)
isBalanced(s)
        

        

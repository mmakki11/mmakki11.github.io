# Source: index.html link "Dessert Exam Questions" (pythontutor.com)
#Fall 2012, #5, version 1
def enigma1(x,y,z):
    if x == len(y):
        return(z)
    elif x < len(y):
        return(y[0:x])
    else:
        s = cont1(z)
        return(s+y)
def cont1(st):
    r = ""
    for i in range(len(st)-1,-1,-1):
        r = r + st[i]
    return(r)
    
enigma1(7,"caramel","dulce de leche")
enigma1(3,"cupcake","vanilla")
enigma1(10,"pie","nomel")

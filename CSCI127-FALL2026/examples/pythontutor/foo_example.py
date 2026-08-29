# Source: index.html link "Foo Example" (pythontutor.com)
 #From Sample Exam, F 2014
 
def bar(n):
    if n <= 8: 
        return 1
    else:
        return 0

def foo(l):
    n = bar(l[-1])
    return l[n]
    
r = foo([1,2,3,4])
print("Return:  ", r)

r = foo([1024,512,256,128])
print("Return:  ", r)

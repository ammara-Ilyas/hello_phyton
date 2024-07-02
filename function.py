# two types of function
#user defined function
y="You are awesome"
def myFunc():
    print("like as",y)
myFunc()
#
def my_func(fname,lname):
    print(fname," ",lname)
    
my_func("Maha","nazz")   
#default value
def default_func(a=2,b=3):
    print(a*b)
default_func()    
#default value start from end
def default_func(a,b=3):
    print(a*b)
default_func(10) 

list=["yellow","blue","golden","blue","orange"]
def print_list(list):
    for i in range(len(list)):
       print(i,list[i],end=",")
       
print_list(list)       
# #built in function
# print("hello","world") #sep=""
# print("hello",end="+")  #by default end="\n"
# print("world")
# len("Hello")





#Recursion

def show(n):
    if n==10:
        return
    print(n)
    show(n+1)
    
show(2)    
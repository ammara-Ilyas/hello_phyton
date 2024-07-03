def add(a,b):
    return a+b,a-b
add,sub=add(2,5)
print(add)
print(sub)

# BY lmbda function

add=lambda a,b:(a+b,a-b)
print(add(7,8))

def add(n):
    print(n,"n")
    return lambda a:a*n
addFunc=add(10)
print("add function",addFunc(5))

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

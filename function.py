#############################Function
y="You are awesome"
def myFunc():
    print("like as",y)
myFunc()
######################list
x = ["apple", "banana", "cherry"]	
my_list=["Hero","Villain","Dada","Hero"]
my_list[1:3]=["jahan","Sikander"]
#########addd
my_list.append("Bahobali")
my_list.insert(0,"Villain")
print(my_list,"my_list")
print(len(my_list))
print("2 no",my_list[2])
print("1:3",my_list[1:3])

########remove
print("remove")
thislist = ["apple", "banana", "cherry", "banana","cherry", "banana","cherry","apple"]
thislist.remove("banana")
print(thislist,"remove")
thislist.pop()
print(thislist,"pop")
del thislist[0]
print(thislist,"del")
thislist.clear()
print(thislist,"clear")



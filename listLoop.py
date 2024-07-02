thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
thislist = ["apple", "banana", "cherry","grapes"]
for i in range(len(thislist)):
  print(thislist[i])

new_list=[]
for x in thislist:
    if "a" in x:
        new_list.append(x)

print(new_list,"new_list")        
mylist = thislist.copy()
print(mylist)
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3,"joined list")


list1.extend(list2)
print(list1,"extend")

#####################list
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



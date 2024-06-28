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
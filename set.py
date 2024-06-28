myset = {"apple", "banana", "cherry","apple"} #not duplicate value
print(myset)

thisset = {"apple", "banana", "cherry", True, 1, 2,False,5} #true and 1 consider same value
print(thisset,"this set")
#########################add item
thisset.add("orange")
print(thisset)
new_set={"Hero","villian","jupiter"}
myset.update(new_set)
print(myset,"update list")
#######################remove items
thisset.remove("cherry")
print("removed set",thisset)
myset.discard("banana")
print("discard set",myset)

####################loop for set
for x in thisset:
    print(x)
    
 ###############join multiple sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)   

set3 = set1 | set2
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
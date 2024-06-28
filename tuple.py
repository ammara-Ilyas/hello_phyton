tupleData=("apple",2,"Orange","Hero",5)
print(tupleData)
print(tupleData[2])
print(tupleData[1:4])
print(tupleData[:4])

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)
#########################unpack
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
#################amazing new thing multiply
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 4

mytuple.index(2)
print(mytuple)
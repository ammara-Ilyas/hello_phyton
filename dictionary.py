#############like object
thisdict = {
"hero":"sidarth",
"age":21,
"play":"aladin"
}
print(thisdict)
print(thisdict["age"])
print(thisdict.get("age"))
print(thisdict.keys())
#################change item
thisdict = {
"hero":"sidarth",
"age":21,
"play":"aladin"
}
thisdict["age"]=25
thisdict.update({"hero":"Sidarth Nigam"})
print(thisdict,"new dictionary")
####################add item
thisdict = {
"hero":"sidarth",
"age":21,
"play":"aladin"
}
thisdict["color"]="white"
thisdict.update({"heroine": "anveet"})

print("added dictionary",thisdict)
##################remove items
thisdict.pop("heroine")
print(thisdict)
#####remove lasst
thisdict.popitem()
print(thisdict)
for x in thisdict:
  print(x)
  print(thisdict[x])
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
######################nested  dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child2"]["name"])
for x, obj in myfamily.items():
  print(x,"x")

  for y in obj:
    print(y + ':', obj[y])
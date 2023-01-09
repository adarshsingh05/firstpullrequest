mydict= {"ram": "name of a god",
"adarsh": "a vit ap student",
"akash": "brother of adarsh",
"num":"1,2,3,4,5",
"anotherdict":{'jee':'joint entrance exam'}
}
print(list(mydict.keys()))
# use to print the list of keys.
print(list(mydict.values()))
# use to print the list of values.
print(list(mydict.items()))
# use to print the all values of all list and data items altogether.
changedict= { "aditya": "friend of adarsh"}
mydict.update(changedict)
print(mydict)
# updating dict with new values
print(mydict.get("ram"))
print(mydict["ram"])
# both do the same thing but a slite change is there when we use the get function then it does not thrw error 
# but show none for eg below
print(mydict.get("ram2"))


print(len(mydict))
# print the length

del mydict["akash"]

print("ram" in mydict)
# print wether that key values are present 

# we can delete any value using this aasignment operator


# print(mydict["ram2"])
# it will give one error.
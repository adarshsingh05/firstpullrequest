# making a code that take input for five fruits

f0=("your fruit list is as follow")
f1=input("name the fruit 1")
f2=input("name the fruit 2")
f3=input("name the fruit 3")
myfruitlist = [f0,f1,f2,f3]
print(myfruitlist)

# code for accepting marks of five students and arranging in inc order
l1=int(input("enter the number of roll no 1:\n"))
l2=int(input("enter the number of roll no 2:\n"))
l3=int(input("enter the number of roll no 3:\n"))
l4=int(input("enter the number of roll no 4:\n"))
l5=int(input("enter the number of roll no 5:\n"))
mylist=[l1,l2,l3,l4,l5]
mylist.sort()
print (mylist)
# ading number of students of a class

m1= int(input("enter no of roll no 1:\n"))
m2= int(input("enter no of roll no 2:\n"))
m3= int(input("enter no of roll no 3:\n"))
m4= int(input("enter no of roll no 4:\n"))
m5= int(input("enter no of roll no 5:\n"))
m6= int(input("enter no of roll no 6:\n"))
m7= int(input("enter no of roll no 7:\n"))
m8= int(input("enter no of roll no 8:\n"))
m9= int(input("enter no of roll no 9:\n"))
m10= int(input("enter no of roll no 10:\n"))
mylist=[m1,m2,m3,m4,m5,m6,m7,m8,m9,m10]
print("sum of markss of all students are:",sum(mylist))
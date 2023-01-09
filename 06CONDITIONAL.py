a = (input("enter the number a"))
a= int(a)
if(a>3):
     print("the value of a is greater than 3")
elif(a>7):
     print("a is greater than 7")
else:
     print(" a is not in the given values")

    # indent is important otherwise it will not run that is
    # ek line me hona chachiye  and if you use the elif inside the other then double gap accordingly.
# sabse pahle wo first staetement pe focus krega then baki pe agar pahla true hgya to wahi ruk jayga and the ladder does not work.

# multiple if statement:-
b =input("enter the number b")
b = int(b)
if(b>15):
     print("b is greater than 15")
if(b>18):
     print("b is greater tha 18")
if(b<25):
     print("b is less than 25")
if(b>777):
     print("b is greater than 777")
else:
     print(" b is not in the given values")
# baki sabhi lines as usual print hoaga but last wala lader banega and koi ek line hi print hoga
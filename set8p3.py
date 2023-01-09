n=int(input("enter the six distance"))
if n>100:
    print("Out of park")
elif n in range(90,100):
    print("Excellent dictance")
elif n in range(80,90):
    print("Good distance")
elif n in range(70,80):
    print("Just cleared the rope")
elif n in range(0,70):
    print("Not cleared the ropes")
else:
    print("the input is not in given range")
    
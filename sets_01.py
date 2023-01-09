maths=int(input("enter the marks in maths"))
science=int(input("enter the marks in science"))
english=int(input("enter the marks inenglish"))
cse=int(input("enter the marks in cse"))
sst=int(input("enter the marks in sst"))
total_marks=maths+science+english+sst+cse
print(total_marks)
avg_marks=(maths+science+english+sst+cse)/5
print(avg_marks)
if avg_marks>90:
    print("the student got S grade")
elif avg_marks in range(80,90):
    print("the student got A grade")
elif avg_marks in range(70,80):
    print("The student got B grade")
elif avg_marks in range(60,70):
    print("the student got C grade")
elif avg_marks in range(50,60):
    print("The student got D grade")
elif avg_marks in range(40,50):
    print("the studnet got E")
elif avg_marks <30:
    print("the student got F grade")
else:
    print("NOT A VALID INPUT")

# vertical printing
n=5
for i in range(n):
    print("*")

# horizontal printing
n2=5
for i in range(n2):
    print('*',end=' ')


z=5
for i in range(z):
    print((str(z)+" ")*z)

n=5
for i in range(n):
    print((str(i+1)+" ")*n)

# normal pyramid
n=5
for i in range(n):
    print(("*"+" ")*(i+1))

# reverse star pyramid
n=5
for i in range(n):
    print('* '*(n-i))


# reverse with digits
n=5
for i in range(n):
    for j in range(n-i):
        print(j+1, end=' ')
    print()


# pyramid with digits.
n=5
for i in range(n):
    print(' '*(n-i-1)+(str(i+1)+' ')*(i+1))


# full diamond
n=5
for i in range(n):
    print(' '*(n-i-1)+'* '*(i+1))
for i in range(n-1):
    print(' '*(i+1)+'* '*(n-i-1))


# right half diamond and left half together
n=5
for i in range(n):
    print(''*(n-i-1)+'*'*(i+1))
for i in range(n):
    print(' '*(n-i-1)+'*'*(i+1))




# top half diamond
n=5


for i in range(n):
    print('  '*(n-i-1)+"*",end='')
    if i>=1:
        print(('  ')*(2*i-1)+'*',end='')
    print()

# pyq

n=5
for i in range(n):
   for j in range(i+1):
    print(i-j+1,end=' ')
   print()
    
n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1):
            print(end=" ")
    print()

str=input("Enter a string ")
j=0
a=" "
for i in str:
    j=ord(i)
    if j!=90 and j!=122:
        j=j+3
    if j==90:
        j=65
    if j==122:
        j=97
    a=a+chr(j)
print(a)

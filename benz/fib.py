n = int(input("Enter the limit of the series"))
print("The fibonacci series upto ", n, "are")
a = 0
b = 1
c=a+b
print(a,b)
for i in range(0,n):
    print(c)
    a=b
    b=c
    c=a+b
    i=i+1
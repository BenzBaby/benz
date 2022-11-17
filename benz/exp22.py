n=int(input("enter the no of elements:"))
print("enter the elements")
list1=[]
count=0
for i in range(0,n):
    element=input()
    list1.append(element)
    print(list1)
for i in list1:
    for j in i:
         if j=='a' or j=='A':
           count=count+1
print("the occurance of 'a' in list is",count)

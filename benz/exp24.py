str1=input("enter a string:")
print(str1)
dict3={}
str4=str1.split()
for i in str4:
    if i in dict3:
        dict3[i]+=1
    else:
       dict3[i]=1

for j,k in dict3.items():
       print(j,k)
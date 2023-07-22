
# Data : Heterogeneous
# Ordered : yes
# Indexed : yes
# Mutable : yes
# Duplicates : yes

data=[11,21,51,101,21,11]

print("Output using for")
for no in data:         #for each loop of java
    print(no, end=" ")          #end to avoid next line
print()


print("output using for with index")
for i in range(0,len(data)):
    print(data[i],end=" ")
print()


print("Output using while with index")
i=0
while(i<len(data)):
     print(data[i],end=" ")
     i=i+1
print()





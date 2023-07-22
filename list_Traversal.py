#travesing the list
values=[10,20,30,40,50]
print(values[0])
print(values[1])
print(values[2])
print(values[3])
print(values[4])

#traversing list
for i in range(0,len(values),1): #prefer this one
    print(values[i])

for no in values:  #same like for each loop in java
    print(no)
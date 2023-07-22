print("Demonstration of list")

# Data : Heterogeneous
# Ordered : yes
# Indexed : yes
# Mutable : yes
# Duplicates : yes

data=[11,21,51,101,21,11]
data1=[11,90,80,True,"hello"]   #heterogeneous

print("Data is heterogeneous : ",data1)
print("Data is ordered : ",data1)
print("data at index 2 : ",data1[2])
print("Data with duplicate elements : ",data)

print("List is mutable")
data.append(201)
print("Data after append : ",data)

data.pop()
print("data after pop : ",data)
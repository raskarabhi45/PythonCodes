# square bracket is subscriptable operator
print("Demonstration of set")

# Data : Heterogeneous
# Ordered : no
# Indexed : no
# Mutable : yes        frozen set for immutable
# Duplicates : no

data={11,21,51,101,11,21}
data1={11,90,80,True,"hello"}  #heterogeneous

print(data)
print(len(data))
print("Data is heterogeneous : ",data1)
print("Data is unordered : ",data1)
#print("data at index 2 : ",data1[2])
print("Data not allow duplicate elements : ",data)

print("set is mutable")
#insert element in set
data.add(251)
data.add(151)
print("Data after insertion : ",data)

#remove element in set
data.remove(251)
print("Data after removal : ",data)

data.discard(201)   
print("Data after removal : ",data)


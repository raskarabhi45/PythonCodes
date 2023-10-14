print("Demonstration of Dictionary")

# Data : Heterogeneous
# Ordered : yes
# Indexed : no
# Mutable : yes
# Duplicates : no

programming={"c":"Ritchie" , "c++":"Stroustrup" , "java":"gosling" , "python":"rossum"}
batches={"PPA":18000, "LB":16700, "Python":16500 , "Angular":15000}
print("Data of programming : ",programming)
print("Data of dictionary : ",batches)
print("Data type is : ",type(batches))
print("len of dictionary : ",len(batches))
print("value of PPA is :",batches["PPA"])
print(programming["java"])

#op
# Demonstration of Dictionary
# Data of programming : {'c': 'Ritchie', 'c++': 'Stroustrup', 'java': 'gosling', 'python': 'rossum'}
# Data of dictionary :  {'PPA': 18000, 'LB': 16700, 'Python': 16500, 'Angular': 15000}
# Data type is :  <class 'dict'>
# len of dictionary :  4
# value of PPA is : 18000
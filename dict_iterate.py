#juat iterating over the dictionary
batches={"PPA":18000, "LB":16700, "Python":16500 , "Angular":15000}

print("Data of dictionary : ",batches)

print("Data traversal using for loop")
for x in batches:
    print(x)
print() #new line

#for displaying key value pair
print("Data traversal using for loop")
for x in batches:
    print(x,batches[x])
print()



print("Data traversal using for loop")
for x in batches:
    print(x,batches.get(x))

keybatches=batches.keys()
print(type(keybatches))# <class 'dict_keys'> dict_keys(['PPA', 'LB', 'Python', 'Angular'])
print(keybatches)

valuebatches=batches.values()  
print(type(valuebatches))  # <class 'dict_values'> dict_values([18000, 16700, 16500, 15000])
print(valuebatches)


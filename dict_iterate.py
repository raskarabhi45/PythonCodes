
batches={"PPA":18000, "LB":16700, "Python":16500 , "Angular":15000}

print("Data of dictionary : ",batches)

print("Data traversal using for loop")
for x in batches:
    print(x)
print()

#for displaying key value pair
print("Data traversal using for loop")
for x in batches:
    print(x,batches[x])
print()



print("Data traversal using for loop")
for x in batches:
    print(x,batches.get(x))

keybatches=batches.keys()
print(type(keybatches))
print(keybatches)

valuebatches=batches.values()
print(type(valuebatches))
print(valuebatches)


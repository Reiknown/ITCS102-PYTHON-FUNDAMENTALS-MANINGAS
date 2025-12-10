# List & It's Functions

nm = ['apple','hotdog','orange','watermelon','egg']
nm.append('mango')   #add an item to the last of the list
print(nm)

nm.pop()    #remove the last item
print(nm)

nm.insert(0,'watermelon')   #add item in dif position
print(nm)

for i in nm:
    print(f"{i}  in the basket")    #all fruits one by one with 'in the basket' at the last

mi = 'HANNIEL MANINGAS'
for u in mi:
    print(u)    #Will print my name from f to e
    
print("\nReversed")
for q in mi[::-1]:  #will print my name in reverse from n to j
    print(q)


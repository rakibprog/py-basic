#Remove list

thislist = ['Apple','Banna','Orange']

thislist.remove('Banna')
print(thislist)

# Remove the first occurrence  of banna

thislist = ['Apple','banna','orage','banna']

thislist.remove('banna')
print(thislist)

#The del keyword remove the specific index

thislist = ['Apple','Banna','Orange']

del thislist[0]
print(thislist)

#Clear the list

thislist = ['apple','banna','cherry']

thislist.clear()

print(thislist)

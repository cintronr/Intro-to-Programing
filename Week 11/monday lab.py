
dictionary = {1:"Rico",2:"Joyce",3:"Zoe","c":"b"}
print (dictionary [1])
print (dictionary)

if 'g' in dictionary:
    print("The key 2 is in the Dictionary")

for x in dictionary:
    print (x)
    print (dictionary[x])

dictionary['z']=56
del dictionary [1]
print(dictionary)

mylist = [(1,2),(2,2),(3,2),(4,5)]
print (mylist)

dict(mylist)
print (dict(mylist))

x= dict (mylist)
print (x)

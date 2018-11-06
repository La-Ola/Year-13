#Bubble sort 
usortedlist = ["1","7","3","8","4","6","2","9","5"]
print(usortedlist)

swap = True
while swap == True:
    swap = False 
    for position in range (len(usortedlist)-1):
        if (usortedlist[position]) > (usortedlist[position+1]):
            new1 = usortedlist[position+1]
            new2 = usortedlist[position]
            usortedlist[position+1] = new2
            usortedlist[position] = new1
            swap = True
    newlist = usortedlist
    print (newlist)
            
#how to split a list in half

unsortedlist = ["1","7","3","8","4","6","2","9","5"]
    
half = len(unsortedlist)//2
unsortedlist1 = unsortedlist[:half]
unsortedlist2 = unsortedlist[half:]
print(unsortedlist1)
print(unsortedlist2)
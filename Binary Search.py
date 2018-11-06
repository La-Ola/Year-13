#Binary Search

def binary(search):
    list = ["1","2","3","4","5","6","7","8","9"]
    lower = 0
    upper = len(list) -1
    
    found = False
    while found == False and lower != upper:
        mid = round((lower + upper)/2)
        print (mid)
        if list[mid] == search:
            found = True
            print ("found at position", mid)
        elif list[mid] < search:
            lower = mid + 1
        elif len(list) == 3:
            for i in range (len(list)):
                if list[i] == search:
                    found = True
                    print ("found at position", mid + 1)   
        else:
           upper = mid - 1
    return found
       

search = input("enter what yoou're looking for")
found = binary(search) # feeds search into def binary      

if found == False:
    print("item not in list")
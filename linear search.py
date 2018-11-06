#linear searching
pointer = 0
x = int(input("how many entries do you want in the list?"))
for i in range (x):
    enter = input("enter what youd like to put into the list; only one data type please")
    list = []
    list.append(enter)##
    
print(list)
search = input("what are you searching for?")


while pointer < len(list) and list[pointer]!= search:
    pointer = pointer + 1
    
if pointer >= len(list):
    print("item isn't in list!")
    
else:
    print("item located in position", pointer + 1)
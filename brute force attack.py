#brute force attack

cypher = input("input your cypher")
new = ""

a = -25
while a < 25 :
    a = a + 1
    new = ""
    for i in range (len(cypher)):
        val = ord(cypher[i])
        val = val + a
        nextt = chr(val)
        new = new + nextt

    print(new)
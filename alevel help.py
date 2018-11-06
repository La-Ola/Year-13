#naughts and crosses

x = [
    ["","","",""],
    ["","","",""],
    ["","","",""],
    ["","","",""],
    ["","","",""],
    ["","","",""],
    ]
for i in range (4):
    def displaygrid():
        for i in range(6):
            print(x[i])

    def makegrid():
        for i in range(6):
            for j in range(4):
                x[i][j] = "x"

    makegrid()

    i_ = int(input("what line would you like the '0' to be on?"))
    j_ = int(input("which collumn would you like the '0' to be on?"))

    x[i_ - 1][j_ - 1] = "0"

    displaygrid()
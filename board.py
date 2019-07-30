from qwerty import *
n = int(input("what number is N\n"))
k = int(input("what number is K\n"))
char = input("what character is Char\n")
print("\n")


q = blah(n,k, char)


cb = [0,1]
while(True):
    meh = input("direction")
    if meh == "right":
        cb[0]+= 1 
        q[cb[0]][cb[1]] = 0
        print(q)
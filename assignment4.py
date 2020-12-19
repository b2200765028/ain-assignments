import sys ,os
if len(sys.argv) != 5:
    print("Parameter Number Error")
    exit()

letterscode = "-abcdefghıjklmnopqrstuvwxyz "

if sys.argv[1] != "dec" and sys.argv[1]  != "enc":
    print("Undefined parameter ")
    exit()
## should check whether file exists or Not

if os.path.exists(sys.argv[3]) :  
    pass
else:
    print("Input file  not found")
    exit()

if os.path.exists(sys.argv[2]):
    pass
else:
    print("Key file not found")
    exit()

try:
    input_file = open(sys.argv[3],"r")
    line = input_file.readline()
    list_line = [x for x in line ]
    assert   len(list_line) != 0

except IOError:
    print("Input File could not be read")
    exit()
except AssertionError:
    print("Input file is empty")
    exit()


try:
    for x in  range(len(list_line)):
        if list_line[x].lower()not in letterscode:
            raise AssertionError
        elif "-" in list_line[x]:
            raise AssertionError  
except AssertionError:
    print("Invalid character in input file ")
    exit()

try:
    key_file= open(sys.argv[2],"r") 
    keymatrixlist,count  = [],0
    for j in key_file.readlines():
        j ,u,numberlist= j.rstrip("\n"),[],[]
        for i in range(len(j)):
            if j[i] != ",":
                u.append(int(j[i]))
        keymatrixlist.append(u)
        count +=1
    key_matrix = count   
    assert len(keymatrixlist) != 0
except IOError:
    print("Key file could not be read")
    exit()
except AssertionError:
    print("Key file is empty")
    exit()

letterlist = []  
y,a = 0,""
while y < len(list_line): 
    if y < len(list_line):
        x = 0
        a = ""
        if y + key_matrix <= len(list_line):
            while x < key_matrix:
                a += (list_line[y+x])
                x+=1
            letterlist.append(a)
        elif  list_line[y] != "":
            while y+x<len(list_line):
                a += list_line[y+x]
                x +=1
            while len(a) != key_matrix:
                a += " "
            
            letterlist.append(a)

        y+=key_matrix

def encode_to_number(letterlist):
    global matrixlist,count
    matrixlist = []
    for i in range(len(letterlist)):
        z= []
        for j in range(len(letterlist[i])):
            letter = letterlist[i][j].lower()
            number = letterscode.index(letter)
            z.append(number)
        matrixlist.append(z)
    return matrixlist  

encode_to_number(letterlist)
print(matrixlist)
print(keymatrixlist)
matrix2 , result = [] , []
for i in range(len(matrixlist)):
    a = []
    for j in range(len(matrixlist[i])):
        a.append([matrixlist[i][j]])
    matrix2.append(a)
print(matrix2)
for i in range(len(matrix2)):
    matrix3 = matrix2[i]
    result1 = []
    for j in range(len(matrix3)):
        result1.append([0])
    for u in range(len(keymatrixlist)):
        for w in range(len(matrix3[0])):
            for k in range(len(matrix3)):
                result1[u][w] += keymatrixlist[u][k]*matrix3[k][w]
            
    result.append(result1)
print(result)

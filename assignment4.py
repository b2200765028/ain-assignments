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

except IOError:
    print("Input File could not be read")
    exit()
except AssertionError:
    print("Input file is empty")
    exit()


try:
    if sys.argv[3] == "plain_input.txt":
        line = input_file.readline()
        list_line = [x for x in line ]
        for x in  range(len(list_line)):
            if list_line[x].lower()not in letterscode:
                raise KeyError
            elif "-" in list_line[x]:
                raise KeyError
        assert len(list_line)!=0
    elif sys.argv[3] == "ciphertext.txt":
        numberlist = []
        for line in input_file.readlines():
            x = line.split(",")
            for i in range(len(x)):
                numberlist.append(int(x[i]))
        assert len(numberlist) !=0    
        print(numberlist)
except AssertionError:
    print("Input file is empty")
    exit()
except KeyError:
    print("Invalid character in input file")
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

def encode_to_number(letterlist):
    global matrixlist,result,stra,keymatrixlist
    matrixlist , result , stra = [] , [] , ""
    for i in range(len(letterlist)):
        z= []
        for j in range(len(letterlist[i])):
            letter = letterlist[i][j].lower()
            number = letterscode.index(letter)
            z.append(number)
        matrixlist.append(z)
    
    matrix2 , result = [] , []
    for i in range(len(matrixlist)):
        a = []
        for j in range(len(matrixlist[i])):
            a.append([matrixlist[i][j]])
        matrix2.append(a)
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
    for i in range(len(result)):
        for j in range(len(result[i])):
            stra += (' '.join(map(str, result[i][j])))
            stra += ","
        
    stra = stra.rstrip(",")
    return stra


def inverse(keymatrixlist):
    global key_matrix 
    if key_matrix==2:
        a , d , b , c = keymatrixlist[0][0],keymatrixlist[1][1],keymatrixlist[0][1],keymatrixlist[1][0]
        keymatrixlist[0][0] = d
        keymatrixlist[1][1] = a
        keymatrixlist[0][1] = -b
        keymatrixlist[1][0] = -c
    return keymatrixlist

def decode(numberlist):
    targetlist = []
    j = 0
    y = []
    for i in range(len(numberlist)):
        j +=1
        y.append([numberlist[i]])
        if j%n ==0:
            targetlist.append(y)
            y = []

if sys.argv[1] == "enc":    
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
    encode_to_number(letterlist)
    f = open(sys.argv[4],"w")
    f.writelines(stra)




elif sys.argv[1] == "dec":
    
    
    
    
    
    
    
    pass

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
    if sys.argv[3] == "enc":
        line = input_file.readline()
        list_line = [x for x in line ]
        for x in  range(len(list_line)):
            if list_line[x].lower()not in letterscode:
                raise KeyError
            elif "-" in list_line[x]:
                raise KeyError
        assert len(list_line)!=0
    elif sys.argv[1] == "dec":
        numberlist = []
        for line in input_file.readlines():
            x = line.split(",")
            for i in range(len(x)):
                numberlist.append(int(x[i]))
        assert len(numberlist) !=0   
        numberlist1 = numberlist 
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
    elif key_matrix ==3:
        try:
            a,b,c = keymatrixlist[0][0],keymatrixlist[0][1],keymatrixlist[0][2]
            d,e,f = keymatrixlist[1][0],keymatrixlist[1][1],keymatrixlist[1][2]
            g,h,ı = keymatrixlist[2][0],keymatrixlist[2][1],keymatrixlist[2][2]
            det =  a*(e*ı-f*h) - b*(d*ı-f*g) + c*(d*h - e*g)
            keymatrixlist = [[(e*ı-f*h)/det,-(b*ı-c*h)/det,(b*f-c*e)/det],[-(d*ı-f*g)/det,(a*ı-c*g)/det,-(a*f-c*d)/det],[(d*h-e*g)/det,-(a*h-b*g)/det,(a*e-b*d)/det]]
            return keymatrixlist
        except ZeroDivisionError:
            pass

def decode(targetlist):
    global stra
    result , stra = [],""
    for i in range(len(targetlist)):
        matrix2 = targetlist[i]
        result1 = []
        for j in range(len(matrix2)):
            result1.append([0])

        for u in range(len(keymatrixlist)):
            for w in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    result1[u][w] += keymatrixlist[u][k]*matrix2[k][w]
            
        result.append(result1)
    for i in range(len(result)):
        for j in range(len(result[i])):
        
            stra += letterscode[result[i][j][0]]
    return stra


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
    targetlist = []
    j , count = 0 , 0
    y = []
    kalan = len(numberlist1)%key_matrix 
    for i in range(len(numberlist1)):
        j +=1
        y.append([numberlist1[i]])
        if j%key_matrix ==0:
            count +=1
            targetlist.append(y)
            y = []
    y = []
    if kalan !=0:
        for b in range(count*key_matrix,len(numberlist1)):   
            y.append([numberlist1[b]])
    
        while len(y) != key_matrix:
            y.append([27])
        targetlist.append(y)
    inverse(keymatrixlist)
    decode(targetlist)
    f = open(sys.argv[4],"w")
    f.writelines(stra)
    
    
    
    
    
    
    
    pass

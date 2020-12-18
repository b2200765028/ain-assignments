import sys ,os
if len(sys.argv) != 5:
   print("Parameter Number Error")
   exit()

letterlist = "-abcdefghıjklmnopqrstuvwxyz "

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
      if list_line[x].lower()not in letterlist:
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

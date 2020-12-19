import sys

try:
   if len(sys.argv) != 3:
      raise IndexError
   if sys.argv[2] != "comparison_data.txt":
      raise IOError
   comparisonfile = open(sys.argv[2],"r")
except IndexError:
   print("IndexError: number of input files less than expected\n\n- Game Over -")
   exit()
except IOError:
   print("IOError cannot open {}\n\n- Game Over -".format(sys.argv[2]))
   exit()

try:
   if sys.argv[1] != "operands.txt":
      raise IOError
   operandsfile = open(sys.argv[1],"r")
except IOError:
   print("IOError: cannot open {}\n\n- Game Over -".format(sys.argv[1]))
   exit()

operandlist = [x.split() for x in operandsfile.readlines()]
comparisonlist = [y.split() for y in comparisonfile.readlines()]

oplist1 = []
complist1 = []
i,j = -1,-1
while len(oplist1) != len(operandlist):       
      while i < len(operandlist)-1:
         i+=1
         a = []
         j = -1
         while j < len(operandlist[i])-1:
            j+=1
            u = operandlist[i][j]
            if u.isdigit():
               a.append(int(u))
            elif "." in u:
               u = float(u)
               a.append(int(u))
            else:
               a.append(str(u))
         oplist1.append(a)

i,j = -1,-1

while len(complist1) != len(comparisonlist):       
      while i < len(comparisonlist)-1:
         i+=1
         a = []
         j = -1
         while j < len(comparisonlist[i])-1:
            j+=1
            u = comparisonlist[i][j]
            if u.isdigit():
               a.append(int(u))
            elif "." in u:
               u = float(u)
               a.append(int(u))
            else:
               a.append(str(u))
         complist1.append(a)

def print_input(x):
   stra = (' '.join(map(str, x)))
   return stra

class myError(Exception):
   pass

a , z= 0,-1
while a != len(oplist1): 
   try:
         print("---------------------")
         while z < len(oplist1)-1:
            z+=1
            outputlist = []
            oplist = oplist1[z]
            complist = complist1[z]
            a+=1
            for j in range(oplist[2],oplist[3]+1):
               if j%(oplist[0]) == 0 and j%(oplist[1]) !=0:
                  outputlist.append(j)
            assert outputlist == complist  
            if outputlist == complist:
               raise myError
   except ZeroDivisionError:
         print("ZeroDivisionError: You can't divide by 0\nGiven input: {}".format(print_input(oplist)))
   
   except ValueError: 
         print("ValueError: only numeric input is accepted\nGiven input: {}".format(print_input(oplist)))
   
   except IndexError:
         print("IndexError: number of operands less than expected\nGiven input: {}".format(print_input(oplist)))
   
   except AssertionError:
         print("My Results:\t\t{}\nResults to compare:\t{}".format(print_input(outputlist),print_input(complist)))
         print("Assertion Error: results don’t match.")
   except myError:
         print("My Results:\t\t{}\nResults to compare:\t{}".format(print_input(outputlist),print_input(complist)))
         print("Goool!!!") 
   except TypeError:
      print("ValueError: only numeric input is accepted\nGiven input: {}".format(print_input(oplist)))
   
   except Exception as e:
         print("kaBOOM: run for your life!".format(print_input(outputlist)))
   else:
         print("My Results:\t\t{}\nResults to compare:\t{}".format(print_input(outputlist),print_input(complist)))
         print("Goool!!!") 
print("- Game Over -")

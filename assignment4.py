import sys ,os
if len(sys) != 5:
    print("Parameter Error")
    exit()
letterlist = "-abcdefghıjklmnopqrstuvwxyz "
###try except error catching at openings


try :
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
      if list_line[x] not in letterlist:
          raise AssertionError
      elif "-" in list_line[x]:
          raise AssertionError  
except AssertionError:
    print("Invalid character in input file ")
    exit()
    
try:
    key_file_txt = open(sys.argv[2],"r")    
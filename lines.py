import sys

def main():
    lenght_arg()

    try:
         file = open(sys.argv[1], "r")
         lines = file.readlines()
         print(lines)

    except FileNotFoundError:
         sys.exit("File does not exist")
    
    count = 0
    for line in lines:
         if myline(line) == False:
              count +=1
    print(count)

def lenght_arg():
      if len(sys.argv) < 2:
           sys.exit("Too few command-line arguments")
                
      elif len(sys.argv) > 2:
           sys.exit("Too many command-line arguments")
    
      elif sys.argv[1].endswith(".py") == False:
           sys.exit("Not a Python file")
                
      print(sys.argv[1]) 

def myline(line):
     if line.isspace():
          return True
     if line.lstrip().startswith('#'):
          return True
     return False
    
if __name__ == "__main__":
     main()
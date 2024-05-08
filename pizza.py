import sys
import csv
import tabulate

def main():
    lenght_cmd()

    try:
         with open(sys.argv[1], "r") as file:
              reader = csv.DictReader(file)
              print(tabulate(reader, headers= "keys", tablefmt = "grid"))

    except FileNotFoundError:
         sys.exit("File does not exist")
    

def lenght_cmd():
      if len(sys.argv) < 2:
           sys.exit("Too few command-line arguments")
                
      elif len(sys.argv) > 2:
           sys.exit("Too many command-line arguments")
    
      elif sys.argv[1].endswith(".csv") == False:
           sys.exit("Not a CSV file")
                
      print(sys.argv[1])
    


if __name__ == "__main__":
    main()



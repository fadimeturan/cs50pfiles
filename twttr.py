def main():
    my_input = input("Input: ")
    output = shorten(my_input)
    print("Output: "+output)

def shorten(word):
    text = ""
    
    for letter in word:
        if letter not in ["a","e","i","o","u", "A", "E" "I", "O", "U"]:
            text += letter
    return text

if __name__ == "__main__":
    main()

"""
def main():
    the_input = input("Input: ")
    print("Output: ", end="")
    shorten(the_input)
    
def shorten(the_input):
     for letter in the_input:
          if not letter in ["a", "e", "i", "u",  "o", "A", "E", "I", "U", "O"]:
              print(letter, end="") 

if __name__ == "__main__":
    main()"""
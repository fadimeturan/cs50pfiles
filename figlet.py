import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(fonts))

elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fonts:
    figlet.setFont(font=sys.argv[2])

else:
    sys.exit("invalid")    


my_input = input("Input: ")
print(figlet.renderText(my_input))


"""print(f"Output: ", figlet.renderText(my_input))

"""
#cmd olarak yazarken dosyanın adını da giriyoruz ya, liste şeklinde olduğu için, dosya adı zero oluyor

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if  6>= len(s)>= 2:
        if s.isalpha():
            return True
        elif s.isalnum() and s[0:2].isalpha():
            for i in s:       
                if i.isdigit():
                    place= s.index(i)
                    if s[place:].isdigit() and int(i) != 0:
                        return True
                    else:
                        return False

        for p in s:
            if p in [".", ",", "?", "!", "*", "-"]:
                return False

    

if __name__ == "__main__":
    main()

"""
    şimdi karakter sayısı 2-6 arası, alphanumeric ve il ikisi kesinlikle str olacak dedik
    sonra içerideki charakter digitse yani sayısal gidiyorsa 1 noktadan sonra, ilk sayı 0 olamaz dedik
"""
    



# check50 cs50/problems/2022/python/nutrition


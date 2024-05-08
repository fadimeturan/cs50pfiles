import validators

def main():
    email = input("What's your email address? ")
    format = validators.email(email)

    if format == True:
        print("Valid")
    else:
        print("Invalid")
 

if __name__ == "__main__":
    main()
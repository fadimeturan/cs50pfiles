from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    birth_day = input("Date of Birth: ")
    try:
        result = check(birth_day)
        if result is not None:
            print(result.capitalize() + " minutes")
        else:
            print("Invalid date")
    except ValueError:
        sys.exit("Invalid date")



def check(birth_day):
    try:
        the_date = date.fromisoformat(birth_day)
        the_today = date.today()
        total_day = the_today - the_date
        total_min = total_day.days *24 *60
        output = p.number_to_words(total_min, andword="")
        return output

    except ValueError:
        raise ValueError("Invalid date")


if __name__ == "__main__":
    main()

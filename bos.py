import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    match = re.search(r"^([0-9]|1[0-2])?(:[0-5][0-9])? ?(AM|PM).to.([0-9]|1[0-2])?(:[0-5][0-9])? ?(AM|PM)$", s, re.IGNORECASE)
    if match:
        num = match.groups()
        if int(num[0]) > 12 or int(num[3]) > 12:
            raise ValueError
        before = clock(num[0], num[1], num[2])
        after = clock(num[3], num[4], num[5])
        return f"{before} to {after}"
    else:
        raise ValueError

def clock(hour, minute, time):
    if time == "PM":
        if int(hour) == 12:
            my_hour = 12
        else:
            my_hour = int(hour) + 12
    else:
        if int(hour) == 12:
            my_hour = 00
        else:
            my_hour = int(hour)
    if minute:
        my_minute = minute[1:]  # ":" karakterini atlayarak dakika kısmını alıyoruz
    else:
        my_minute = "00"
    return f"{my_hour:02}:{my_minute}"

if __name__ == "__main__":
    main()

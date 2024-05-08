import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>", s):
        match = re.search(r"(https?):\/\/(www\.)?youtube\.com\/embed\/([a-zA-Z0-9_]+)", s)
        if match:
            url = match.group(3)
            return "htpps://youtube/" + url
           


if __name__ == "__main__":
    main()
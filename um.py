import re

def main():
    print(count(input("Text: ")))

def count(s):
    match = r"\bum\b"
    output = re.findall(match, s, re.IGNORECASE)
    return len(output)

if __name__ == "__main__":
    main()

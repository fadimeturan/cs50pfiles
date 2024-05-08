from twttr import shorten

def main():
    test_lowercase()
    test_uppercase()
    test_number()

def test_lowercase():
    assert shorten("rory") == "rry"
    assert shorten("birtanem") == "brtnm"
    assert shorten("lolipop") == "llpp"
    assert shorten("delidana") == "dldn"

def test_uppercase():
    assert shorten("MARY") == "MRY"
    assert shorten("FRoNCE") == "FRNC"
    assert shorten("LONDON") == "LNDN"
    assert shorten("ISTANBUL") == "STNBL"

def test_number():
    assert shorten("23123") == "23123"

if __name__ == "__main__":
    main()

"""   ,"A","E","I","O","U"
 """
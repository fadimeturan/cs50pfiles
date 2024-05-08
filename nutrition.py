
input = input("Item: ").lower()

fruits = {
    "apple" : 130,
    "avocado" : 50,
    "kiwifruit" : 90,
    "pear" : 100,
    "sweet cherries" : 100
}

if input in fruits:
    print("Calories:", fruits[input])




fruit = input("Item: ")

if fruit == "apple":
    print("Calories: 130")


if fruit == "Avocado":
    print("Calories: 50")

if fruit == "Kiwifruit":
    print("Calories: 90")

if fruit == "pear":
    print("Calories: 100")

if fruit == "Sweet Cherries":
    print("Calories: 100")
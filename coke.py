

amount = 50

while amount > 0:
    print("Amount Due:", amount)
    
    coin = int(input("Insert Coin: "))  
    
    if coin in [5, 10, 25]:
        amount -= coin

owe = abs(amount)
print("Change Owed:", owe)

print(amount)
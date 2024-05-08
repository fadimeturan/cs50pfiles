import json
import requests
import sys

if len(sys.argv) == 2:
        try:
            number = float(sys.argv[1])
             
        except:
            print(f"command-line argument is not a number")
            sys.exit(1)
else:
    print("Missing command-line argument") 
    sys.exit(1)  


try:
     r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
     result = r.json()
     bitcoin = result['bpi']['USD']['rate_float']
     amount = bitcoin * number
     print(f"${amount:,.4f}")



except requests.RequestException:
     print("RequestsException")
     sys.exit(1)
     

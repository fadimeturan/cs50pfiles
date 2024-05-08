"""
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    
    try:

        date = input("Date: ").title()
    
        month,day,year = date.split("/")
        if 1<= int(month) <=12 and 1<= int(day) <= 31:
            break
    except:
        try:     #iki senaryo olduğu için iç içe try except kullanabiliriz
            month2, day2, year = date.split("")
            month= months.index(month2) +1  #jnuary 0 olarak indexli ama tarihte 1. ay olmali o yüzden +1
            
            if not day2.endswith(","):
                    continue
            day = day2.replace(",","")        

            if 1<= int(month) <=12 and 1<= int(day) <= 31:
                    break

        except:
            print()
            pass

print(f"{year}-{int(month):02}-{int(day):02}")  #02 formülü 7 yerine 07 olarak görünsün diye ay veya gün  

"""



months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
     try:
            date = input("Date: ").title()
             
            if "/" in date:
                month,day,year = date.split("/")
                if 1<= int(month) <=12 and 1<= int(day) <= 31:
                    break



            elif "," in date:
                  month, day, year = date.split()
                  day = day.strip(",")
                  
                  if month in months:
                      month = months.index(month) + 1
                      if 1<= int(month) <=12 and 1<= int(day) <= 31:
                        break

            else:
                 print()
                 continue    

     except ValueError:
          continue
        

print(f"{year}-{int(month):02}-{int(day):02}")
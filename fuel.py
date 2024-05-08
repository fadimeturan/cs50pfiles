
def main():
    fraction = input("Fraction: ")
    my_fraction = convert(fraction)
    output = gauge(my_fraction)
    print(output)
    
    
def convert(fraction):
    while True:
        try:
            my_x , my_y = fraction.split("/")
            x = int(my_x)
            y = int(my_y)
            
            f = x/y    #her şeyi tek tek def gerekiyor, mesela kesir fonksiyonu yok o zaman sen tanımlıyorsun, yüzde fonksiyonu yok""
            if f <= 1:
                p = int(f * 100)
                return p
            else:
                fraction = input("Fraction: ")
                pass
                
        except (ValueError, ZeroDivisionError ):   #try except yapıp funcion olağan akışını sonradan ekliyoruz, print kısmını
            raise
    
def gauge(percentage):   #round yaparsak daha iyi olabilir 
    if percentage >= 99:
       return("F")
    elif percentage <=1:
       return("E")
    else:
       return(f"{percentage}%")   # (str(percentage) +"%")

if __name__ == "__main__":
    main()
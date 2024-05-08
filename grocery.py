#check50 cs50/problems/2022/python/

grocery_list = {}         #terminalde oluşturmuş oluyruz aslında

while True:
    try:
        food = input()   #output upper istendiği için canim
        if food in grocery_list:          #burada da aslında saymaya başlıyor ve o sayı dictin key'i oluyor
            grocery_list[food] += 1
        else:
            grocery_list[food] = 1
            
    except EOFError:
        for key in sorted(grocery_list.keys()):
            print(grocery_list[key], key)  
        break 
        
#keyler numara, keyin karşılığı grocories oldu yani"""
            
#ctrl z yapinca ^z yazacak, sonra enter deyince output geliyor

    
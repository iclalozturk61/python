# Creating a Function
#Benefits: We can save lines of code if function is large
#One source of truth. No repeat of code. Need changes?
#update one spot
#Can improve code readability

def greet(): # bu şekilde tanımlanır
    print("merhabalar")
    print("iclal \n")    

greet()
greet()
greet()
greet()

#Arguments and Parameters YARIM KALDI
def greet(name): #bunun adı parameters fonksyonun aldığı şeydir (parameters are the variables on the inside of the function)
    print("merhabalar" , name , "argüman örneğidir")

greet("iclal") #bunun adı arguments fonksyona verdiğimiz şeydir (arguments you pass the things)

#return break gibi ama o döngüler için kullanılır bunu fonksyonlar için kullanılır. Fonksyonun içinde döngü varsa break ve continue kullanılabilir ama direk fonksyon içnde kullanılamaz
def greet(name):
    if name == "fellas":
        print("1. return çıktısı")
        return 
    print("fonksyonun içindeki asla okunmayacak şeyler")
    
greet("fellas")

#return vs else to Exit Function: ikisi de olur ama okunabilirlik ve basitlik gereği return bence daha iyi
def greet(name):
    if name == "fellas":
        print("1. else ile çıkıldı")
     
    else: 
        print("fonksyonun içindeki asla okunmayacak şeyler")
    
greet("fellas")

#NOT: aynı dosya içinde aynı isimle iki fonksyon üretilirse python öncekileri geçersiz kılar sadece sonuncuyu önemser

#How to Return a Value from Function
def greet_2(name):
    if name == "hatice":
        return "oo nabıyon lan " + name #bu şekilde returne değer verilir
    return "merhabalar greet_2 çıktısı " + name 

returned = greet_2("iclal") #bu şekilde kullanılır
print(returned)
print(greet_2("hatice"))

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
def greet(name): #bunun adı parameters ()
    print("merhabalar" , name)

greet("iclal") #bunun adı arguments ()
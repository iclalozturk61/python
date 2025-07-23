print(16/2) #8.0 yazar 
print(5 + 3) #8 yazar
print( (6*2) + (8 /4) - 1) # bazen gerek olmasa bile görünüşü basitleştirmek için parantez kullanılabilir
print((((5 + 5)))) #fazla parantezler sorun çıkarmaz

"""" bu şekilde çoklu yorum satırı yazılabiliyor
round fonksyonu hakkında: bankacı yuvarlaması (banker's rounding) fonksyonudur: eğer yuvarlanacak sayı 5 ile bitmiyorsa 
sıkıntı yok normal matematikteki kurallar uygulanır ama 5 ile bitiyorsa en yakın çift sayıya yuvarlanır.
"""
yuvarlama = round(2.5) #normalde 3 e yuvarlanması gerekiyordu ama 2 çift o yüzden 2 ye yuvarladı
print(yuvarlama)
round(2.344, 2)  # → 2.34 , virgülden sonra gelen rakam noktadan sonraki kaç basamak saklanacak şekilde yuvarlanacağını işaret eder
round(2.345, 2)  # → 2.34  → çünkü 0.345 en yakın çift olan 0.34’e gider
round(2.355, 2)  # → 2.36  → çünkü 0.355 en yakın çift olan 0.36

import math
print(math.ceil(3.3)) #yukarıya yuvarlar
print(math.floor(3.6)) #aşağıya yuvarlar

print(5+5, 'hey', 10.3) #print farklı türleri aynı anda basabilir
print('hi', end= " ") #end komutu şunu yapar "" arasındakini yazar ama imleci alt satıra geçirmez
print('selam')


#variable naming rules
age1 = 1 #GOOD
age_of_users = 2 #GOOD
#age-3=3 #NOT GOOD
#4age = 4 #NOT GOOD
ag5e = 5 #GOOD
Age = 6 #NOT RECOMMENDED
#return = 5 #NOT GOOD it is keyword


# Floor Division (Double Forward Slash)
result = 10 / 3   # / --> float division 
print(result)   # // --> integer division

new_result = 10 // 3  #// math.floor() un işini yapıyor virgülden sonrasını atıyor
print(new_result)

#modulus
pizza = 10
people = 3
print('left over', 10 % 3) # % kalan bulma operatörüdür

#Raising Numbers to a Power
print(3 * 3 * 3)
print(3 ** 5) # ** üs işlemleri için kullanılıyor
result1 = math.pow(3 , 5) # birinci sayının ikinci sayı üssünü alır
print(result1)
#**********************STRING************************
# #escape characters
print("Hello\nI\'m iclal\töztürk\rhey")
print("\x3A") #hexadecimal karakter numarası böyle verilir

print(r"merhabalar \t selam \n hehe") #Raw string: başa konan r ile escape characterlere bakılmaz ne yazdıysan kabul edilir 
#Double vs Single Quotes
print("annem 'iki ekmek al' dedi") #olur
print('annem "iki ekmek al" dedi') #olur
# print('annem 'iki ekmek al' dedi') olmaz
# print("annem "iki ekmek al" dedi") olmaz


#concenation = expectin 1 argument "eğer birleştirmek gibi"
msg1 = "selam"
msg2 = "iclal"

print(msg1, msg2) #seperate arguemts
print(msg1 + " " + msg2) #concenation 
print("hey" "there")

msg3 = ("uzuuuuun bir string"
"devam ediyor") #parantezi koymasaydım ikinci satırı görmezdi
print(msg3)
msg4 = "slm"
print(msg4 + "aleykum") #araya ya virgül ya da + koymak gerekiyor

#Multiline Strings (Three Double Quotes) = yanyana yazmasın alt satıra geçmelere saygılı olsun siye böyle yapılıyor.
#alt satıra geçmesini istemediğimizde \ koyuyoruz

poem = """Ağlasam sesimi duyar mısınız,
Mısralarımda;
Dokunabilir misiniz,
Gözyaşlarıma, ellerinizle?

Bilmezdim şarkıların bu kadar güzel,
Kelimelerinse kifayetsiz olduğunu
Bu derde düşmeden önce.

Bir yer var, biliyorum; \
Her şeyi söylemek mümkün;\
Epeyce yaklaşmışım, duyuyorum; \
Anlatamıyorum."""

print(poem)

#Slicing Strings 
sentence = "where am I?"
#           012345678910
#      -li: 10987654321
print(sentence[3:]) #3. dahil
print(sentence[:3]) #3. dahil değil

#Negatives with String Slicing
print(sentence[-4:]) #sondan 4. karakterden başlıyor ileri doğru (4. dahil)
print(sentence[:-7]) #sondan 7. karakterden öncesini yazdrıyor (7.dahil değil)

#Slicing with Two Numbers
print(sentence[6:8]) #6. dahil 8 dahil değil
print(sentence[6:-3]) #6. dahil -3. dahil değil
start_number = 6
print(sentence[start_number:start_number + 3]) #değişken kullanımına izin var

#Strings are Immutable : Bir string oluşturulduktan sonra, içeriği değiştirilemez., bir değişiklik yapılması durumunda
#başka değişken oluşturulur, bu değişkenin korunması konusunda fayda sağlar
task = "Substring"
print(id(task)) #id fonksyonu değişkenin bellekte nerede tutulduğuna dair bilgi verir

#task[0] = 's' #type error verir çünkü değiştirilemez

task = "Like"
print(id(task)) #id lerini farklı olması da bunun kanıtı

#length fonksion
print(len(task)) #uzunluğunu yazar hep index numarasının bir eksiğini yazar

#Convert Integer to String (Concat int and str)
msg5 = "please subscribe"
print("your message was " + str(len(msg5)) + " characters long") #str() fonksyonu ile dönüştürmek lazım yoksa erorr verir 
print("your message was " , len(msg5) , " characters long") #bu şekilde erorr vermez çünkü conconation yapmıyor
#list
ages = [1,2,3]
people = ["hatice", "beyza" , "zeynep" , "feyza"]
my_favorite_things = ["friends" , 7 , ['tabi' , 'netflix' , 'youtube']]
print(id(my_favorite_things))

my_favorite_things[0] = "how I met your mother"
print(id(my_favorite_things)) #aynı id yi veriyor çünkü listler mutabledır. Elemanları değiştirilebilir başka yeni oluşturmaya gerek yok.

print(len(my_favorite_things)) #kendi içindeki diğer listeleri de bir saydığı için 3 eleman

#How to Copy a List (Slicing and copy Function)
print(my_favorite_things[:]) #bu şekilde bütün elemanlarına erişip yazdırabiliyoruz

copy1 = my_favorite_things[:] #bu şekilde tanımlayınca  my_favorite_things değişikliklerden etkilenmiyor
copy1[0] = "the mentalist" 

print(copy1 , my_favorite_things) 

copy2 = my_favorite_things #bu şekilde tanımlayınca  my_favorite_things değişikliklerden etkileniyor
copy2[0] = "the big bang teori" #çünkü bu tanımlama "alias" takma ad koyma olarak biliniyor, aynı şeye farklı bir isimle refere ediyorsun 

print(copy2 , my_favorite_things)

copy3 = my_favorite_things.copy() #copy fonksyonu kopyalama yapar my_favorite_things değişklerden etkilenmez
copy3[0] = "gassal"

print(copy3 , my_favorite_things)

#Intro to Nested Lists (2D Lists)
my_favorite_things = ["friends" , 7 , ['tabi' , 'netflix' , ['youtube' , 'instangram']]]
print(my_favorite_things[2][2][0]) #liste içindeki listeye böyle erişiyoruz
print(len(my_favorite_things))
print(len(my_favorite_things[2]))
print(len(my_favorite_things[2][2]))

#How to Deep Copy a List (copy.deepcopy)
copy4 = my_favorite_things.copy() #copy() fonksyonu immutable değerlerini kopyalar ama mutable değerler için alias(takma ad koyma) yapar
copy4 [2][1] = "disney plus" #eriştiğimiz değer bir liste olduğu içn alias yapacak

print(copy4 , my_favorite_things) 

import copy
copy5 = copy.deepcopy(my_favorite_things) #copy.deepcopy() fonsyonu yeni bir liste oluşturup bütün değerleri kopyalar.
#immutable veya mutable olmasına bakmaz ama yenii bir liste oluşturduğu için bellekte fazla yer kaplar
copy5[2][1] = "blu tv"
print(copy5 , my_favorite_things)

#Combining Lists (Concatenation for Lists)
least_favorite_things = ["tyt biyoliji" , "altyazısız bölümler"]
print(my_favorite_things + least_favorite_things) #böyle birleştirme yapılabiliyor

least_favorite_things = least_favorite_things + ["mantar"] #böyle ekleme yapılabiliyor
least_favorite_things.append("rush hour") #böyle de ekleme yapılabiliyor bu daha öneriliyor 
print(least_favorite_things)
#Getting User Input
""""
print("give us a number:")
number1 = input()
print("another:")
number2 = input()
print(number1 + number2) #örn: 8+10=810 yazıyor çünkü input string türünde dönüyor retun olarak
"""

#Type Casting
print(type(int("5"))) #type komutu değişkenin hangi veri tipinde olduğunu verir

""""
print("what is your favorite number?")
fav_num1 = int(input()) #inte çevirerek 199.satırdaki sorunu çözeriz, input direk string alır
print("other?")
fav_num2 = int(input())
print(fav_num1 + fav_num2)
print("any decimal?")
fav_num3 = float(input())
print(str(fav_num1) + "+" + str(fav_num2) + "=" + str(fav_num1 + fav_num2)) #str() siz olmazdı print kendi içinde string ve int değişkenlerini toplayamaz
print(fav_num1 + fav_num2 + fav_num3) #float ve int değerleri için hata vermez
"""





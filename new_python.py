a = "yigiter family"

for i in a:
  print(i)

print(True and False or True or not True)

#  CLASS oluşturma

class calisan:
  def __init__(self, name, surname, age):
    self.name = name
    self.surname = surname
    self.age = age
calisan1 = calisan("Ali", "Yazar", 42)
print(calisan1.name, calisan1.surname, calisan1.age)

##  ŞİMDİ CLASS IMIZA METOD EKLEYCEĞİZ.  ----

def show_info(self):
  print(f"Ad : {self.namw} Soyad : {self.surname} Yaş : {self.age})
      
calisan1.show_info()
        
calisan.show_info(calisan1)  # BU ŞEKİLDE DE ÇAĞIRABİLİRİZ.

Laambda map() = map(function, iterable)
iterable = (1, 2, 3, 4, 5, 6)
map(lambda x: x**2, iterable)
result = map(lambda x: x**2, iterable)
print(list(result))
print(list(map(lambda x: x**2, iterable)))  # çıktı yukarıdaki ile aynı olur.

## LAMBDA İLE FİLTER FONKSİYONU 
        
filter(function, sequence)
## ÖĞELERİN DOĞRU OLUP OLMADIĞINI İŞLER TEST EDER.
FOR İNSTANCE:
first_ten = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
even = filter(lambda x: x % 2 == 0, first_ten)
        print("Even numbers are : ", list(even))

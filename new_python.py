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


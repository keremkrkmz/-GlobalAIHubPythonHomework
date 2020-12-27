import random

ad = input("Adınızı giriniz : ")
soyAd = input("Soyadınızı giriniz : ")
i=0
while i<3:
    Check_ad = input("Öğrencinin Adı : ")
    Check_soyAd = input("Öğrencinin Soyadı : ")

    if Check_ad == ad.lower() and Check_soyAd==soyAd.lower():
        print("Hoşgeldin {} {}".format(ad,soyAd))
        break
    else:
        print("Hatalı giriş lütfen daha sonra tekrar deneyiniz!")
        i+=1
        if(i==3):
            print("Daha sonra tekrar deneyiniz.")
            exit()
    
dersler=[]
secilenDersler=[]        

for i in range(5):
   ders=input("Bu dönemki ders listenizi giriniz: ")
   dersler.append(ders)
   i+=1
print(dersler)

print("Seçebileceğiniz dersler : ")
        
for i in range(len(dersler)):
    print("{}.{}".format(i+1,dersler[i]))
print("-"*20)
        
dersSayisi=int(input("Kac ders almak istiyorsunuz? :"))
if dersSayisi<3 or dersSayisi>5:
    print("en az 3 en fazla 5 ders seçebilirsiniz. Sınıfta kaldınız :)") 
    exit()
else:
    for i in range(dersSayisi):
        ders=input("{}.dersinizin ismini yazınız :".format(i+1))
        secilenDersler.append(ders)

print("aşağıdaki kursları aldınız.")
for i in range(dersSayisi):
        print("{}.{}".format(i+1,secilenDersler[i]))
        
print("Sınava girmek istediğiniz dersi seciniz: ")

for i in range(len(secilenDersler)):
    print("{}.{}".format(i+1,secilenDersler[i])) #buraya bir daha bak

print("-"*20) 

while True:
    ders=(input("Sınava girmek istediğiniz dersin adını giriniz :"))
    if ders in secilenDersler:
        vize=random.randint(0,100)
        final=random.randint(0,100)
        proje=random.randint(0,100)
        
        gecmeNotu=vize*0.3+final*0.5+proje*0.2
        print("Ders durum bilgileriniz: ")
        print("Vize Notu : ",vize)
        print("final Notu : ",final)
        print("Proje Notu : ",proje)
        print("gecme notunuz : ",gecmeNotu)
        
        if gecmeNotu > 90:
            print("HArf Notunuz : AA - Gectiniz.")
        elif 70 < gecmeNotu < 90:
             print("Harf Notunuz : BB - Gectiniz. ")
        elif 50 < gecmeNotu < 70:
            print("Harf Notunuz : CC - Gectiniz. ")
        elif 30 < gecmeNotu < 50:
            print("Harf Notunuz : DD - Gectiniz.")
        elif gecmeNotu < 30:
            print("Harf Notunuz : FF - Dersten kaldınız.")
                
        break
    else:
        print("Ders listenizde {} isimli bir ders yok  ".format(ders))
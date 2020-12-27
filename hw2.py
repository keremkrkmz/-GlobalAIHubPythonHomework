ad= input("Adınız : ")
soyAd= input("Soyadınız : ")
yas=int(input("Yaşınız : "))
dtarihi=int(input("Doğum tarihiniz(yıl) : "))

bilgiler=[ad, soyAd,yas,dtarihi]
yazılar=["Adı :","Soyadı: ","yaşı :","Doğum Tarihi :"]


for i in range(len(bilgiler)):
    print("{} {}".format(yazılar[i],bilgiler[i]))
    i+=1
print("\n")

if yas>18:
      print("Dışarı çıkabilirsin")
else:
      print("Dışarı çıkamazsın çünkü tehlikeli!!!")

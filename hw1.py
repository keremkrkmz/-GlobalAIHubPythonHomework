print("Başvurunuz için aşağıdaki bilgileri doldurunuz:")
print("\n")
adSoyad= input("Adınız ve Soyadınız : ")
yas=int(input("Yaşınız : "))
uni=input("Mezun olduğunuz okul : ")
blm=input("Bitirmiş olduğunuz bölüm : ")
maas=int(input("Beklediğiniz maaş miktarı : "))

print("\n")
print("Girmiş olduğunuz bilgiler aşağıdaki gibidir:")

bilgiler=[adSoyad,yas,uni,blm,maas]
yazılar =["Ad Soyad : ","Yaşınız: ","Mezun olduğunuz universite: ","Bitirmiş olduğunuz bölüm: ","istediğiniz maaş miktarı: "]

for i in range(len(bilgiler)):
    print("{} {} --> veri tipi : {}".format(yazılar[i],bilgiler[i],type(bilgiler[i])))
    i+=1
    


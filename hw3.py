from random import randint

rnd_sayi=randint(1,100)
tahminHakki=0

while True:
    g_sayi=int(input("Lütfen 1-100 arasında bir sayı giriniz : "))
    tahminHakki+=1
    if g_sayi==rnd_sayi:
        print("Bravo sayıyı doğru bildiniz")
        break
    elif g_sayi<rnd_sayi:
        print("daha büyük bir sayı denemelisiniz.. ")
    elif g_sayi>rnd_sayi:
        print("daha küçük bir sayı denemelisiniz..")    
    else:
        print("gecerli bir sayi giriniz.") 
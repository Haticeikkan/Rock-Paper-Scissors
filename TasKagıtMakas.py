import random

secenek = ["Taş", "Kağıt", "Makas"]
Taş = secenek[0]
Kağıt = secenek[1]
Makas = secenek[2]

print(
    "Taş Kağıt Makas Oyununa Hoşgeldiniz :) \nOyunu Bitirmek için X harfine basabilirsiniz..."
)

while True:
    secim = input("Taş / Kağıt / Makas seçeneklerinden birini seçerek oynayabilirsiniz. \nSizin seçiminiz: ")
    pc_secim = random.choice(secenek)

    if secim == Taş:
        if pc_secim == Taş:
            print("Bilgisayarın Seçimi: Taş \nOyun Berabere Sonuçlandı...")
        elif pc_secim == Kağıt:
            print("Bilgisayarın Seçimi: Kağıt \nBilgisayar Oyunu Kazandı...")
        else:
            print("Bilgisayarın Seçimi: Makas \nOyunu siz kazandınız...")
    elif secim == Kağıt:
        if pc_secim == Taş:
            print("Bilgisayarın Seçimi: Taş \nOyunu siz kazandınız...")
        elif pc_secim == Kağıt:
            print("Bilgisayarın Seçimi: Kağıt \nOyun Berabere Sonuçlandı...")
        else:
            print("Bilgisayarın Seçimi: Makas \nBilgisayar Oyunu Kazandı...")
    elif secim == Makas:
        if pc_secim == Taş:
            print("Bilgisayarın Seçimi: Taş \nBilgisayar Oyunu Kazandı...")
        elif pc_secim == Kağıt:
            print("Bilgisayarın Seçimi: Kağıt \nOyunu siz kazandınız...")
        else:
            print("Bilgisayarın Seçimi: Makas \nOyun Berabere Sonuçlandı...")
    elif secim == "X":
        print("Oyundan çıkış yapılıyor")
        break

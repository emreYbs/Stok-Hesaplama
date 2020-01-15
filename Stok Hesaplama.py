#  EmreYbs 29 Kasım 2019, Ödev

# İşletmeler için Basitçe DönemSonu Ortalama Stok Miktarını Gösteren Python kodları
'''
                    .-"""-.
                   / .===. \
                   \/ 6 6 \/
                   ( \___/ )
  _____________ooo__\_____/_________________
 /                                          \
| İşletmeler için Ortalama Stok Hesaplama |
 \__________________________ooo_____________/
                   |  |  |
                   |_ | _|
                   |  |  |
                   |__|__|
                   /-'Y'-\
                  (__/ \__)



# Önce fonkisyonları tanımlarız. Sonra da değişkenleri
'''


def donemBasi(ks, ys, ds):
    global donemBasiS
    donemBasiS = ks + ys + ds
    print("Dönem başındaki stok miktarınız:", donemBasiS)
    return donemBasiS


def müsteriGirisi(donemBasiS, eklenenKs, eklenenYs, eklenenDs):
    global girilenStok
    girilenStok = donemBasiS + eklenenKs + eklenenYs + eklenenDs
    print("Dönemiçi Stok miktarınız:", girilenStok)
    return girilenStok


def donemSonuStok(girilenStok, dusenKs, dusenYs, dusenDs):
    global donemSonuStok
    donemSonuStok = girilenStok - (dusenKs + dusenYs + dusenDs)
    print("Dönem sonunda stok miktarınız: ", donemSonuStok)
    return donemSonuStok


def ortalamaStok(donemBasiS, donemsonuStok):
    ortalamaStok = (donemBasiS + donemsonuStok) / 2
    print("Ortalama stok miktarınız: ", ortalamaStok)
    return ortalamaStok



eklenenKs = int(input("Stoğa eklenecek koltuk adedini giriniz:"))
eklenenYs = int(input("Stoğa eklenecek yatak adedini giriniz:"))
eklenenDs = int(input("Stoğa eklenecek dolap adedini giriniz:"))

dusenKs = int(input("Stoktan düşülecek koltuk adedini giriniz:"))
dusenYs = int(input("Stoktan düşülecek yatak adedini giriniz:"))
dusenDs = int(input("Stoktan düşülecek dolap adedini giriniz:"))

ilkStok = donemBasi(ks=1250, ys=850, ds=350)
girilenStok = müsteriGirisi(donemBasiS, eklenenKs, eklenenYs, eklenenDs)
sonStok = donemSonuStok(girilenStok, dusenKs, dusenYs, dusenDs)
ortalamastok = ortalamaStok(donemBasiS, donemSonuStok)
ortalamastok = ortalamaStok(donemBasiS, donemSonuStok)



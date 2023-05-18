import magaza

data={}
magaza=magaza.magaza()
while True:
    islem=int(input("Bir satışa ait bilgiler girmek icin 1'i ,  mağazaların ve satıcıların her biri için toplam satış tutarlarını görmek için 2'yi tuslayınız :"))

    if islem==1:

        magaza_adi=input("Magaza adını giriniz:")
        satıcı_adi=input("Satıcı adını giriniz:")
        satıcı_cinsi=input("Satıcı cinsini giriniz:")
        tutar=int(input("Satış tutarını giriniz:"))

        magaza.mutator(magaza_adi,satıcı_adi,satıcı_cinsi)

        dictkey=magaza_adi+"_"+satıcı_adi

        try:
            data[dictkey]+=tutar
        except KeyError:
            data[dictkey]=tutar

    elif islem==2:
        break
    else:
        print("Gecersiz bir islem girdiniz. Lütfen tekrar deneyiniz.")


mydict=magaza.magaza_satis_tutar(data)
print(magaza)
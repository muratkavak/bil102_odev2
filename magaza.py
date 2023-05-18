class magaza():
    def __init__(self):
        self.__magaza_adi=str()
        self.__satıcı_adi=str()
        self.__satıcı_cinsi=str()

    def accessor(self):
        data=self.__magaza_adi+self.__satıcı_adi+self.__satıcı_cinsi
        return data
    def mutator(self,magaza_adi,satıcı_adi,satıcı_cinsi):
        self.__magaza_adi = magaza_adi
        self.__satıcı_adi = satıcı_adi
        self.__satıcı_cinsi = satıcı_cinsi

    def magaza_satis_tutar(self,mydict):
        fiyatlar=dict()
        for i in mydict.items():
            j=i[0].split("_")
            try:
                fiyatlar[j[0]] += int(i[1])
            except KeyError:
                fiyatlar[j[0]] = int(i[1])
            try:
                fiyatlar[j[1]] += int(i[1])
            except KeyError:
                fiyatlar[j[1]] = int(i[1])
        self.sonuc=str()
        for i in fiyatlar.items():
            for j in i:
                self.sonuc+=str(j)+":"
            self.sonuc+="\n"

    def __str__(self):
        return self.sonuc


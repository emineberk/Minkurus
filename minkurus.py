def min_Kurus(tutar, kuruslar, bulunanDegerler={}):
    
    if tutar in bulunanDegerler:  # Tutarın önceki bulunan değerler arasında olup olmadığı kontrol ediliyor
        return bulunanDegerler[tutar]
    elif tutar in kuruslar:  # Tutarın kuruşlardan biri olup olmadığı kontrol ediliyor
        bulunanDegerler[tutar] = [tutar]
        return [tutar]
    elif min(kuruslar) > tutar:  #Kuruşların en küçüğü tutardan büyükse sonuç dönme
        bulunanDegerler[tutar] = []
        return []
    else:
        minKurus = []  # Değer bulunamazsa boş dönmesi için.
        for kurus in kuruslar:  # tüm kuruş değerleri kontrol ediliyor
            results = min_Kurus(tutar - kurus, kuruslar, bulunanDegerler=bulunanDegerler)  # içiçe dönerek tutar için 
            if results and (not minKurus or (1 + len(results)) < len(minKurus)):  # eğer fonksiyondan sonuç dönüyorsa ve (minKurus boşsa yada dönen sonuç minKurus değişkenini eleman sayısından küçükse)
                minKurus = [kurus] + results
        bulunanDegerler[tutar] = minKurus  # tekrar kontrol etmek için bulunan degeri listeye ekle
    return bulunanDegerler[tutar]
try:    
    tutar =  float(input("Bir Tutar Giriniz:"))#Parametresi ile bir tutar alıyor
    kuruslar = [0.01, 0.05, 0.10,0.25,0.50]#Bozukluklar kuruş cinsinden  kayıt ediliyor
    degerler = min_Kurus(tutar ,kuruslar)#Fonksiyon çağrılıyor 
    print(tutar,len(degerler),degerler)#Bulunan değerler print ediliyor
    
except ValueError:#Hataya düşerse girmesi sayısal değer girilmmemiştir
    print("Lütfen bir sayı giriniz!!!!?")
    

from itertools import islice,takewhile
from uzay_oyunu.akis import fibonacci,yakit_gostergesi,satirlari_oku,ayristir,uzun_yolculuklar,rota_sayaci
from uzay_oyunu.istatistik import buyuk_harf_map,coklu_baglanti_filter,toplam_baglanti_reduce,hizli_yolculuk
#-----GÖREV 1 TEST------------------------------------------------------------------
def test_fibonacci():
    g=fibonacci()
    assert next(g)==0
    assert next(g)==1
    assert next(g)==1
    #İlk 12 deger
    assert list(islice(fibonacci(),12))==[0,1,1,2,3,5,8,13,21,34,55,89]
    #100 den küçük degerler
    assert list(takewhile(lambda x: x<100, fibonacci()))==[0,1,1,3,5,8,13,21,34,55,89]
    #Üretecin tek kullanımlık oldugunu test etme
    g2=fibonacci()
    ilk_bes=list(islice(g2,5))
    sonraki_bes=list(islice(g2,5))
    assert ilk_bes!=sonraki_bes #İkinci çagrı kaldıgı yerden devam eder
#-----GÖREV 2 TEST-------------------------------------------------------------------
def test_yakit_gostergesi():
    assert list(yakit_gostergesi(100,30))==[70,40,10,0]
#-----GÖREV 3 TEST-------------------------------------------------------------------
def test_boru_hatti():
    kayitlar=list(ayristir(satirlari_oku("veri/seyir.txt")))
    toplam_yakit=sum(y for _,_, y in kayitlar)
    assert toplam_yakit==88

    uzun_yol_kayitlari=ayristir(satirlari_oku("veri/seyir.txt"))
    hedef_gezegenler=[h for _, h,_ in uzun_yolculuklar(uzun_yol_kayitlari,10)]
    assert hedef_gezegenler==['sirius','centauri','orion','kara_delik']
#-----GÖREV 4 TEST------------------------------------------------------------------
def test_rota_sayaci():
    ornek_baglantilar={
        "dünya":["sirius","centauti"],
        "centauri":["orion"],
        "sirius":["orion","kara_delik"],
        "orion":["dünya"],
        "kara_delik":[]
    }
    say=rota_sayaci(ornek_baglantilar)
    assert say("dünya",0)==1
    assert isinstance(say("dünya",3),int)
#-----GÖREV 5 TEST----------------------------------------------------------------------------
def istatislikler():
    gezegenler=["dünya","centauri","sirius","orion","kara_delik"]
    baglantilar={
        "dünya":["sirius","centauti"],
        "centauri":["orion"],
        "sirius":["orion","kara_delik"],
        "orion":["dünya"],
        "kara_delik":[]
    }
    assert buyuk_harf_map(gezegenler)==['DÜNYA','CENTAURI','SIRIUS','ORION','KARA_DELIK']
    assert coklu_baglanti_filter(baglantilar)==['dunya','sirius']
    assert toplam_baglanti_reduce(baglantilar)==5
    assert hizli_yolculuk("dünya","sirius")=="dünya->sirius(Hiz:3)"

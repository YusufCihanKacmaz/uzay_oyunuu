from functools import reduce,partial
from typing import List,Dict
#Örnek galaksi verisi
galaksi_gezegenleri=["dünya","centauri","sirius","orion","kara_delik"]
baglanti_sozlugu={
    "dünya":["sirius","centauri"],
    "centauri":["orion"],
    "sirius":["orion","kara_delik"],
    "orion":["dünya"],
    "kara_delik":[]
}
#1.Gezegen adlarının buyuk harfli listesi (map vs liste üreteci)
def buyuk_harf_map(gezegenler:List[str])->List[str]:
    return list(map(str.upper,gezegenler))
#2.En az iki baglantısı olan gezegenler (filter)
def coklu_baglanti_filter(baglantilar:Dict[str,List[str]])->List[str]:
    return List(filter(lambda g:len(baglantilar[g])>=2,baglantilar.keys()))
#3.Toplam baglantı sayısı (reduce)
def toplam_baglanti_reduce(baglantilar:Dict[str,List[str]])->int:
    return reduce(lambda toplam, g:toplam+len(baglantilar[g]),baglantilar.keys(),0)
#4.partial (Kısmi uygulama) ornegi
def yolculuk_yap(kaynak:str,hedef:str,hiz:int)->str:
    return f"{kaynak}->{hedef} (Hiz:{hiz})"
#hizi sabit 3 olan yeni fonksiyon türetiyoruz
hizli_yolculuk=partial(yolculuk_yap,hiz=3)
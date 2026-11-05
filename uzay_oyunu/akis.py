from typing import Generator,Iterator,Tuple,Dict,List
from itertools import islice,takewhile
from functools import lru_cache

#-----GÖREV 1 ------------------------------------------------------------------------------
def fibonacci()->Generator[int,None,None]:
    #Sonsuz bir fibonacci dizisi üreten üreteç fonksiyonu
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
#-----GÖREV 2-------------------------------------------------------------------------------
def yakit_gostergesi(yakit:int,tuketim:int)->Generator[int,None,None]:
#Her adımda yakıtı tüketim kadar azaltıp kalan yakıtı üreten üretec
    while yakit>0:
     yakit=max(0,yakit-tuketim)
     yield yakit
     if yakit==0:
        break
#-----GÖREV 3-------------------------------------------------------------------------------
def satirlari_oku(yol:str)->Iterator[str]:
   #Dosyadaki bos ve # ile atlayarak satırları atlayarak satırları uretec olarak dondurur
   with open(yol,"r",encoding="utf-8") as f:
      for satir in f:
         temiz=satir.strip()
         if temiz and not temiz.startswith("#"):
            yield temiz
def ayristir(satirlar: Iterator[str])->Iterator[Tuple[str,str,int]]:
   #Her satırı (kaynak,hedef yakit) tuple donusturur
   for satir in satirlar:
      parcalar=satir.split("->")
      kaynak=parcalar[0].strip()
      hedef_ve_yakit=parcalar[1].strip().split
      hedef=hedef_ve_yakit[0]
      yakit=int(hedef_ve_yakit[1])
      yield(kaynak,hedef,yakit)
def uzun_yolculuklar(kayitlar:Iterator[Tuple[str,str,int]],esik:int)->Iterator[Tuple[str,str,int]]:
   #Yakıtı verilen esik degerinden buyuk olan kayıtları suzer
   for kaynak,hedef,yakit in kayitlar:
      if yakit>esik:
         yield(kaynak,hedef,yakit)
#-----GÖREV 4---------------------------------------------------------------------------------------------
def rota_sayaci(baglantilar: Dict[str,List[str]]):
   #Verilen baglantıları göre farklı rotaların sayısını hesapalayan önbellekli fonsksiyon döndürür
   @lru_cache(maxsize=None)
   def rota_sayisi(gezegen:str,adim:int)->int:
      if adim==0:
         return 1
      if gezegen not in baglantilar:
         return 0
      toplam=0
      for komsuluk in baglantilar[gezegen]:
         toplam+=rota_sayisi(komsuluk,adim-1)
         return toplam
      return rota_sayisi
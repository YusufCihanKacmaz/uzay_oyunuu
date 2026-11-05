
import time
from functools import wraps

def hamle_sayaci():
    """Her çağrıldığında artan bir sayaç closure'ı döndürür (nonlocal kullanır)."""
    sayac = 0
    def say():
        nonlocal sayac
        sayac += 1
        return sayac
    return say

def en_bagli_gezegenler(galaksi: dict) -> list[str]:
    """Gezegenleri bağlantı sayısına göre azalan, eşitlikte alfabetik sırayla döndürür."""
    baglantilar = galaksi.get("baglantilar", {})
    gezegenler = list(baglantilar.keys())
    return sorted(gezegenler, key=lambda g: (-len(baglantilar.get(g, [])), g))

def sure_olc(fonksiyon):
    """Bir fonksiyonun çalışma süresini ölçen ve yazdıran sarmalayıcı (decorator)."""
    @wraps(fonksiyon)
    def sarmalayici(*args, **kwargs):
        baslangic = time.time()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.time()
        print(f"[{fonksiyon.__name__}] Çalışma süresi: {bitis - baslangic:.6f} saniye")
        return sonuc
    return sarmalayici

# Bonus uygulama:
en_bagli_gezegenler = sure_olc(en_bagli_gezegenler)
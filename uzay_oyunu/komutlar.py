from functools import wraps
KOMUTLAR={}

def komut(ad,aciklama=""):
    """Fonksiyon degistirmeden KOMUTLAR sözlügüne kaydeder"""
    def dekorator(func):
        if ad in KOMUTLAR:
            raise ValueError(f"'{ad}' komutu zaten tanimli!")
        KOMUTLAR[ad]=(func,aciklama)
        @wraps(func)
        def wrapper(*args,**kwargs):
            return func(*args,**kwargs)
        return wrapper
    return dekorator
@komut("yardim","komutlari listeler")
def cmd_yardim(durum):
    cikis=[]
    for isim,(fonk,aciklama) in KOMUTLAR.items():
        cikis.append(f"{isim}:{aciklama}" if aciklama else isim)
    return "\n".join(cikis)
@komut("envanter","envanter esyalarini gösterir")
def cmd_envanter(durum):
    credits=durum.get("credits",0)
    engines=durum.get("engines",[])
    copilot=durum.get("copilot","Yok")
    return f"Credits: {credits},Motorlar: {engines},Yardimci Pilot:{copilot}"
@komut("harita","gidebilecegin gezegenleri gösteririr")
def cmd_harita(durum):
    baglantilar=durum.get("baglantilar",[])
    return", ".join(baglantilar)
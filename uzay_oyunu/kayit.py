
def gorev_kaydi(baslik: str, *adimlar: str, oncelik: str = "normal", **ekler: str) -> str:
    """Esnek parametreler alarak biçimlendirilmiş görev kaydı metni oluşturur."""
    sonuc = [f"[{oncelik.upper()}] {baslik}"]
    for i, adim in enumerate(adimlar, start=1):
        sonuc.append(f"{i}. {adim}")
    for anahtar, deger in ekler.items():
        sonuc.append(f" {anahtar}: {deger}")
    return "\n".join(sonuc)

if __name__ == "__main__":
    # Liste ve sözlük açarak çağırma örnekleri
    adimlar_listesi = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ek_bilgiler = {"sorumlu": "Ayşe"}
    
    print(gorev_kaydi("Kara deliğe atla", *adimlar_listesi, oncelik="YÜKSEK", **ek_bilgiler))
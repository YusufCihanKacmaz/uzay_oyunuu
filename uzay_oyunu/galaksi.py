
import json

def galaksi_kur(gezegenler: list[str], baglantilar: dict, baslangic: str, **kwargs) -> dict:
    """Galaksi haritasını ve başlangıç durumunu kurar."""
    if baslangic not in gezegenler:
        raise ValueError(f"Başlangıç gezegeni '{baslangic}' gezegenler listesinde bulunmuyor!")
    
    yakit = kwargs.get("yakit", 50)
    return {
        "gezegenler": gezegenler,
        "baglantilar": baglantilar,
        "konum": baslangic,
        "yakit": yakit
    }
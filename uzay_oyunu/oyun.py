from uzay_oyunu.araclar import hamle_sayaci 
def envanter_metni(credits:bool,engines:bool,copilot:bool)->str:
    #Envanterdeki ögelerin durumuna göre metin döndürür(saf fonksiyon)
    parcalar=[]
    if credits:
        parcalar.append("bol kredi")
    if engines:
        parcalar.append("saglam motor")
    if copilot:
        parcalar.append("yetenekli bir pilot")

    if not parcalar:
        return ""
    return "Sende : " + ",".join(parcalar)

def hedef_menusu(hedefler:list[str])->str:
    #Gidebilecek hedefleri numaralandirmis menü metni olarak döndürür (Saf fonksiyon)
    satirlar=["Nereye gitmek istersin?"]
    for i, hedef in enumerate(hedefler,start=1):
        satirlar.append(f"[{i}] {hedef}")
    return "\n".join(satirlar)

def travel(galaksi:dict)->None:
    #Uzay oyunu seyahat döngüsü yönetir.
    hamle_arttir=hamle_sayaci()
    konum=galaksi["konum"]
    yakit=galaksi["yakit"]
    baglantilar=galaksi["baglantilar"]

    while True:
        print(f"\nSu anki konumun:{konum} Yakit:{yakit}")
        hedefler=baglantilar.get(konum,[])
        if not hedefler:
            print("Gidebilecek baska yer kalmadi!")
            break

        print(hedef_menusu(hedefler))
        secim=input("Secimin (cikis icin q):")

        if secim.lower()=='q':
            break
        hamle_sayisi=hamle_arttir()

        try:
            secim_idx=int(secim)-1
            if 0<=secim_idx<len(hedefler):
                konum=hedefler[secim_idx]
                yakit-=10
            else:
                print("Gecersiz secim!")
        except ValueError:
            print("Lütfen bir sayi girin.")
        if yakit<=0:
            print("Yakit bitti! Oyun bitti.")
            break
    print(f"Oyunu {hamle_sayisi} hamlede bitirdin!")
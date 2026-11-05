from functools import lru_cache
import pytest
from uzay_oyunu.dekoratorler import hafiza,log_cagri,say,sinirla,sure_olc
from uzay_oyunu.komutlar import KOMUTLAR,cmd_envanter,cmd_harita,cmd_yardim,komut
#-----GÖREV 1 TEST-------------------------------------------------------------
def test_sure_olc(capsys):
    @sure_olc
    def topla(a,b):
        return a+b
    sonuc=topla(3,4)
    assert sonuc==7
    captured=capsys.readouterr()
    assert "topla:" in captured.out
    assert "sn" in captured.out
#-----GÖREV 2 TEST------------------------------------------------------------------
def test_say():
    @say
    def faktoriyel(n):
        if n<=1:
            return 1
        return n*faktoriyel(n-1)
    assert faktoriyel(5)==120
    assert faktoriyel.cagri>0
#-----GÖREV 3 TEST------------------------------------------------------------------
def test_log_cagri(capsys):
    @log_cagri
    def selamla(isim, unvan="Kaptan"):
        return f"Selam {unvan} {isim}"
    res=selamla("Ali",unvan="Amiral")
    assert res=="Selam Amiral Ali"
    captured=capsys.readouterr()
    assert "Selamla" in captured.out
#-----GÖREV 5 TEST-------------------------------------------------------------------
def test_sinirla():
    @sinirla(0,100)
    def yakit_harca(miktar):
        return 100-miktar
    assert yakit_harca(30)==70
    with pytest.raises(ValueError):
        yakit_harca(-10)
#-----GÖREV 4 TEST------------------------------------------------------------------
def test_komutlar_sistemi():
    durum={
        "konum":"dunya",
        "baglantilar":["orion","kara_delik"],
        "credits":500,
        "engines":["warp1"],
        "copilot":"Ayla",
    }   
    assert "yardim" in KOMUTLAR
    assert "envanter" in KOMUTLAR
    assert "harita" in KOMUTLAR

    assert "yardim" in cmd_yardim(durum)
    assert "500" in cmd_envanter(durum)
    assert "orion" in cmd_harita(durum)
def test_ayni_komut_tekrar_hata():
    with pytest.raises(ValueError):
        @komut("yardim")
        def mukerrer_komut(durum):
            pass
#------BONUS-----------------------------------------------------------------------
def test_hafiza_bonus():
    @hafiza(maxsize=2)
    def kare(x):
        return x*x
    assert kare(4)==16
    assert kare(5)==25
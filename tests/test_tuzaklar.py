
import pytest

def yakit_ekle(miktar, depo=None):
    if depo is None:
        depo = []
    depo.append(miktar)
    return depo

def test_yakit_ekle_tuzagi():
    sonuc1 = yakit_ekle(10)
    sonuc2 = yakit_ekle(20)
    # Mutable default argument (depo=[]) çözüldüğü için ikinci çağrı ilkini kirletmez.
    assert sonuc1 == [10]
    assert sonuc2 == [20]
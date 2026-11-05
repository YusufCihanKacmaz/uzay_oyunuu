
# Kapsam (Scope) ve UnboundLocalError Açıklamaları

## 1. Kapsam Örnekleri Tahminleri ve Sonuçları
- **Yerel (Local) Kapsam:** Bir fonksiyon içinde tanımlanan değişkenler sadece o fonksiyon içinde erişilmektedir.
- **Kapsayan (Enclosing) Kapsam:** İç içe fonksiyonlarda üst fonksiyonun değişkenleri alt fonksiyonlar tarafından okunabilir.
- **Küresel (Global) Kapsam:** Modül seviyesinde tanımlanan değişkenlerdir.

## 2. UnboundLocalError Nedir?
Python'da bir fonksiyon içinde global veya dış kapsamdaki bir değişkene atama yapmaya (değer değiştirmeye) çalıştığınızda, Python o değişkeni otomatik olarak yerel (local) kabul eder. Ancak atama yapılmadan önce okumaya (veya işleme sokmaya) kalkarsanız `UnboundLocalError: local variable referenced before assignment` hatası alınır. `global` anahtar kelimesi kullanılmadan bu durumdan kaçınmak için değerler argüman olarak aktarılmalı veya yapı (closure/nonlocal) kullanılmalıdır.
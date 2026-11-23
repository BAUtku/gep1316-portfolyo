import datetime  # Geçerli yılı öğrenmek için tarih modülünü içe aktarır.

ad = input("Adınız nedir? ")  # Kullanıcıdan adını ister.
dogum_yili = int(input("Doğum yılınız kaç? "))  # Kullanıcıdan doğum yılını alıp tam sayıya dönüştürür.

yas = datetime.date.today().year - dogum_yili  # Güncel yıla göre yaşını hesaplar.

print(f"Merhaba {ad}! {yas} yaşındasın.")  # Kişiselleştirilmiş Türkçe mesajı ekrana yazdırır.

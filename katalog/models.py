from django.db import models
from django.utils.text import slugify

class Kategori(models.Model):
    baslik = models.CharField(max_length=100, verbose_name="Kategori Adı")

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"

    def __str__(self):
        return self.baslik

class Urun(models.Model):
    # Teknik seçenekleri (İhtiyacına göre burayı genişletebilirsin)
    TEKNIK_SECENEKLERI = [
        ('emprime', 'Emprime Baskı'),
        ('nakis', 'Nakış / Bordür'),
        ('dijital', 'Dijital Baskı'),
        ('3d_nakis', '3D Kabartma Nakış'),
    ]

    baslik = models.CharField(max_length=200, verbose_name="Ürün Adı")
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, related_name="urunler", verbose_name="Kategorisi")
    teknik = models.CharField(max_length=50, choices=TEKNIK_SECENEKLERI, verbose_name="Uygulanan Teknik")
    resim = models.ImageField(upload_to='urunler/', verbose_name="Ürün Görseli")
    eklenme_tarihi = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Ürün"
        verbose_name_plural = "Ürünler"
        ordering = ['-eklenme_tarihi']

    def __str__(self):
        return f"{self.baslik} ({self.get_teknik_display()})"

class KurumsalSayfa(models.Model):
    baslik = models.CharField(max_length=200, verbose_name="Sayfa Başlığı")
    slug = models.SlugField(unique=True, blank=True, verbose_name="URL Uzantısı")
    icerik = models.TextField(verbose_name="Sayfa İçeriği")
    aktif = models.BooleanField(default=True, verbose_name="Yayında mı?")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.baslik)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Kurumsal Sayfa"
        verbose_name_plural = "Kurumsal Sayfalar"

    def __str__(self):
        return self.baslik
        # Mevcut kodlarının en altına ekle:

class Teklif(models.Model):
    ad_soyad = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20)
    email = models.EmailField()
    urun_turu = models.CharField(max_length=100)
    adet = models.IntegerField()
    notlar = models.TextField(blank=True, null=True)
    tarih = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ad_soyad} - {self.urun_turu}"

# KurumsalSayfa modelinin içine (class KurumsalSayfa: altına) şu satırı ekle:
# sira = models.PositiveIntegerField(default=0, verbose_name="Sıralama")
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

# SADECE ELİMİZDE OLAN 3 TABLOYU ÇAĞIRIYORUZ (Teklif hayaleti silindi)
from .models import Urun, Kategori, KurumsalSayfa, Teklif
try:
    from .models import BaskiTuru
except ImportError:
    BaskiTuru = None

# 1. ANA SAYFA (VİTRİN)
def vitrin(request):
    urunler = Urun.objects.all().order_by('-eklenme_tarihi')
    kategoriler = Kategori.objects.all()
    return render(request, 'vitrin.html', {'urunler': urunler, 'kategoriler': kategoriler})

# 2. ÜRÜN DETAY SAYFASI
def urun_detay(request, id):
    urun = get_object_or_404(Urun, id=id)
    return render(request, 'detay.html', {'urun': urun})

# 3. ARAMA MOTORU
def urun_ara(request):
    query = request.GET.get('q')
    sonuclar = ''
    if query:
        # Sadece ürün başlığında arama yapar (Çökmemesi için)
        sonuclar = Urun.objects.filter(baslik__icontains=query)
    return render(request, 'arama_sonuclari.html', {'sonuclar': sonuclar, 'query': query})

# 4. KURUMSAL SAYFALAR
def kurumsal_detay(request, slug):
    sayfa = get_object_or_404(KurumsalSayfa, slug=slug)
    return render(request, 'kurumsal_detay.html', {'sayfa': sayfa})

# 5. TEKLİF AL FORMU
def teklif_al(request):
    # Formun veritabanına kayıt özelliğini Faz-2'ye bıraktık. 
    # Şimdilik sadece müşterinin göreceği sayfayı sorunsuz açar.
    return render(request, 'teklif.html')
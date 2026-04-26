from django.contrib import admin
from .models import Kategori, Urun, KurumsalSayfa
from .models import Teklif

# Modelleri yönetim paneline kaydediyoruz ki panelde işlem yapabilelim
admin.site.register(Kategori)
admin.site.register(Urun)
admin.site.register(KurumsalSayfa)
admin.site.register(Teklif)
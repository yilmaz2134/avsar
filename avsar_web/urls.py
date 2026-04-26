from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('panel/', admin.site.urls),
    path('', include('katalog.urls')), # Katalog uygulamasının linkleri
]

# GELİŞTİRME AŞAMASINDA MEDYA DOSYALARINI AKTİF ETME
# Bu kısım sadece DEBUG=True olduğunda (yani senin bilgisayarında) çalışır.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # avsar_web/urls.py dosyasının en altına eklenecek

admin.site.site_header = 'Avşar Emprime Komuta Merkezi'
admin.site.site_title = 'Avşar Emprime Yönetim'
admin.site.index_title = 'Sistem Yönetim Paneline Hoş Geldiniz'
# Resimlerin sunucuda güvenle görünmesi için gereken ayar
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
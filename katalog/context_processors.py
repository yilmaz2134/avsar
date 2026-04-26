from .models import KurumsalSayfa

def kurumsal_menu(request):
    # Veritabanındaki tüm kurumsal sayfaları 'sira' numarasına göre alıp her sayfaya gönderir
    sayfalar = KurumsalSayfa.objects.all()
    return {'kurumsal_linkler': sayfalar}
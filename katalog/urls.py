from django.urls import path
from . import views

urlpatterns = [
    # Ana Sayfa (Vitrin)
    path('', views.vitrin, name='vitrin'),
    
    # Teklif Alma Sayfası
    path('teklif-al/', views.teklif_al, name='teklif_al'),
    
    # Kurumsal Sayfalar
    path('kurumsal/<slug:slug>/', views.kurumsal_detay, name='kurumsal_detay'),
    path('urun/<int:id>/', views.urun_detay, name='urun_detay'), 
]
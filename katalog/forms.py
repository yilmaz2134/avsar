from django import forms
from .models import Teklif

class TeklifForm(forms.ModelForm):
    class Meta:
        model = Teklif
        fields = ['ad_soyad', 'email', 'telefon', 'urun_turu', 'adet', 'tasarim', 'notlar']
        widgets = {
            'ad_soyad': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Adınız Soyadınız'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'E-posta Adresiniz'}),
            'telefon': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Telefon Numaranız'}),
            'urun_turu': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Örn: Siyah Oversize Tişört veya Şapka'}),
            'adet': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Kaç adet üretilecek?'}),
            'tasarim': forms.FileInput(attrs={'class': 'form-input'}),
            'notlar': forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'Baskı bölgesi (Sırt/Göğüs), kumaş türü veya özel istekleriniz...', 'rows': 4}),
        }
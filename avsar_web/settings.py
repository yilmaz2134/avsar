from django.conf.urls import static
import os
import dj_database_url
from pathlib import Path
from dotenv import load_dotenv

# Çevresel değişkenleri (.env) yükle
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --- GÜVENLİK AYARLARI (.env kasasından çekiliyor) ---
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG') == 'True'

# ALLOWED_HOSTS listesini ayarla
env_hosts = os.environ.get('ALLOWED_HOSTS')
if env_hosts:
    ALLOWED_HOSTS = env_hosts.split(',')
else:
    ALLOWED_HOSTS = ['*']

# --- UYGULAMALAR ---
INSTALLED_APPS = [
    'katalog',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
# Middleware listesinin en üstüne (SecurityMiddleware'den sonraya) ekle:
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Bunu ekle!
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Dosyanın en altına ekle:
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'avsar_web.urls'

# --- ŞABLONLAR (TEK VE GÜNCEL HALİ) ---
TEMPLATES = [
    {
        'APP_DIRS': True,
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'katalog.context_processors.kurumsal_menu',  # Dinamik kurumsal menü elçimiz
            ],
        },
    },
]

WSGI_APPLICATION = 'avsar_web.wsgi.application'

# --- VERİTABANI ---
DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',
        conn_max_age=600
    )
}
# --- ŞİFRE DOĞRULAMA ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# --- DİL VE SAAT ---
LANGUAGE_CODE = 'tr-TR'  # Türkçeye çevrildi (Admin paneli vs. için)
TIME_ZONE = 'Europe/Istanbul' # Saat dilimi İstanbul yapıldı
USE_I18N = True
USE_TZ = True

# --- STATİK VE MEDYA DOSYALARI (RESİMLER & CSS) ---
# --- STATİK VE MEDYA DOSYALARI ---
STATIC_URL = '/static/'

# İŞTE EKSİK OLAN KISIM BURASI:
# BASE_DIR ana dizini (manage.py'nin olduğu yer) temsil eder.
# Senin static klasörün avsar_web klasörünün içinde olduğu için yolu şöyle tarif etmeliyiz:

STATICFILES_DIRS = [
    BASE_DIR / "avsar_web" / "static",
]
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- E-POSTA GÖNDERİM AYARLARI ---
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'avsaremprime@gmail.com'
EMAIL_HOST_PASSWORD = 'buraya_google_uygulama_sifresi_gelecek'
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
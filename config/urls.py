from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# ------------------------------
# Ana URL Conf
# ------------------------------
urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', include('formapp.urls')),    
]

# ------------------------------
# DEBUG modunda medya dosyalarını sunmak için
# ------------------------------
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

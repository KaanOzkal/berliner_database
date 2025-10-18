from django.urls import path, include
from rest_framework import routers
from .views import UserFormViewSet, home, form_page

# ------------------------------
# DRF Router: React API endpointleri için
# ------------------------------
router = routers.DefaultRouter()
router.register(r'forms', UserFormViewSet, basename='userform')  # URL: /api/forms/

# ------------------------------
# URL Patterns
# ------------------------------
urlpatterns = [
    path('', home, name='home'),                # Ana sayfa (template)
    path('basvuru/', form_page, name='form_page'), # Django template form sayfası
    path('api/', include(router.urls)),         # React ve API için endpoint
]

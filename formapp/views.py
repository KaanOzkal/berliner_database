from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from django.utils.decorators import method_decorator
from .models import UserForm
from .serializers import UserFormSerializer
# views.py
from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session
from django.utils.crypto import get_random_string

# Basit session tabanlı giriş kontrolü
def home(request):
    # Eğer zaten giriş yapılmışsa form sayfasına yönlendir
    if request.session.get('authenticated'):
        return redirect('form_page')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Güvenli kullanıcı adı ve şifre kontrolü
        valid_credentials = [
            {'username': 'admin', 'password': 'berliner2024'},
            {'username': 'kiel', 'password': 'kiel123'},
            {'username': 'berliner', 'password': 'berliner'},
        ]
        
        for cred in valid_credentials:
            if cred['username'] == username and cred['password'] == password:
                request.session['authenticated'] = True
                request.session['user'] = username
                return redirect('form_page')
        
        # Hatalı giriş
        return render(request, 'home.html', {'error': 'Hatalı kullanıcı adı veya şifre!'})
    
    return render(request, 'home.html')

def form_page(request):
    # Giriş kontrolü - eğer giriş yapılmamışsa ana sayfaya yönlendir
    if not request.session.get('authenticated'):
        return redirect('home')
# Django Template View
def home(request):
    return render(request, 'home.html')

def form_page(request):
    if request.method == 'POST':
        print("=== DJANGO DEBUG ===")
        print("POST Data:", dict(request.POST))
        print("FILES Data:", dict(request.FILES))
        
        # Tüm dosya alanlarını al
        file_fields = [
            'cv', 'kimlik_karti', 'ehliyet', 'diploma', 'mezuniyet_sertifakasi',
            'staj_sertifikasi', 'sgk_hizmet_dokumu', 'adli_sicil', 
            'adli_sicil_almanca', 'vukuatli_nufus_kayit_ornegi', 'formul_a', 'formul_b', 'ikametgah', 
            'ek_belgeler'
        ]
        
        files_data = {}
        for field in file_fields:
            file_obj = request.FILES.get(field)
            files_data[field] = file_obj
            print(f"{field}: {file_obj}")
        
        # Model kaydı oluştur
        try:
            user_form = UserForm.objects.create(
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                email=request.POST.get('email'),
                phone=request.POST.get('phone'),
                birth_date=request.POST.get('birth_date'),
                source=request.POST.get('source'),
                education=request.POST.get('education'),
                profession=request.POST.get('profession'),
                terms=request.POST.get('terms') == 'on',
                privacy=request.POST.get('privacy') == 'on',
                **files_data
            )
            print(f"Kayıt başarıyla oluşturuldu: {user_form.id}")
        except Exception as e:
            print(f"Kayıt oluşturma hatası: {e}")
            return redirect('form_page')

        return redirect('form_page')

    # GET isteğinde tüm başvuruları çek
    submissions = UserForm.objects.all().order_by('-created_at')
    return render(request, 'form_page.html', {'submissions': submissions})

# API ViewSet
@method_decorator(csrf_exempt, name='dispatch')
class UserFormViewSet(viewsets.ModelViewSet):
    queryset = UserForm.objects.all()
    serializer_class = UserFormSerializer
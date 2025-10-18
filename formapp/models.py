from django.db import models

class UserForm(models.Model):
    # Kişisel Bilgiler
    first_name = models.CharField(max_length=100, verbose_name='Ad')
    last_name = models.CharField(max_length=100, verbose_name='Soyad')
    email = models.EmailField(verbose_name='E-posta')
    phone = models.CharField(max_length=20, verbose_name='Telefon')
    birth_date = models.DateField(verbose_name='Doğum Tarihi')

    # Nereden ulaştı (source)
    SOURCE_CHOICES = [
        ('ads', 'Sosyal medya reklamları veya diğer reklamlar'),
        ('friend', 'Bir tanıdığın vasıtası üzerine'),
        ('google', 'Google'),
        ('other', 'Diğer'),
    ]
    source = models.CharField(
        max_length=200,
        choices=SOURCE_CHOICES,
        verbose_name='Nereden Ulaştı'
    )

    # Eğitim ve Meslek
    EDUCATION_CHOICES = [
        ('primary', 'İlkokul'),
        ('middle', 'Ortaokul'),
        ('highschool', 'Lise'),
        ('associate', 'Ön Lisans'),
        ('bachelor', 'Lisans'),
        ('master', 'Yüksek Lisans'),
        ('phd', 'Doktora'),
    ]
    education = models.CharField(
        max_length=20,
        choices=EDUCATION_CHOICES,
        verbose_name='Eğitim Durumu'
    )

    PROFESSION_CHOICES = [
        ('kamyon_surucu', 'Kamyon Şoförü'),
        ('tir_surucu', 'Tır Şoförü'),
        ('kurye', 'Kurye'),
        ('saglik', 'Sağlık'),
        ('elektrik', 'Elektrik'),
        ('tekniker', 'Tekniker'),
        ('muhendis', 'Mühendis'),
        ('ogretmen', 'Öğretmen'),
        ('diger', 'Diğer'),
    ]
    profession = models.CharField(
        max_length=50,
        choices=PROFESSION_CHOICES,
        verbose_name='Meslek'
    )

    # Onay Kutuları
    terms = models.BooleanField(default=False, verbose_name='Kullanım Koşulları')
    privacy = models.BooleanField(default=False, verbose_name='Gizlilik Politikası')

    # Dosya Alanları - React'teki isimlerle aynı
    cv = models.FileField(upload_to='cv/', null=True, blank=True)
    kimlik_karti = models.FileField(upload_to='kimlik_kartis/', null=True, blank=True)
    ehliyet = models.FileField(upload_to='ehliyets/', null=True, blank=True)
    diploma = models.FileField(upload_to='diplomas/', null=True, blank=True)
    mezuniyet_sertifikasi = models.FileField(upload_to='certificates/', null=True, blank=True)
    staj_sertifikasi = models.FileField(upload_to='certificates', null=True, blank=True)
    sgk_hizmet_dokumu = models.FileField(upload_to='reports/', null=True, blank=True)
    adli_sicil = models.FileField(upload_to='records/', null=True, blank=True)
    adli_sicil_almanca = models.FileField(upload_to='records/', null=True, blank=True)
    vukuatli_nufus_kayit_ornegi = models.FileField(upload_to='records/', null=True, blank=True)
    formul_a = models.FileField(upload_to='forms/', null=True, blank=True)
    formul_b = models.FileField(upload_to='forms/', null=True, blank=True)
    ikametgah = models.FileField(upload_to='ikametgahs/', null=True, blank=True)
    ek_belgeler = models.FileField(upload_to='documents/', null=True, blank=True)

    # Zaman Damgaları
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

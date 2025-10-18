from django.contrib import admin
from .models import UserForm

@admin.register(UserForm)
class UserFormAdmin(admin.ModelAdmin):
    list_display = [
        'first_name', 
        'last_name', 
        'email', 
        'profession',
        'education',
        'source' ,
        'created_at'
        
    ]
    
    list_filter = [
        'profession',
        'education', 
        'source',
        'created_at',
    ]
    
    search_fields = [
        'first_name',
        'last_name', 
        'email',
        'profession'
    ]
    
    date_hierarchy = 'created_at'
    list_per_page = 25
    ordering = ['-created_at']
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('myapp.urls')),   # 👈 KEEP THIS FIRST
    path('admin/', admin.site.urls),
]
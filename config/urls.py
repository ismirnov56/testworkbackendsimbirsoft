from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls

"""
    Основные URL
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/v1/', include('notes.urls'))
]

urlpatterns += doc_urls
from django.contrib import admin
from django.urls import path, include
from django.conf import settings # importando os settings
from django.conf.urls.static import static # importando os statics

urlpatterns = [
    path('', include('receitas.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

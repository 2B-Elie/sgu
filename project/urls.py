from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# Personnaliser les textes de l'interface d'administration
admin.site.site_header = "Site d'administration du Système de Gestion des Urgences (SGU)"
admin.site.index_title = "Panel administration SGU"
admin.site.site_title = "SGU Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashborad.urls')), 
    path('ckeditor/', include('ckeditor_uploader.urls')),  # Ajout de l'URL pour CKEditor
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

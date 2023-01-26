from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
#from AppCoder.views import * #Ya no seria necesario :) 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/AppCoder/', permanent=True)), # Para que ingrese directamente a nuestra pagina
    path('AppCoder/', include('AppCoder.urls')),
    
]

# Clase 24 --> Para las imagenes
urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
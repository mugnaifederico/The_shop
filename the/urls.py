from django.urls import path
from .views import login, signup, home, logout, addthe, dettaglio
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),
    path('addthe/', addthe, name='addthe'),
    path('dettaglio/<int:id>/', dettaglio, name='dettaglio')
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
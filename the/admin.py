from django.contrib import admin
from .models import The, Recensione, Preferito, Utente
# Register your models here.

admin.site.register(The)
admin.site.register(Recensione)
admin.site.register(Preferito)
admin.site.register(Utente)
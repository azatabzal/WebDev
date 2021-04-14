from django.contrib import admin
from .models import company
from .models import vacancy

admin.site.register(company)
admin.site.register(vacancy)
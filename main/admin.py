from django.contrib import admin
from .models import Administration, Question, GovernmentEmployee


admin.site.register(Administration)
admin.site.register(Question)
admin.site.register(GovernmentEmployee)

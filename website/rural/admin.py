from django.contrib import admin
from . models.birth import Birth
from . models.death import Death

# Register your models here.
admin.site.register(Birth)
admin.site.register(Death)

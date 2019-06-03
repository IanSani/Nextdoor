from django.contrib import admin
from .models import Profile
from .models import Hood
from .models import Business
from .models import Location

# Register your models here.
admin.site.register(Profile)
admin.site.register(Hood)
admin.site.register(Business)
admin.site.register(Location)

from django.contrib import admin
from .models import (participants,Reservation)
from category.models import category
from .models import conference
admin.site.register(participants)
admin.site.register(Reservation)
admin.site.register(category)
admin.site.register(conference)


                    # Register your models here.

from django.contrib import admin
from .models import Event, Participant, Announcement

admin.site.register(Event)
admin.site.register(Participant)
admin.site.register(Announcement)
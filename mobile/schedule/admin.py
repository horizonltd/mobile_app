from django.contrib import admin
from . models import Event, Agenda, Membership, TypeOfMembership, Speaker
# Register your models here.


class EventAdmin(admin.ModelAdmin):

    search_fields = ['id','title']
class AgendaAdmin(admin.ModelAdmin):

    search_fields = ['__all__']

class MembershipAdmin(admin.ModelAdmin):
    search_fields = ['__all__']

class TypeOfMembershipAdmin(admin.ModelAdmin):
    search_fields = ['__all__']

class SpeakerAdmin(admin.ModelAdmin):
    search_fields = ['__all__']

admin.site.register(Event, EventAdmin)
admin.site.register(Agenda, AgendaAdmin)
admin.site.register(Membership, MembershipAdmin)
admin.site.register(TypeOfMembership, TypeOfMembershipAdmin)
admin.site.register(Speaker, SpeakerAdmin)

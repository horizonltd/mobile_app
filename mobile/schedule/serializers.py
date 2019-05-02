from rest_framework import serializers
#from hub.models import Lecture
from .import models

#Event serializer
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = '__all__'

#Agenda Serializer
class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model  = models.Agenda
        fields = '__all__'
#Membership Serializer
class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model  = models.Membership
        fields = '__all__'

#TypeOfMembership Serializer
class TypeOfMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model  = models.TypeOfMembership
        fields = '__all__'

#Speaker Serializer
class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model  = models.Speaker
        fields = '__all__'



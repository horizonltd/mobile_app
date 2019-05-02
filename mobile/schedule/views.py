from rest_framework import generics
from . import models
from . import serializers

#Event views
class EventList(generics.ListCreateAPIView):
    queryset  = models.Event.objects.all()
    serializer_class = serializers.EventSerializer
class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer

#Agenda views
class AgendaList(generics.ListCreateAPIView):
    queryset  = models.Agenda.objects.all()
    serializer_class = serializers.AgendaSerializer
class AgendaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Agenda.objects.all()
    serializer_class = serializers.AgendaSerializer

#Membership views
class MembershipList(generics.ListCreateAPIView):
    queryset  = models.Membership.objects.all()
    serializer_class = serializers.MembershipSerializer
class MembershipDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Membership.objects.all()
    serializer_class = serializers.MembershipSerializer

#Type of Membership views
class TypeOfMembershipList(generics.ListCreateAPIView):
    queryset  = models.TypeOfMembership.objects.all()
    serializer_class = serializers.TypeOfMembershipSerializer
class TypeOfMembershipDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.TypeOfMembership.objects.all()
    serializer_class = serializers.TypeOfMembershipSerializer

#Speaker  views
class SpeakerList(generics.ListCreateAPIView):
    queryset  = models.Speaker.objects.all()
    serializer_class = serializers.SpeakerSerializer
class SpeakerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Speaker.objects.all()
    serializer_class = serializers.SpeakerSerializer
from django.urls import path
from . import views

#This bind the views created in views.py class of the hub
urlpatterns = [
    #Event
    path('', views.EventList.as_view()),
    path('<int:pk>/', views.EventDetail.as_view()), #This get the ID of the passed lecture

    #Agenda
    path('', views.AgendaList.as_view()),
    path('<int:pk>/', views.AgendaDetail.as_view()), #This get the ID of the passed lecture

    #Membership
    path('', views.MembershipList.as_view()),
    path('<int:pk>/', views.MembershipDetail.as_view()), #This get the ID of the passed lecture

    #Membership Types
    path('', views.TypeOfMembershipList.as_view()),
    path('<int:pk>/', views.TypeOfMembershipDetail.as_view()), #This get the ID of the passed lecture

    #Speaker
    path('', views.SpeakerList.as_view()),
    path('<int:pk>/', views.SpeakerDetail.as_view()), #This get the ID of the passed lecture
]

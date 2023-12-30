
from rest_framework import generics
from .models import Event, UserRegistration
from .serializers import EventSerializer, UserRegistrationSerializer

class EventListAPIView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetailAPIView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class UserRegistrationCreateAPIView(generics.CreateAPIView):
    queryset = UserRegistration.objects.all()
    serializer_class = UserRegistrationSerializer

class UserRegistrationsListAPIView(generics.ListAPIView):
    queryset = UserRegistration.objects.all()
    serializer_class = UserRegistrationSerializer

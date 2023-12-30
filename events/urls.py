
from django.urls import path
from .views import home, create_event, register_event, event_detail, register_user, login_user, logout_user, unregister_event, search_events, user_dashboard 
from .api_views import EventListAPIView, EventDetailAPIView, UserRegistrationCreateAPIView, UserRegistrationsListAPIView


urlpatterns = [
    path('', home, name="home"),
    path('create/', create_event, name='create_event'),
    path('register/<int:event_id>/', register_event, name='register_event'),
    path('event/<int:event_id>/', event_detail, name='event_detail'),
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('unregister/<int:event_id>/', unregister_event, name='unregister_event'),
    path('search/', search_events, name='search_events'),
    path('dashboard/', user_dashboard, name='user_dashboard'), 

    # API Endpoints
    path('api/events/', EventListAPIView.as_view(), name='api_event_list'),
    path('api/events/<int:pk>/', EventDetailAPIView.as_view(), name='api_event_detail'),
    path('api/register/', UserRegistrationCreateAPIView.as_view(), name='api_register'),
    path('api/user_registrations/', UserRegistrationsListAPIView.as_view(), name='api_user_registrations'),
]






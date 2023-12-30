# events/urls.py

from django.urls import path
from .views import home, create_event, register_event, event_detail, register_user, login_user, logout_user, unregister_event # Ensure 'home' is imported correctly

urlpatterns = [
    path('', home, name="home"),
    path('create/', create_event, name='create_event'),
    path('register/<int:event_id>/', register_event, name='register_event'),
    path('event/<int:event_id>/', event_detail, name='event_detail'),
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('unregister/<int:event_id>/', unregister_event, name='unregister_event'),
    # Add other URLs as needed
]




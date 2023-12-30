# events/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Event, UserRegistration
from .forms import EventForm, UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate





def home(request):
    return render(request, 'events/home.html')


def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            return redirect('event_detail', event_id=event.id)
    else:
        form = EventForm()

    return render(request, 'events/create_event.html', {'form': form})

@login_required
def register_event(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        raise Http404("Event does not exist")

    if request.method == 'POST':
        if not UserRegistration.objects.filter(user=request.user, event=event).exists():
            if event.available_slots > 0:
                UserRegistration.objects.create(user=request.user, event=event)
                event.available_slots -= 1
                event.save()

    return render(request, 'events/register_event.html', {'event': event})


def event_detail(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        raise Http404("Event does not exist")

    return render(request, 'events/event_detail.html', {'event': event})


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('home')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register_user.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('home')

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login_user.html', {'form': form})

@login_required
def unregister_event(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        raise Http404("Event does not exist")

    if request.method == 'POST':
        try:
            registration = UserRegistration.objects.get(user=request.user, event=event)
            registration.delete()
            event.available_slots += 1
            event.save()
        except UserRegistration.DoesNotExist:
            pass  # Handle the case where the user is not registered for the event

    return redirect('event_detail', event_id=event.id)


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Event, UserRegistration
from .forms import EventForm, UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.db.models import Q
from django.contrib import messages



@login_required
def home(request):
    location_filter = request.GET.get('filter_location', '')
    title_filter = request.GET.get('search', '')

    
    events = Event.objects.filter(
        Q(location_name__icontains=location_filter) | Q(title__icontains=title_filter)
    )

    
    event = events.first()

    return render(request, 'events/home.html', {'events': events, 'event': event})



@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            messages.success(request, 'Event created successfully!')  # 
            return redirect('home')  
    else:
        form = EventForm()

    return render(request, 'events/create_event.html', {'form': form})

@login_required
def register_event(request, event):
    try:
        event = Event.objects.get(pk=event)
    except Event.DoesNotExist:
        raise Http404("Event does not exist")

    if request.method == 'POST':
        if not UserRegistration.objects.filter(user=request.user, event=event).exists():
            if event.available_slots > 0:
                UserRegistration.objects.create(user=request.user, event=event)
                event.available_slots -= 1
                event.save()

    return render(request, 'events/user_dashboard.html', {'event': event})



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
            login(request, user) 
            return redirect('login_user')
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

def search_events(request):
    query = request.GET.get('q')
    if query:
        events = Event.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    else:
        events = Event.objects.all()

    return render(request, 'events/search_events.html', {'events': events, 'query': query})



@login_required
def user_dashboard(request):
    
    user_registrations = UserRegistration.objects.filter(user=request.user)

    return render(request, 'events/user_dashboard.html', {'user_registrations': user_registrations})

@login_required
def unregister_event(request, event_id):
    
    event = get_object_or_404(Event, pk=event_id)

    
    registration = UserRegistration.objects.filter(user=request.user, event=event).first()

    if registration:
        
        registration.delete()
        
        event.available_slots += 1
        event.save()

    return redirect('user_dashboard')


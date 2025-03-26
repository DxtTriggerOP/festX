from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Participant
from django.contrib import messages

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/detail.html', {'event': event})

def register(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        participant, created = Participant.objects.get_or_create(email=email, defaults={'name': name})
        participant.events.add(event)
        messages.success(request, f'Registration successful for {event.title}!')
        return redirect('event_list')
    return render(request, 'events/register.html', {'event': event})
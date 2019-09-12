from django.shortcuts import render
from core.models import Event


def list_events(request):
    # user = request.user
    event = Event.objects.all()
    data = {'events': event}
    return render(request, 'listagem.html', data)

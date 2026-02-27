import django
from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import get_duration
from datacenter.models import format_duration
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    non_closed_visits = []
    for visit in Visit.objects.filter(leaved_at__isnull=True):
        duration = get_duration(visit)
        non_closed_visits.append(
            {
                'who_entered': str(visit.passcard),
                'entered_at': str(django.utils.timezone.localtime(visit.entered_at).strftime("%d %B %Y %H:%M")),
                'duration': format_duration(duration),
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)



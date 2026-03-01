import django
from django.shortcuts import get_object_or_404
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.helper_functions import get_duration
from datacenter.helper_functions import format_duration
from datacenter.helper_functions import is_visit_long
from django.utils.timezone import localtime


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    this_passcard_visits = []
    for visit in Visit.objects.filter(passcard=passcard):
        duration = get_duration(visit)
        this_passcard_visits.append(
            {
                'entered_at': str(django.utils.timezone.localtime(visit.entered_at).strftime("%d %B %Y %H:%M")),
                'duration': format_duration(duration),
                'is_strange': is_visit_long(visit),
            }
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)

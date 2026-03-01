import django
from datetime import timedelta
from django.utils.timezone import localtime


def get_duration(visit):
    if not visit.leaved_at:
        return django.utils.timezone.now() - visit.entered_at
    return visit.leaved_at - visit.entered_at


def format_duration(duration):    
    return str(duration).split('.')[0]


def is_visit_long(visit, minutes=60):
    return get_duration(visit) > timedelta(minutes=minutes)

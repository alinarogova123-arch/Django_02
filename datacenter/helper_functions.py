import django
from datetime import time
from datetime import timedelta
from django.utils.timezone import localtime


def get_duration(visit):
    if not visit.leaved_at:
        return django.utils.timezone.now() - visit.entered_at
    return visit.leaved_at - visit.entered_at


def format_duration(duration):
	duration_seconds = int(duration.total_seconds())
	hours = duration_seconds // 3600
	minutes = (duration_seconds % 3600) // 60
	seconds = (duration_seconds % 3600) % 60
	return time(hours, minutes, seconds).strftime("%H:%M:%S")


def is_visit_long(visit, minutes=60):
    return get_duration(visit) > timedelta(minutes=minutes)

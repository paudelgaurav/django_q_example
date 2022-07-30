from django.db.models import Case, F, When
from django_q.models import Schedule

from .models import Event


def decrease_remaining_days_from_event():
    Event.objects.update(
        remaining_days=Case(
            When(remaining_days__gt=1, then=F("remaining_days") - 1), default=0
        )
    )


Schedule.objects.create(
    func="decrease_remaining_days_from_event",
    schedule_type=Schedule.DAILY,
)

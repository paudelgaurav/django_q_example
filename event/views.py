from django.http import HttpResponse
from django_q.tasks import async_task

from .models import Event


def create_event(request, *args, **kwargs):
    Event.objects.create(title="my cool event", remaining_days=10)
    msg = "A new event has been created"
    async_task(
        "django.core.mail.send_mail",
        "New Event",
        msg,
        "from@example.com",
        ["to@example.com"],
    )
    async_task("time.sleep", 10)
    return HttpResponse(status=201)

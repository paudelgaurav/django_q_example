from django.core.management.base import BaseCommand
from django_q.models import Schedule
from django_q.tasks import schedule


class Command(BaseCommand):
    help = "Create CRON scheduler tasks"

    def handle(self, *args, **options):
        schedule(
            name="Decrease Remaining Days From Event",
            func="event.tasks.decrease_remaining_days_from_event",
            schedule_type=Schedule.DAILY,
        )
        self.stdout.write(self.style.SUCCESS("Successfully created CRON tasks"))

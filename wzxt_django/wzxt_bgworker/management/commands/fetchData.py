from django.core.management.base import BaseCommand, CommandError
from wzxt_bgworker.models import Transaction
from wzxt_bgworker.operations import liveline

class Command(BaseCommand):
    help = 'Update data and invest in stocks!!'

    def handle(self, *args, **options):
        # self.stdout.write(self.style.SUCCESS('Started fetching for data! instance %d'))
        liveline()

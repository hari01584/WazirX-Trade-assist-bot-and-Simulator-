from django.core.management.base import BaseCommand, CommandError
from dashboard.models import Transaction

class Command(BaseCommand):
    help = 'Update data and invest in stocks!!'

    def add_arguments(self, parser):
        parser.add_argument('instance_id', type=int, nargs='?', default=1)

    def handle(self, *args, **options):
        instance_id = options["instance_id"]
        self.stdout.write(self.style.SUCCESS('Started fetching for data! instance %d')%(instance_id,))

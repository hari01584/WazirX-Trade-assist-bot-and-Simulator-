from django.core.management.base import BaseCommand, CommandError
from wzxt_bgworker.models import Transaction
from wzxt_bgworker.views import doTrans

class Command(BaseCommand):
    help = 'Update data and invest in stocks!!'

    def add_arguments(self, parser):
        parser.add_argument('instance_id', type=int, nargs='?', default=1)

    def handle(self, *args, **options):
        instance_id = options["instance_id"]
        self.stdout.write(self.style.SUCCESS('Started fetching for data! instance %d')%(instance_id,))
        doTrans(instance_id)

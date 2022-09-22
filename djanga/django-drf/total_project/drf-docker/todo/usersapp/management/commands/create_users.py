from django.core.management.base import BaseCommand

from usersapp.models import User


class Command(BaseCommand):
    help = 'Create superuser and x users (default 3)'

    def handle(self, *args, **options):
        User.objects.all().delete()
        User.objects.create_superuser('kto', 'kto@kto.ru', '1')

        user_count = options['count'] if options['count'] else options['default']

        for i in range(user_count):
            User.objects.create_user(f'kto{i}', f'kto{i}@kto.ru', 6 * str(i))

    def add_arguments(self, parser):
        parser.add_argument('-c', '--count', type=int, default=3, help='count of users to create')

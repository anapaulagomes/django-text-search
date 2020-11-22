import csv
import sys

from django.core.management.base import BaseCommand

from files.models import File

csv.field_size_limit(sys.maxsize)  # be careful


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("file")

    def handle(self, *args, **options):
        with open(options["file"], newline="") as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            next(reader)
            for row in reader:
                File.objects.create(**{"url": row[0], "content": row[1]})

from django.core.management.base import BaseCommand
from django.db import connections


class Command(BaseCommand):

    def handle(self, database="default", *args, **options):

        cursor = connections[database].cursor()

        cursor.execute("SHOW TABLE STATUS")

        for row in cursor.fetchall():
            if row[1] != "InnoDB":
                print("Converting %s: %s" % (row[0], cursor.execute("ALTER TABLE `%s` ENGINE=InnoDB" % row[0])))

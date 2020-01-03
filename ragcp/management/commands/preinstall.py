from django.core.management.base import BaseCommand
from django.db import connections

tables = ['login', 'char']


class Command(BaseCommand):

    def handle(self, database="default", *args, **options):

        cursor = connections[database].cursor()

        cursor.execute("SHOW TABLE STATUS")

        for row in cursor.fetchall():
            if row[1] != "InnoDB" and row[0] in tables:
                print("Converting %s: %s" % (row[0], cursor.execute("ALTER TABLE `%s` ENGINE=InnoDB" % row[0])))

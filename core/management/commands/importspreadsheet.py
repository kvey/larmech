from django.core.management.base import BaseCommand, CommandError

from optparse import make_option
import gspread

from core.models import PartListing

class Command(BaseCommand):
    help = 'Imports part listings from google spreadsheet'
    option_list = BaseCommand.option_list + (
            make_option('-u', '--username',
                action='store',
                dest='username',
                default=False,
                help='Google username'),
            ) + (
            make_option('-p', '--password',
                action='store',
                dest='password',
                default=False,
                help='Google password'),
            ) + (
            make_option('-g', '--gurl',
                action='store',
                dest='spreadsheet_url',
                default=False,
                help='Google password'),
            )

    def handle(self, *args, **options):
        gc = gspread.login(options['username'], options['password'])
        sheet = gc.open_by_key('1HZoOkf4KlvomJC_wyoCb7LmCyhf9d2E8oLxN7FRM_SE')
        for worksheet in sheet.worksheets():
            list_of_lists = worksheet.get_all_values()
            headers = list_of_lists[0]
            rows = list_of_lists[1:]
            for row in rows:
                (listing, created) = PartListing.objects.get_or_create(
                        part_type=row[0],
                        part_number=row[1],
                        description=row[2],
                        quantity=int(float(row[3])),
                        )
                if created:
                    self.stdout.write('Added row %s' % listing.part_number)
                else:
                    self.stdout.write('Row already exists %s' % listing.part_number)
        self.stdout.write('Imported all')

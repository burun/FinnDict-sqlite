import os
import io
import sys
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'FinnDic.settings')

import django
django.setup()

from dictionary.models import Word
from openpyxl import load_workbook

wb = load_workbook('FinnishWords.xlsx', read_only=True)
ws = wb['Sheet1']
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')


def populate():

    for row in ws.rows:
        add_word(finnish=row[0].value,
                 chinese=row[1].value,
                 category=row[2].value)


def add_word(finnish, chinese, category):

    c = Word.objects.get_or_create(finnish=finnish)[0]
    c.chinese = chinese
    c.category = category
    c.save()

# Start execution here!
if __name__ == '__main__':
    print("Starting FinnDict words population script...")
    populate()

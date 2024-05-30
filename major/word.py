'''
This script is responsible for writing a generated schedule
into a word document.
'''

import docx
from copy import deepcopy
from docx.shared import pt

GAMES = ["name games", "softball", "basketball", "squash", "ultimate", "hockey", "lacrosse", "american-football", "tennis", "volleyball", "football"]

def create_tables(n, doc):
    '''
    this method creates all of the neccessary tables/schedules for
	each week in a new word document.
    :param doc: word document to add tables to
    :param n: number of tables to add
    '''

    for x in range(n):
        p = doc.add_paragraph("Group " + str(x+3))
        p.style = "group"
        template = doc.tables[0]
        tbl = template._tbl
        new_tbl = deepcopy(tbl)
        paragraph = doc.add_paragraph()
        paragraph._p.addnext(new_tbl)
        doc.add_page_break()

def fill_tables(matrix, doc):
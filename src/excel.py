# -*- coding: utf-8 -*-
# authors 13077/13130
# data: 05 de outubro de 2014
#

from mmap import mmap,ACCESS_READ
from xlrd import open_workbook

class Excel:
    excelFileLoc = ""

    def __init__(self, excelfilelocation):
        Excel.excelFileLoc = excelfilelocation
        print excelfilelocation

    def readFile(self):

        with open(Excel.excelFileLoc, 'rb') as f:
            print open_workbook(
                file_contents=mmap(f.fileno(),0,access=ACCESS_READ)
                )
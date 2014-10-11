# -*- coding: utf-8 -*-
# authors 13077/13130
# data: 05 de outubro de 2014
#

from excel import Excel
from db import Database

x = Excel("../Data/IPC_Portugal_1977_2013.xls")
x.readFile()
lista = x.lista

x.readData()
lista2 = x.lista2


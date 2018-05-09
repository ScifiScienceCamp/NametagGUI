import pandas
from Manager import Manager

class Camp():

    def __init__(self):

        self.df = pandas.read_excel('srs_export.xlsx', sheet_name='anything')

c = Camp()
f = Manager()
print(c.df[f.get_fields()[5]][1])

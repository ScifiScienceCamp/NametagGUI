import pandas
from Manager import Manager
from Child import Child

class Camp():

    def __init__(self, folder):

        self.df = pandas.read_excel(folder + '/srs_export.xlsx', sheet_name='anything')
        self.children = []
        for i in range(len(self.df)):
            c = Child()
            self.children.append(c)
            for field in Manager().get_fields():
                c.fields[field] = self.df[field][i]

if __name__ == "__main__":
    c = Camp("Compton")
    f = Manager()
    print(c.children[1].fields["FIRST_GIVEN_NAME"])

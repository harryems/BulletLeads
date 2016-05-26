
import csv
base='C:/Users/carlos.espinosa/Documents/pcna/'

class CustomCSV(object):
    def __init__(self):
        pass
    def read(self,brand):

        reader = csv.reader(open(base+brand+'.csv', 'rb'))
        return reader     
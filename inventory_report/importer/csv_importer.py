from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(self, path):
        if (path.endswith(".csv")):
            list = []
            with open(path) as fileRaw:
                file = csv.DictReader(fileRaw, delimiter=",", quotechar='"')
                list = [line for line in file]
            return list
        raise ValueError("Arquivo inválido")

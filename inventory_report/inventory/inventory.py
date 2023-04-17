import csv

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory():
    @staticmethod
    def import_data(path: str, type: str):
        file = csv.DictReader(open(path), delimiter=",", quotechar='"')
        list = [line for line in file]

        if (type == "simples"):
            return SimpleReport.generate(list)
        elif (type == "completo"):
            return CompleteReport.generate(list)
        else:
            print("Tipo incorreto")

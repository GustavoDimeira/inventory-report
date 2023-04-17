import csv
import json

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory():
    @staticmethod
    def import_data(path: str, type: str):
        if (path.endswith(".csv")):
            file = csv.DictReader(open(path), delimiter=",", quotechar='"')
            list = [line for line in file]
        elif (path.endswith(".json")):
            list = json.load(open(path))
        elif (path.endswith(".XML")):
            pass

        if (type == "simples"):
            return SimpleReport.generate(list)
        return CompleteReport.generate(list)

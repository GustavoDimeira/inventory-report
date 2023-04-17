import csv
import json
import xmltodict

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory():
    @staticmethod
    def import_data(path: str, type: str):
        list = []
        with open(path) as fileRaw:
            if (path.endswith(".csv")):
                file = csv.DictReader(fileRaw, delimiter=",", quotechar='"')
                list = [line for line in file]
            elif (path.endswith(".json")):
                list = json.load(fileRaw)
            elif (path.endswith(".xml")):
                file = fileRaw.read()
                list = xmltodict.parse(file)['dataset']['record']

        if (type == "simples"):
            return SimpleReport.generate(list)
        return CompleteReport.generate(list)

import sys

from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter

from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    if (len(sys.argv) >= 3):
        _, path, type = sys.argv
        if path.endswith(".json"):
            extention = JsonImporter
        elif path.endswith(".csv"):
            extention = CsvImporter
        else:
            extention = XmlImporter

        response = InventoryRefactor(extention).import_data(path, type)
        sys.stdout.write(response)
    else:
        sys.stderr.write("Verifique os argumentos\n")

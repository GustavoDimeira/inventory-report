from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(self, path):
        if (path.endswith(".json")):
            list = []
            with open(path) as fileRaw:
                list = json.load(fileRaw)
            return list
        raise ValueError("Arquivo inválido")

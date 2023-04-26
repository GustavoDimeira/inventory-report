from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    def import_data(path):
        if (path.endswith(".xml")):
            list = []
            with open(path) as fileRaw:
                file = fileRaw.read()
                list = xmltodict.parse(file)['dataset']['record']
            return list
        raise ValueError("Arquivo inválido")

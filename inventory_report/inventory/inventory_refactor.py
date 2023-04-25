from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path: str, type: str):
        for product in self.importer.import_data(path):
            self.data.append(product)

    def __iter__(self):
        return InventoryIterator(self.data)

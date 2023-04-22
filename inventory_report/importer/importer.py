from abc import ABC, abstractclassmethod


class Importer(ABC):
    @staticmethod
    @abstractclassmethod
    def import_data(self, path):
        raise NotImplementedError("Função não implementada")

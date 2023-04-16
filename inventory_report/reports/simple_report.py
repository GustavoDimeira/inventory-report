from datetime import datetime


class SimpleReport():
    @staticmethod
    def getOlder(list):
        (year, month, day) = list[0]["data_de_fabricacao"].split("-", 3)
        older = datetime(int(year), int(month), int(day))

        for product in list:
            (year, month, day) = product["data_de_fabricacao"].split("-", 3)
            testing = datetime(int(year), int(month), int(day))

            if older > testing:
                older = testing

        return str(older).split(" ")[0]

    def getSpoiling(list):
        now = datetime.now()
        (year, month, day) = list[0]["data_de_validade"].split("-", 3)
        closest = datetime(int(year), int(month), int(day))

        for product in list:
            (year, month, day) = product["data_de_validade"].split("-", 3)
            testing = datetime(int(year), int(month), int(day))

            if abs(now - closest) > abs(now - testing):
                closest = testing

        return str(closest).split(" ")[0]

    def getActive(list):
        ammount = {}

        for product in list:
            if (product["nome_da_empresa"] in ammount):
                ammount[product["nome_da_empresa"]] += 1
            else:
                ammount[product["nome_da_empresa"]] = 1

        most_products = list[0]["nome_da_empresa"]

        for company in ammount:
            if (ammount[company] > ammount[most_products]):
                most_products = company

        return [most_products, ammount]

    def generate(list: list):
        older = SimpleReport.getOlder(list)
        spoiling = SimpleReport.getSpoiling(list)
        mostProducts = SimpleReport.getActive(list)

        return (
            f"Data de fabricação mais antiga: {older}\n"
            f"Data de validade mais próxima: {spoiling}\n"
            f"Empresa com mais produtos: {mostProducts[0]}"
        )

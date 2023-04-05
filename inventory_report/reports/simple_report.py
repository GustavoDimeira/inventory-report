from datetime import datetime


def get_older_X_spoiling():
    older = False
    spoiling = False
    products_counter = {}

    for iten in list:
        (
            year_f,
            month_f,
            day_f,
        ) = iten["data_de_fabricacao"].split("-", 2)

        (
            year_v,
            month_v,
            day_v,
        ) = iten["data_de_validade"].split("-", 2)

        fabrication_date = datetime(int(year_f), int(month_f), int(day_f))
        validation_date = datetime(int(year_v), int(month_v), int(day_v))

        if (not older or fabrication_date < older):
            older = fabrication_date

        if (not spoiling or validation_date < spoiling):
            spoiling = validation_date

        if iten["nome_da_empresa"] in products_counter:
            products_counter[iten["nome_da_empresa"]] += 1
        else:
            products_counter[iten["nome_da_empresa"]] = 1
    return (older, spoiling, products_counter)


class SimpleReport:
    @staticmethod
    def generate(list: list):
        most_products = list[0]["nome_da_empresa"]

        (older, spoiling, products_counter) = get_older_X_spoiling()

        for company in products_counter:
            if (products_counter[company] > products_counter[most_products]):
                most_products = company

        return (f"""
            Data de fabricação mais antiga: {older}
            Data de validade mais próxima: {spoiling}
            Empresa com mais produtos: {most_products}
        """)

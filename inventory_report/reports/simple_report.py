from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(list: list):
        most_products = list[0]["nome_da_empresa"]
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

        for company in products_counter:
            if (products_counter[company] > products_counter[most_products]):
                most_products = company

        return (f"""
            Data de fabricação mais antiga: {older}
            Data de validade mais próxima: {spoiling}
            Empresa com mais produtos: {most_products}
        """)


SimpleReport.generate([
     {
       "id": 1,
       "nome_do_produto": "CADEIRA",
       "nome_da_empresa": "Forces of Nature",
       "data_de_fabricacao": "2022-04-04",
       "data_de_validade": "2023-02-09",
       "numero_de_serie": "FR48",
       "instrucoes_de_armazenamento": "Conservar em local fresco"
     },
     {
        "nome_da_empresa": "Forces of Nature",
        "data_de_fabricacao": "2022-04-05",
        "data_de_validade": "2023-02-08",
     },
     {
        "nome_da_empresa": "Forces of Naturea",
        "data_de_fabricacao": "2022-04-05",
        "data_de_validade": "2023-02-08",
     },
     {
        "nome_da_empresa": "Forces of Naturea",
        "data_de_fabricacao": "2022-04-05",
        "data_de_validade": "2023-02-08",
     },
     {
        "nome_da_empresa": "Forces of Naturea",
        "data_de_fabricacao": "2022-04-05",
        "data_de_validade": "2023-02-08",
     },
   ])

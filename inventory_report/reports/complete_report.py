from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(list: list):
        older = SimpleReport.getOlder(list)
        spoiling = SimpleReport.getSpoiling(list)
        mostProducts = SimpleReport.getActive(list)

        response = (
            f"Data de fabricação mais antiga: {older}\n"
            f"Data de validade mais próxima: {spoiling}\n"
            f"Empresa com mais produtos: {mostProducts[0]}\n"
            f"Produtos estocados por empresa:\n"
        )

        for key in mostProducts[1]:
            response += f"- {key}: {mostProducts[1][key]}\n"

        return response

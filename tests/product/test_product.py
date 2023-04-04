from inventory_report.inventory.product import Product


def test_cria_produto():
    newProduct = Product(
        1,
        'newProduct',
        'newCompany',
        '01/01/1001',
        '01/01/2001',
        '0915629628',
        '',
    )

    assert newProduct.id == 1
    assert newProduct.nome_do_produto == 'newProduct'
    assert newProduct.nome_da_empresa == 'newCompany'
    assert newProduct.data_de_fabricacao == '01/01/1001'
    assert newProduct.data_de_validade == '01/01/2001'
    assert newProduct.numero_de_serie == '0915629628'
    assert newProduct.instrucoes_de_armazenamento == ''

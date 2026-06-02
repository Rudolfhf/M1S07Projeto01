from funcoes import calcularMedia, funcValidar_tratar, funcPadronizar_regex, funcRegranegocio_cancelados, funcFormatarData

products = 'arquivos\olist_products_dataset.csv'
orders = 'arquivos\olist_orders_dataset.csv'





print("\n" + 5 * "//===//==")
print("Iniciando sanitização e tratamento na lista:")


listaProdutos, total_linhas_processadas, total_nulos_corrigidos = funcValidar_tratar(products)
pedidosCancelados = funcRegranegocio_cancelados(orders)

print("\n" + 5 * "===//===")
print(2 * "//===//" + " RELATORIO " + 2 * "//===//")
print(5 * "===//===")
print(f"Total de linhas processadas: {total_linhas_processadas}")
print(f"Total de registros nulos corrigidos: {total_nulos_corrigidos}")
print(f"Total de pedidos nulos cancelados: {pedidosCancelados}")
#calcularMedia(products, "bebes", ['product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm'])
#funcPadronizar_regex(products)
#funcRegranegocio_cancelados(orders)
#funcFormatarData(orders)
#relatorioFinal()
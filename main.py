from funcoes import tirarMediana, funcValidar_tratar, funcPadronizar_regex, funcRegranegocio_cancelados, funcFormatarData, relatorioFinal

products = 'arquivos\olist_products_dataset.csv'
orders = 'arquivos\olist_orders_dataset.csv'




#print("A sanitização dos arquivos será realizad, O Programa será Executado")

funcValidar_tratar(products)
#tirarMediana(products, "bebes", ['product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm'])
#funcPadronizar_regex(products)
#funcRegranegocio_cancelados(orders)
#funcFormatarData(orders)
#relatorioFinal()
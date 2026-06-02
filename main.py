from funcoes import calcularMedia, funcValidar_tratar, funcPadronizar_regex, funcRegranegocio_cancelados, funcFormatarData, total_linhas_processadas

products = 'arquivos\olist_products_dataset.csv'
orders = 'arquivos\olist_orders_dataset.csv'


#1
print("\n" + 46 * "=")
print("Iniciando tratamento de nulos nos nomes e dimensões")
print(46 * "=")
listaProdutos, total_nulos_corrigidos, total_linhas_products = funcValidar_tratar(products)

#2
print("\n" + 46 * "=")
print("Iniciando padronização de Categorias de Produtos")
print(46 * "=")
padronizarCategorias = funcPadronizar_regex(products)
print(padronizarCategorias)

#3
print("\n" + 46 * "=")
print("Iniciando Verificação da regra de negócios...")
print(46 * "=")
ordersType, contagem_cancelados_semdata, pedidosCancelados, contagem_geral_cancelados, total_linhas_orders = funcRegranegocio_cancelados(orders)
#A ver no relatório

#4
print("\n" + 46 * "=")
print("Tratamento de datas para formato simplificado Brasileiro")
print(46 * "=")
novaData = (funcFormatarData)

total_linhas_processadas = (total_linhas_products + total_linhas_orders)

print("\n" + 46 * "*")
print(5 * "===//===")
print(2 * "//===//" + " RELATORIO " + 2 * "//===//")
print(5 * "===//===")
print(f"Total de linhas processadas: {total_linhas_processadas}, Products:{total_linhas_products} - Orders:{total_linhas_orders}")
print(f"Total de registros nulos corrigidos: {total_nulos_corrigidos}")
print(f"Total de pedidos [Cancelados]: {contagem_geral_cancelados} ")

print("------------------------------")
print("Resultado Regra de Negócio")
print("------------------------------") 
print(f"Quantidade de Nulos na coluna [order_delivered_customer_date]:>>{contagem_cancelados_semdata}<<")
print(f"Distribuição por status:{ordersType}")
print(f"Total de pedidos com [Data de Entrega] nula e Status: cancelado: {pedidosCancelados}")
print("Conclusão: ")
print("Nem todos os registros que possuem [Data de Entrega vazia] são pedidos cancelados\npois há pedidos em que o processamento não foi finalizado")
print(46 * "*")  
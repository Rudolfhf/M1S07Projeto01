from funcoes import calcularMedia, funcValidar_tratar, funcPadronizar_regex, funcRegranegocio_cancelados, funcFormatarData

products = 'arquivos\\olist_products_dataset.csv'
orders = 'arquivos\\olist_orders_dataset.csv'


#1
print("\n" + 46 * "=")
print("Iniciando tratamento de nulos nos nomes de categorias e dimensões de produtos")
print(46 * "=")
listaProdutos, total_nulos_corrigidos, total_linhas_products = funcValidar_tratar(products)
print("----------------------------------------------")

#2
print("\n" + 46 * "=")
print("Iniciando padronização de Categorias de Produtos")
print(46 * "=")
padronizarCategorias = funcPadronizar_regex(products)
print("\n", padronizarCategorias)
print("----------------------------------------------")

#3
print("\n" + 46 * "=")
print("Iniciando Verificação da regra de negócios")
print(46 * "=")
ordersType, contagem_cancelados_semdata, pedidosCancelados, contagem_geral_cancelados, total_linhas_orders = funcRegranegocio_cancelados(orders)
print("\n===> Hipótese não confirmada, consta no relatório")
print("----------------------------------------------")
#No relatório

#4
print("\n" + 46 * "=")
print("Tratamento de datas para formato simplificado Brasileiro")
print(46 * "=")
novaData = funcFormatarData(orders)
print("===> Exemplo das 3 últimas linhas:")
for linha in novaData[-3:]:
    print(linha['order_approved_at'])
print("----------------------------------------------")

total_linhas = (total_linhas_products + total_linhas_orders)

print("\n" + 46 * "*")
print(5 * "===//===")
print(2 * "//===//" + " RELATÓRIO " + 2 * "//===//")
print(5 * "===//===")
print(f"Total de linhas processadas: Products:[{total_linhas_products}] + Orders:[{total_linhas_orders}] = {total_linhas} ")
print(f"Total de registros nulos corrigidos: {total_nulos_corrigidos}")
print(f"Total de pedidos [Cancelados]: {contagem_geral_cancelados} ")

print("------------------------------")
print("Resultado Regra de Negócio")
print("------------------------------") 
print(f"===> Quantidade de Nulos na coluna [order_delivered_customer_date]:\n>>{contagem_cancelados_semdata}<<")
print(f"===> Distribuição por status:")
for chave, valor in ordersType.items():
    print(f"> {chave}: {valor}")
#print(f"{ordersType}")
print(f"===> Total de pedidos com [Data de Entrega] 'Nula' e Status cancelado:\n>>{pedidosCancelados}<<")
print("===> Conclusão: ")
print("A hipótese não é verdadeira, porque nem todos os registros que possuem [Data de Entrega Vazia/Nula] \nsão pedidos com 'Status Cancelado' pois há pedidos em que o processamento não foi finalizado.")
print(46 * "*")  
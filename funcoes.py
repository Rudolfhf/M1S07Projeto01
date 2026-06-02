import csv
import re
from datetime import datetime

dimencoes = ['product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm']

#Função chamada pela função funcValidar_tratar para tratar a mediana da categoria dos produtos
# em que foram identificadas e passadas pelo método com nomecategoria, e campos_vazios que foram 
# identificados como dimensões nulas
#Percorre a lista novamente para cada produto identificado sem dimensões
def calcularMedia(arquivo, nomecategoria, campos_vazios):
    with open(arquivo, "r", newline='', encoding='utf-8') as csvfile:
        leitor = csv.DictReader(csvfile, delimiter=',') 
            
        soma = {campo: 0 for campo in campos_vazios} #Armazena a soma de cada registro de cada coluna de dimensão
        quantidade = {campo: 0 for campo in campos_vazios} # Armazena a quantidade de produtos por dimensões nulas identificadas
        medias = {} #Chave que armazena o cálculo da média por de cada dimensão
        print(f"===> Iniciando Calculo da soma para cada dimensão da categoria:{nomecategoria}")
        for linha in leitor:                   
            if linha['product_category_name'] == nomecategoria:
                  for campo in campos_vazios:                  
                    if linha[campo] not in ('', None):
                        soma[campo] += int(linha[campo])
                        quantidade[campo] += 1
                                              
        print(f"Categoria: {nomecategoria}")
        print(f"Soma Total: {soma}")
        print(f"Quantidade: {quantidade}")

        print("\n===> Calculando a média para ser preenchida nas dimensoes vazias...")

        #Cálcula a dimensão
        for campo in campos_vazios:

            if quantidade[campo] > 0:
                media = soma[campo] / quantidade[campo]
                medias[campo] = media
                print(f"{campo}: {media}")                         
            else:
                print(f"{campo}: sem dados") 
                return print("sem dados")   
        print("------------------------------------------")
        return medias

#Função para lista de Produtos:
#           - Valores nulos na coluna 'product_category_name' serão preenchidos com "Sem Categoria"
#           - Será verificado os produtos com dimensões nulas e será preenchido conforme a regra de corte.
#           - Regra de Corte: Foi escolhida a 'Listwise deletion' que é o tipo de descarte por ausência de valores
#           - Produtos sem identificação de categoria E dimensões nulas serão descartados, pois não há como tirar a média
#           - Produtos com categoria E dimensões nulas será aplicada a mediana das dimensões dos demais produtos da mesma categoria visando 
#             manter um maior número de registro, pois a quantidade de dados pode influênciar na regra de negócios
def funcValidar_tratar(arquivo):
    #Contadores
    total_linhas_products = 0 # Variável para armazenar o total de linhas processadas na lista de produtos
    total_nulos_corrigidos = 0 # Contador de Nulos para coluna 'product_category_name' da lista de Produtos
 
    linhas_sem_dimensoes = [] # Guarda as linhas com categoria mas faltando dimensões
    campos_vazios = [] # Guarda quais dimensões estão faltando para determinada linha
    resultados = [] # Utilizado para apresentação no main.py

    with open(arquivo, "r", newline='', encoding='utf-8') as csvfile:
        leitor = csv.DictReader(csvfile, delimiter=',')     
        
        for linha in leitor: 
            total_linhas_products += 1 
            #Correção dos nulos na coluna "product_category_name" preenchendo por "Sem Categoria"                           
            if linha and not linha['product_category_name']:             
                linha['product_category_name'] = "Sem Categoria"
                total_nulos_corrigidos += 1 #Contador de quantos nulos corrigidos
                                    
            #Verificar e guardar quais colunas das dimensões estão vazias para cada linha     
            campos_vazios = list(filter(lambda campo: not linha[campo], dimencoes))
            #Teste lógico para tratar somente linhas com categoria e campos vazios, descartando conforme a regra de corte
            if campos_vazios and linha['product_category_name'] != "Sem Categoria":
                
                linhas_sem_dimensoes.append(linha) 
                print("---------------------------------------------")
                print("===> Novo Produto com dimensoes vazias identificado\n")
                print(f"ID:{linha['product_id']}\n Categoria:{linha['product_category_name']}\n Tratar:{campos_vazios} ")
                print("---------------------------------------------")
                
                cat = linha['product_category_name'] #Captura o tipo da categoria para enviar para a função 'calcularMedia'

                #Envia a linha com as dimensões faltantes para a função que fará o calculo da mediana de determinada categoria 
                resultado = calcularMedia(arquivo, cat, campos_vazios) 
                try:
                    for campo, media in resultado.items():
                        linha[campo] = int(round(media))  #round(media, 2)                  
                        total_nulos_corrigidos += 1
                    print(f"===> RESULTADO CORREÇÃO DIMENSÕES: \n{linha}")
                except:
                    print("***Média não corrigida!!! Não há Categoria identificada ****")
                
                resultados.append(resultado) #Variável para fins de apresentação: mostra as linhas identificadas e tratadas
                 
        return resultados, total_nulos_corrigidos, total_linhas_products

#Padroniza as strings na coluna 'product_category_name', 
# transformando caractéres em minúsculos e sem espaçamento em nenhum dos lados
# e aplica a remoção de caráctéres especiais utilizando a função regex 
def funcPadronizar_regex(arquivo):
    with open(arquivo, "r", encoding='utf-8') as csvfile:
        resultados = []
        leitor = csv.DictReader(csvfile, delimiter=',')    
        for linha in leitor:       
            #Conversão para letras minúsculas e remoção de espaços em brancos
            if not linha['product_category_name'].islower():             
                linha['product_category_name'] = linha['product_category_name'].lower().strip()
                          
            #Remoção de caractéres especiais e pontuações em nomes das categorias
            resultado = linha['product_category_name'] = re.sub(r'[^\w\s]','',linha['product_category_name'])
            resultados.append(resultado)
        return f"Demonstração das últimas três linhas após padronização: {resultados[-3:]}"
                                                    
#Função para verificar a hipótese da regra de negócio
#A chave ordersType, contabiliza o tipo de status do pedido de todos os registros
# da coluna 'order_delivered_customer_date' que são nulos, apresentando os valores no relatório
def funcRegranegocio_cancelados(arquivo_dois):
    total_linhas_orders = 0
    with open(arquivo_dois, 'r', encoding='utf-8') as cvsfile:
        leitor = csv.DictReader(cvsfile, delimiter=',')

        #Armazena a quantidade de pedidos por tipo de status quando a data de entrega for nula.
        ordersType = {'order_canceled': 0,
        'order_shipped': 0,
        'order_unavailable': 0,
        'order_processing': 0,
        'order_invoiced': 0,
        'order_delivered': 0,
        'order_created': 0,
        'order_approved': 0
       }

        contagem_cancelados_semdata = 0 #Contador usado para guardar pedidos cancelados E com a data de entrega nula
        contagem_geral_cancelados = 0 #Contador usado para guardar todos os pedidos cancelados, apresentando no relatório
        #For para percorrer todos os registros com data de entrega nula e guardar seu valor de status
        for linha in leitor:
            total_linhas_orders += 1
            if linha['order_status'] == 'canceled' and linha['order_delivered_customer_date']:               
                contagem_geral_cancelados += 1
            
            elif not linha['order_delivered_customer_date']:
                contagem_cancelados_semdata += 1

                if linha['order_status'] == 'canceled':
                    ordersType['order_canceled'] += 1

                elif linha['order_status'] == 'shipped':
                    ordersType['order_shipped'] += 1

                elif linha['order_status'] == 'unavailable':
                    ordersType['order_unavailable'] += 1   

                elif linha['order_status'] == 'processing':
                    ordersType['order_processing'] += 1

                elif linha['order_status'] == 'invoiced':
                    ordersType['order_invoiced'] += 1

                elif linha['order_status'] == 'delivered':
                    ordersType['order_delivered'] += 1

                elif linha['order_status'] == 'created':
                    ordersType['order_created'] += 1

                elif linha['order_status'] == 'approved':
                    ordersType['order_approved'] += 1
                
                else:
                    print("N IDENTIFICADO")
                    print(linha['order_status'])

        contagem_geral_cancelados += contagem_cancelados_semdata #Usado para somar todos os cancelados
        
        return ordersType, contagem_cancelados_semdata, ordersType['order_canceled'], contagem_geral_cancelados, total_linhas_orders


#Função para converter para formato brasileiro dd/mm/aa
def funcFormatarData(arquivo):
        linhas_modificadas = []

        with open(arquivo, 'r', encoding='utf-8') as csvfile:
            leitor = csv.DictReader(csvfile, delimiter=',')
            
            qtd_nulos = []
            #Função datetime que utiliza o método strptime transforma a string em objeto date e mapeia o 
            # novo formato para posterior ajuste em data brasileira utilizando o método strftime
            for linha in leitor:
                try:
                    linha['order_approved_at'] = datetime.strptime(linha['order_approved_at'], '%Y-%m-%d %H:%M:%S') 
                    linha['order_approved_at'] = datetime.strftime(linha['order_approved_at'], '%d/%m/%Y %H:%M:%S')
                    
                except ValueError as erro: #Para fins de testes
                    qtd_nulos.append(erro)
                        
                linhas_modificadas.append(linha) #Para return no main.py
        print(f"Quantidade de linhas nulas {len(qtd_nulos)}")
        return f"Exemplo três últimas linhas modificadas{list(linhas_modificadas[-3:])}"    

    

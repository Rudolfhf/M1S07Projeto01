import csv
import re
from datetime import datetime

#products = 'arquivos\olist_products_dataset.csv'
#orders = 'arquivos\olist_orders_dataset.csv'

total_linhas_processadas = 0
dimencoes = ['product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm']


def calcularMedia(arquivo, nomecategoria, campos_vazios):
    with open(arquivo, "r", newline='', encoding='utf-8') as csvfile:
        leitor = csv.DictReader(csvfile, delimiter=',') 
        #mediana = sum(leitor['product_weight_g'])
        total = 0
        quantidade = 0
        soma = {campo: 0 for campo in campos_vazios}
        quantidade = {campo: 0 for campo in campos_vazios}
        medias = {}
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

def funcValidar_tratar(arquivo):

    global total_linhas_processadas
    total_nulos_corrigidos = 0
    #Contadores
    qtd_product_nulos = 0
    linhas_descartadas = []
    #dimencoes = ['product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm']
    linhas_sem_dimensoes = []
    campos_vazios = []
    resultados = []
    with open(arquivo, "r", newline='', encoding='utf-8') as csvfile:
        leitor = csv.DictReader(csvfile, delimiter=',')     
        
        for linha in leitor: 
            total_linhas_processadas += 1 
            #Correção dos nulos e vazius na coluna "product_category_name" por "Sem Categoria"                           
            if linha and not linha['product_category_name']:             
                linha['product_category_name'] = "Sem Categoria"
                total_nulos_corrigidos += 1
            
                              
            #Verificar quantidade de nulos nas dimensões:
            #linhas_sem_dimencoes = list(filter(lambda campo: not linha[campo] and linha['product_category_name'] != 'Sem Categoria', dimencoes))
            
            campos_vazios = list(filter(lambda campo: not linha[campo], dimencoes))

            
            if campos_vazios and linha['product_category_name'] != "Sem Categoria":
                
                linhas_sem_dimensoes.append(linha) 
                print("---------------------------------------------")
                print("===> Novo Produto com dimensoes vazias identificado\n")
                print(f"ID:{linha['product_id']}\n Categoria:{linha['product_category_name']}\n Tratar:{campos_vazios} ")
                print("---------------------------------------------")
                #for linha in linhas_sem_dimensoes:
                cat = linha['product_category_name']
                        
                resultado = calcularMedia(arquivo, cat, campos_vazios)
                try:
                    for campo, media in resultado.items():
                        linha[campo] = int(round(media))  #round(media, 2)                  
                        total_nulos_corrigidos += 1
                    print(f"===> RESULTADO CORREÇÃO DIMENSÕES: \n{linha}")
                except:
                    print("***Média não corrigida!!! Não há Categoria identificada ****")
                
                resultados.append(resultado)
            
        #print(f"Quantidade de linhas sem dimensoes: {len(linhas_sem_dimensoes)}") 
                 
        return resultados, total_nulos_corrigidos, total_linhas_processadas

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
        return f"Demonstração das últimas três linhas: {resultados[-3:]}"
                                                    

def funcRegranegocio_cancelados(arquivo_dois):
    global total_linhas_processadas
    with open(arquivo_dois, 'r', encoding='utf-8') as cvsfile:
        leitor = csv.DictReader(cvsfile, delimiter=',')

        ordersType = {'order_canceled': 0,
        'order_shipped': 0,
        'order_unavailable': 0,
        'order_processing': 0,
        'order_invoiced': 0,
        'order_delivered': 0,
        'order_created': 0,
        'order_approved': 0
       }

        contagem_cancelados_semdata = 0
        contagem_geral_cancelados = 0
    
        for linha in leitor:
            total_linhas_processadas += 1
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

        contagem_geral_cancelados += contagem_cancelados_semdata
        
        return ordersType, contagem_cancelados_semdata, ordersType['order_canceled'], contagem_geral_cancelados, total_linhas_processadas


#Função para converter para formato brasileiro dd/mm/aa
def funcFormatarData(arquivo):
        with open(arquivo, 'r', encoding='utf-8') as csvfile:
            leitor = csv.DictReader(csvfile, delimiter=',')
            
            qtd_nulos = []
            for linha in leitor:
                try:
                    linha['order_approved_at'] = datetime.strptime(linha['order_approved_at'], '%Y-%m-%d %H:%M:%S') 
                    linha['order_approved_at'] = datetime.strftime(linha['order_approved_at'], '%d/%m/%Y %H:%M:%S')
                    print(linha['order_approved_at'])
                except ValueError as erro:
                    qtd_nulos.append(erro)
                                 
            print(f"Quantidade de linhas nulas {len(qtd_nulos)}")
                

# n esquecer de remover a linha q add no csv

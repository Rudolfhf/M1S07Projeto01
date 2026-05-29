import csv
import re
from datetime import datetime

products = 'arquivos\olist_products_dataset.csv'
orders = 'arquivos\olist_orders_dataset.csv'

def ler_arquivo(arquivo):

    with open(arquivo, "r", encoding='utf-8') as csvfile:
        leitor = csv.DictReader(csvfile, delimiter=',')
        
        #Contadores
        qtd_product_weight_g = 0
        qtd_product_length_cm = 0
        qtd_product_height_cm = 0
        qtd_product_width_cm = 0

        #Correção dos nulos e vazius na coluna "product_category_name" por "Sem Categoria"
        
        for linha in leitor:
           
            if linha and not linha['product_category_name']:             
                linha['product_category_name'] = "Sem Categoria"
                print(linha)

            #| product_weight_g | product_length_cm | product_height_cm | product_width_cm |    
            #Verificar quantidade de nulos em product weightm length, heightm width
            if not linha['product_weight_g']:
                qtd_product_weight_g += 1             
                print(linha)
            
            if not linha['product_length_cm']:
                qtd_product_length_cm += 1             
                print(linha)

            if not linha['product_height_cm']:
                qtd_product_height_cm += 1             
                print(linha)

            if not linha['product_width_cm']:
                qtd_product_width_cm += 1
                print("AQUI FOI")             
                print(linha)

        print("RELATORIO")
        print(f"product_weight_g NULOS: = {qtd_product_weight_g}")
        print(f"product_length_cm NULOS: = {qtd_product_length_cm}")
        print(f"product_HEIGHT_cm NULOS: = {qtd_product_height_cm}")
        print(f"product_WIDTH_cm NULOS: = {qtd_product_width_cm}")
        #salvar = csv.DictWriter()

def limpar_padronizar(arquivo):
    with open(arquivo, "r", encoding='utf-8') as csvfile:

        leitor = csv.DictReader(csvfile, delimiter=',')
        
        for linha in leitor:

            #Conversão para letras minúsculas e remoção de espaços em brancos
            if not linha['product_category_name'].islower():             
                linha['product_category_name'] = linha['product_category_name'].lower().strip()
                          
            #Remoção de caractéres especiais e pontuações em nomes das categorias
            linha['product_category_name'] = re.sub(r'[^\w\s]','',linha['product_category_name'])
            print(linha)
                                                    

def filtrar(arquivo_dois):
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

        contador_vazios = 0
    
        for linha in leitor:
            if not linha['order_delivered_customer_date']:

                contador_vazios += 1

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
                      
        print("Resultado Regra de Negócio")
        print(f"Quantidade de datas de entregas vazias:{contador_vazios} com seus respectivos valores na coluna order_delivered_customer_date:")
        #print(f"Ordens Canceladas:{order_canceled}, Ordens Enviadas:{order_shipped}, unavailable:{order_unavailable}")
        print(f"{ordersType}")


#Função para converter para formato brasileiro dd/mm/aa
def formatacaoTemporal(arquivo):
        print("A DATA É")
        with open(arquivo, 'r', encoding='utf-8') as csvfile:
            leitor = csv.DictReader(csvfile, delimiter=',')
            '''
            teste = "2018/05/28 19:45:59"
            
            dataObjeto = datetime.strptime(f'{teste}', '%Y/%m/%d %H:%M:%S')
            data_formatada = datetime.strftime(dataObjeto, '%d/%m/%Y %H:%M:%S')
            print(data_formatada)
            '''

            qtd_nulos = []
            for linha in leitor:
                try:
                    linha['order_approved_at'] = datetime.strptime(linha['order_approved_at'], '%Y-%m-%d %H:%M:%S') 
                    linha['order_approved_at'] = datetime.strftime(linha['order_approved_at'], '%d/%m/%Y %H:%M:%S')
                    print(linha['order_approved_at'])
                except ValueError as erro:
                    qtd_nulos.append(erro)
                    
                finally:
                    print(f"modificação feita com sucesso")
            print(f"Quantidade de linhas nulas {len(qtd_nulos)}")
                
            #lambda x: x, datetime.strptime(x, '%Y/%m/%d %H:%M:%S'), linha['order_approved_at']


def relatorioFinal():
    print("RELATORIO")
       
       
                


                     
#ler_arquivo(products)      
#limpar_padronizar(products)
#filtrar(orders)
formatacaoTemporal(orders)

# n esquecer de remover a linha q add no csv

# M1S07Projeto01
Projeto avaliativo 01

# Descrição do Projeto: 
A Olist extraiu seus dados para suporte à tomada de decisões e integração com outras aplicações. No entanto, foram identificados travamentos e inconsistências que precisam ser solucionados. Este script foi desenvolvido para verificar e corrigir a extração, executando um pipeline de funções que sanitizam, formatam e validam as informações, viabilizando o uso seguro em ferramentas de Business Intelligence e em modelos preditivos de Machine Learning.
Duas listas fornecidas pela equipe de engenharia serão tratadas
- Produtos/products: "olist_products_dataset.csv"
- Pedidos/orders: "olist_orders_dataset.csv"

## Guia de Execução: passos necessários para rodar o script localmente.
O Script utiliza bibliotecas nativas do python sendo necessário somente a instalação do Python
Bibliotecas utilizadas:

- re
- csv
- DateTime

### Pré-requisitos:
Instalção do Python 3.10.1

- Windows:
winget install Python.Python

- Linux: 
sudo apt update
sudo apt install python3

## Passos: 
### 1 Downloads

- Faça o download do script utilizando o comando:<br>
git clone https://github.com/Rudolfhf/M1S07Projeto01.git

- Faça o download dos dois arquivos "olist_orders_dataset.csv" e "olist_products_dataset.csv"
que se encontram no endereço:<br>

Pela Web: https://github.com/fiesc-junior-prado/mine_projeto_bloco_1 <br>

Pelo Git: git clone https://github.com/fiesc-junior-prado/mine_projeto_bloco_1.git


### 2 Modificações Necessárias
- Na pasta em que o script for extraído, crie outra pasta chamada "arquivos" e coloque os dois arquivos .csv dentro dela
- Pelo CMD utilize o comando "python3 main.py" 

## Reflexão Teórica sobre Machine Learning:
Um pipeline estruturado para a correção e o tratamento de dados influencia diretamente a eficácia de futuros modelos de Machine Learning, mitigando vieses e o risco de overfitting. Ao eliminar outliers extremos ou registros corrompidos, o código impede que o algoritmo assimile anomalias e ruídos como se fossem regras. Essa higienização assegura que o modelo identifique padrões reais e mantenha uma forte capacidade de generalização diante de novos cenários.




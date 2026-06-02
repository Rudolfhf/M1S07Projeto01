# M1S07Projeto01
Projeto avaliativo 01

# Descrição do Projeto: 
A Olist extraiu seus dados para tomada de decisões e utilização em demais aplicações, 
mas identificou problemas de travamento e inconsistências que precisam ser solucionadas
e este script foi criado para verificar e corrigir os dados extraidos, realizando o pipeline 
através de funções que irão sanitizar, formatar, validar os dados possibilitando o uso em aplicações da Olist 
em Business Inteligence e em seus modelos preditivos de Machine Learning 

## Guia de Execução: Passo a passo de como rodar o código.

### Pré-requisitos:
Instalção do Python 3.10.1

- Windows:
winget install Python.Python

- Linux: 
sudo apt update
sudo apt install python3

## Passos: 
### 1 Downloads

- Faça o download do script utilizando o comando:
git clone https://github.com/Rudolfhf/M1S07Projeto01.git

- Faça o download dos dois arquivos "olist_orders_dataset.csv" e "olist_products_dataset.csv"
que se encontram no endereço: https://github.com/fiesc-junior-prado/mine_projeto_bloco_1

### 2 Modificações Necessárias
- Na pasta em que o projeto estiver, crie outra pasta chamada "arquivos" e coloque os dois arquivos .csv dentro dela
- Pelo CMD utilize o comando "python3 main.py" sem aspas

## Reflexão Teórica sobre Machine Learning:
Um bom pipeline de dados feito para correção dos dados pode influenciar como um futuro modelo de aprendizado de máquina irá funcionar, evitando vieses e overfitting na aplicação, assegurando que o algoritmo aprenda padrões reais em vez de ruídos. Quando o código limpa a base eliminando outliers extremos ou registros corrompidos, ele impede que o modelo aprenda essas anomalias e se torne rígido demais, o que garante a sua capacidade de generalizar o aprendizado para novas situações.




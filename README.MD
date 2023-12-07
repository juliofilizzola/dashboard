# Dashboard Analysis
Este projeto é uma aplicação Streamlit para a visualização e análise de vendas de supermercado. O projeto em Python envolve o manuseio de dados usando pandas e a visualização usando plotly.express.

O script Python importa as bibliotecas necessárias, carrega os dados de vendas do supermercado, cria uma nova coluna para o ano e mês, filtra os dados com base no mês selecionado e, finalmente, constrói e mostra os vários gráficos e tabelas.
A funcionalidade de layout do streamlit é usada para criar uma página com várias colunas para exibir diferentes gráficos lado a lado. Isso proporciona uma exibição clara e organizada dos gráficos no painel.

Nota: A biblioteca Plotly é usada para criar plots interativos em Python. Ela produz plots de alta qualidade, que aprimoram a aparência e funcionalidade do painel do streamlit.

## Instalação
O projeto envolve a leitura de um arquivo CSV que contém dados de vendas de supermercado e o processamento dos dados para visualização. Streamlit é usado para criar uma interface de painel de visualização amigável ao usuário, enquanto plotly.express é usado para criar gráficos interativos.
- streamlit
- pandas
- plotly
- numpy
You can install these using pip:

```bash
pip install streamlit pandas plotly
```
---
## Conjunto de dados
O conjunto de dados usado para este projeto é um arquivo CSV com o nome supermarket_sale.csv. Este arquivo deve estar localizado no mesmo diretório que o script Python. Os dados incluem os seguintes campos:

- Date
- Total (sales)
- City
- Product line
- Payment
- Rating

## Recursos
O painel mostra várias visualizações, incluindo:

1. Total de vendas por dia (gráfico de barras)
2. Vendas por tipo de produto por dia (gráfico de barras)
3. Total de vendas por filial (gráfico de barras)
4. Vendas por tipo de pagamento (gráfico de pizza)
5. Avaliação média por filial (gráfico de barras)
6. O usuário pode selecionar um mês específico para se concentrar.

## Executando
Para executar o painel, basta navegar até o diretório do projeto e executar o script Python usando o streamlit:

```bash
streamlit run <nome_do_script>.py
```

Substitua <nome_do_script>.py pelo nome do seu script Python. O painel estará então acessível em seu navegador da web.


Codigo desenvolvido a partir de asimov academy


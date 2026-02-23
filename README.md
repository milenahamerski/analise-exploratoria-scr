# Análise de Base SCR com Polars

Este projeto tem como objetivo realizar a análise de dados a partir de bases do [**SCR**](bcb.gov.br/estabilidadefinanceira/scrdata), utilizando **Python** e a biblioteca **Polars**.

## Download das bases de dados

1. Acesse o link do [Google Drive](https://drive.google.com/drive/folders/1RKWM44RwyKJUUb-aR2h2N5Qfx_S6PMfV?usp=sharing) com as bases do SCR. No Drive tambem e possivel encontrar um PDF com todos os parametros disponiveis na base de dados e as analises dos meses (02/25, 05/25 e 09/25)
2. Escolha qualquer arquivo CSV disponível.
3. Faça o download do arquivo para a mesma pasta onde está o código Python (ou ajuste o caminho no código, se necessário).

## Como usar uma base específica no código

Após baixar o arquivo desejado, basta alterar o nome do CSV na linha abaixo do código:

```python
df = pl.read_csv("scrdata_.csv", separator=";")
```

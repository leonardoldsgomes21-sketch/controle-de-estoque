from pathlib import Path


pasta_projeto = Path(__file__).resolve().parent
caminho_csv = pasta_projeto / "dados.csv"

# Aceita o nome atual do arquivo no projeto, que está em maiúsculas.
if not caminho_csv.exists():
    caminho_csv = pasta_projeto / "DADOS.CSV"

try:
    with open(caminho_csv, "r", encoding="utf-8") as arquivo:
        linha = arquivo.readline()
        while linha != "":
            print(linha, end="")
            linha = arquivo.readline()
except FileNotFoundError:
    print("Erro: arquivo 'dados.csv' não foi encontrado na raiz do projeto.")

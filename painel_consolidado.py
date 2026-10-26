import math
from pathlib import Path


COLUNAS_MATRIZ = 3
LINHAS_MATRIZ = 3
CABECALHO_ESPERADO = ["empresa", "produto", "setor", "quantidade", "custo_unitario"]


def localizar_csv():
    pasta_projeto = Path(__file__).resolve().parent
    caminho_csv = pasta_projeto / "dados.csv"

    # O arquivo do projeto também pode estar nomeado como DADOS.CSV.
    if not caminho_csv.exists():
        caminho_csv = pasta_projeto / "DADOS.CSV"
    return caminho_csv


def ler_dados(caminho=None):
    caminho_csv = Path(caminho) if caminho else localizar_csv()
    nome_empresa = None
    produtos = []

    try:
        with open(caminho_csv, "r", encoding="utf-8") as arquivo:
            numero_linha = 0
            cabecalho = arquivo.readline()
            while cabecalho and not cabecalho.strip():
                numero_linha += 1
                cabecalho = arquivo.readline()
            if not cabecalho:
                print("Erro: o arquivo CSV está vazio.")
                return None, []
            if [campo.strip() for campo in cabecalho.strip().split(",")] != CABECALHO_ESPERADO:
                print("Erro: o cabeçalho do CSV não corresponde ao formato esperado.")
                return None, []

            numero_linha += 1
            linha = arquivo.readline()
            while linha != "":
                numero_linha += 1
                if linha.strip():
                    campos = [campo.strip() for campo in linha.strip().split(",")]
                    if len(campos) != len(CABECALHO_ESPERADO) or any(not campo for campo in campos):
                        print(f"Aviso: linha {numero_linha} ignorada por estar incompleta ou conter campos vazios.")
                    else:
                        empresa_linha, produto, setor_texto, quantidade_texto, custo_texto = campos
                        try:
                            setor = int(setor_texto)
                            quantidade = int(quantidade_texto)
                            custo_unitario = float(custo_texto)
                        except ValueError:
                            print(f"Aviso: linha {numero_linha} ignorada por conter valor numérico inválido.")
                        else:
                            if not math.isfinite(custo_unitario) or setor < 1 or setor > LINHAS_MATRIZ * COLUNAS_MATRIZ:
                                print(f"Aviso: linha {numero_linha} ignorada por conter valores fora do intervalo permitido.")
                            elif quantidade < 0 or custo_unitario < 0:
                                print(f"Aviso: linha {numero_linha} ignorada por conter quantidade ou custo negativo.")
                            elif nome_empresa is not None and empresa_linha != nome_empresa:
                                print(f"Aviso: linha {numero_linha} ignorada por pertencer a outra empresa.")
                            else:
                                if nome_empresa is None:
                                    nome_empresa = empresa_linha
                                produtos.append(
                                    {
                                        "produto": produto,
                                        "setor": setor,
                                        "quantidade": quantidade,
                                        "custo_unitario": custo_unitario,
                                    }
                                )
                linha = arquivo.readline()
    except FileNotFoundError:
        print(f"Erro: arquivo '{caminho_csv.name}' não foi encontrado.")
        return None, []

    if not produtos:
        print("Aviso: o arquivo não contém produtos válidos para exibir.")
    return nome_empresa, produtos


def calcular_custos(produtos):
    produtos_calculados = []
    custo_geral = 0.0

    for produto in produtos:
        custo_total = produto["quantidade"] * produto["custo_unitario"]
        produto_calculado = produto.copy()
        produto_calculado["custo_total"] = custo_total
        produtos_calculados.append(produto_calculado)
        custo_geral += custo_total

    return produtos_calculados, custo_geral


def criar_matriz_estado(produtos):
    matriz = [[[] for _ in range(COLUNAS_MATRIZ)] for _ in range(LINHAS_MATRIZ)]

    for produto in produtos:
        # Os setores são numerados a partir de 1 e ocupam a matriz em ordem por linha.
        indice = produto["setor"] - 1
        linha, coluna = divmod(indice, COLUNAS_MATRIZ)
        matriz[linha][coluna].append(f"S{produto['setor']:02d} {produto['produto']}")

    return matriz


def formatar_reais(valor):
    valor_formatado = f"{valor:,.2f}"
    valor_formatado = valor_formatado.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {valor_formatado}"


def exibir_painel(nome_empresa, produtos, custo_geral):
    matriz = criar_matriz_estado(produtos)

    print("\n========== PAINEL CONSOLIDADO ==========")
    print(f"Empresa: {nome_empresa}")
    print("\nProdutos e custos:")
    print(f"{'Produto':<18} {'Setor':>6} {'Quantidade':>12} {'Custo unitário':>18} {'Custo total':>16}")
    print("-" * 74)

    for produto in produtos:
        print(
            f"{produto['produto']:<18} {produto['setor']:>6} {produto['quantidade']:>12} "
            f"{formatar_reais(produto['custo_unitario']):>18} "
            f"{formatar_reais(produto['custo_total']):>16}"
        )

    print(f"\nCusto geral do estoque: {formatar_reais(custo_geral)}")
    print("\nMatriz de estado por setor (setores em ordem por linha):")
    for indice, linha in enumerate(matriz, start=1):
        celulas = [", ".join(setor) if setor else "Livre" for setor in linha]
        print(f"Linha {indice}: " + " | ".join(celulas))


def main():
    nome_empresa, produtos = ler_dados()
    if not produtos:
        return

    produtos_calculados, custo_geral = calcular_custos(produtos)
    exibir_painel(nome_empresa, produtos_calculados, custo_geral)


if __name__ == "__main__":
    main()

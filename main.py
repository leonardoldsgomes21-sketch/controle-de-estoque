("LEONARDO LEITE")# Dados institucionais da empresa
empresa = {
    "nome": "TechStock",
    "ramo": "Tecnologia e Estoque",
    "cidade": "São Paulo",
    "ano_fundacao": 2025
}

("LEONARDO LEITE")# Lista de produtos em operação
produtos = [
    {"nome": "Notebook", "quantidade": 10, "preco": 3500.00},
    {"nome": "Mouse", "quantidade": 25, "preco": 50.00},
    {"nome": "Teclado", "quantidade": 15, "preco": 120.00}
]

# Matriz de estoque: linhas e colunas
estoque = [
    [10, 5, 8],
    [3, 12, 6],
    [7, 4, 9]
]

# Consultar a posição da linha 1, coluna 2
print(estoque[0][1])

# Atualizar a quantidade dessa posição
estoque[0][1] = 20

("KENNEDY MARQUIS")# Exibir a matriz
for linha in estoque:
    print(linha)

def mostrar_menu():
    print("\n===== TECHSTOCK =====")
    print("1 - Ver empresa")
    print("2 - Listar produtos")
    print("3 - Ver matriz de estoque")
    print("0 - Sair")


def ver_empresa():
    print("\nEmpresa:", empresa["nome"])
    print("Ramo:", empresa["ramo"])
    print("Cidade:", empresa["cidade"])


def listar_produtos():
    print("\n--- Produtos cadastrados ---")

    for produto in produtos:
        print(
            f'{produto["nome"]} | '
            f'Quantidade: {produto["quantidade"]} | '
            f'Preço: R$ {produto["preco"]:.2f}'
        )


def ver_estoque():
    print("\n--- Matriz de estoque ---")

    for linha in estoque:
        print(linha)


while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ").strip()

    if not opcao:
        print("Erro: digite uma opção.")
    elif opcao == "1":
        ver_empresa()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        ver_estoque()
    elif opcao == "0":
        print("Programa encerrado!")
        break
    else:
        print("Opção inválida. Tente novamente.")
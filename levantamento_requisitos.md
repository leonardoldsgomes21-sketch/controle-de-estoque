# Levantamento de Requisitos — TechStock

**Entregável:** 1 — Levantamento de Requisitos  
**Data:** 26 de outubro de 2026  
**Ambiente de referência:** GitHub Codespaces, terminal Linux, Python 3 (validado em Python 3.14.2)

## 1. Objetivo

Descrever os requisitos funcionais e não funcionais do protótipo TechStock, uma solução acadêmica para consulta de produtos, organização de estoque por setor e consolidação de custos.

## 2. Escopo e contexto

A solução contém um menu interativo em `main.py` e um painel independente em `painel_consolidado.py`. O primeiro apresenta dados institucionais, três produtos e uma matriz de estoque 3×3. O segundo lê `DADOS.CSV`, valida registros, calcula custos e associa os setores a posições de uma matriz 3×3. O arquivo de dados possui quatro produtos.

Os requisitos deste documento descrevem o comportamento esperado da solução. A coluna de status registra se o comportamento já existe no protótipo atual, sem confundir requisito com implementação concluída.

## 3. Requisitos Funcionais

| ID | Requisito | Critério de aceitação | Status atual |
|---|---|---|---|
| RF-01 | Consultar os dados institucionais da empresa. | A opção de empresa apresenta nome, ramo e cidade da TechStock. | Atendido no menu. |
| RF-02 | Listar os produtos e seus dados de estoque. | A consulta apresenta nome, quantidade e preço unitário em reais. | Parcial: o menu mostra três produtos; o CSV contém quatro. |
| RF-03 | Exibir uma matriz bidimensional de estado do estoque. | A matriz é exibida em linhas e colunas e permite identificar as posições ocupadas. | Parcial: há uma matriz numérica no menu e outra matriz por setor no painel, sem fonte compartilhada. |
| RF-04 | Oferecer navegação por menu interativo. | O programa repete o menu até que o usuário selecione a opção de saída. | Atendido em `main.py`. |
| RF-05 | Validar opções digitadas no menu. | Entradas vazias e opções desconhecidas mostram aviso e mantêm o programa ativo. | Atendido em `main.py`. |
| RF-06 | Ler o CSV sequencialmente e ignorar o cabeçalho. | O painel usa `readline()` até o fim do arquivo e separa os campos por vírgula. | Atendido em `painel_consolidado.py`. |
| RF-07 | Validar os campos dos registros CSV. | Setor e quantidade são convertidos para inteiros; custo unitário para decimal; linhas inválidas são avisadas e ignoradas. | Atendido no painel. |
| RF-08 | Calcular os custos por produto e do estoque. | Para cada produto, calcular quantidade × custo unitário; o total geral é a soma dos subtotais. | Atendido no painel. |
| RF-09 | Relacionar os setores à matriz e apresentar um painel consolidado. | Setores de 1 a 9 ocupam a matriz 3×3 em ordem por linha; o painel exibe produtos, quantidades, custos e total em reais. | Atendido no painel, de forma independente do menu. |
| RF-10 | Tratar falhas de leitura e dados inconsistentes. | Arquivo ausente, cabeçalho inválido, campos vazios, linhas incompletas e valores inválidos geram mensagens sem encerramento inesperado. | Atendido no painel. |

## 4. Requisitos Não Funcionais

| ID | Requisito | Critério |
|---|---|---|
| RNF-01 | Ambiente de execução. | Executar no terminal do GitHub Codespaces usando Python 3; desenvolvimento e validação deste protótipo ocorreram em Python 3.14.2. |
| RNF-02 | Dependências de execução. | Utilizar a biblioteca padrão do Python, sem exigir serviços externos para iniciar o menu ou o painel. |
| RNF-03 | Interface. | Operação por terminal, com opções e mensagens em português; não requer interface gráfica. |
| RNF-04 | Arquivo de dados. | Ler arquivo CSV em UTF-8 com cabeçalho `empresa,produto,setor,quantidade,custo_unitario`. O leitor aceita `dados.csv` e o nome atual `DADOS.CSV`. |
| RNF-05 | Robustez. | Entradas inválidas e registros incorretos não devem provocar encerramento inesperado; mensagens devem indicar o problema. |
| RNF-06 | Legibilidade e manutenção. | Organizar o programa em funções com responsabilidades específicas e nomes claros. |
| RNF-07 | Apresentação de valores. | Exibir preços em reais com prefixo `R$` e duas casas decimais, usando convenção brasileira. |

## 5. Regras de Negócio

1. O setor é um inteiro de 1 a 9 e identifica uma posição na matriz de três linhas por três colunas.
2. O número do setor é convertido para índice começando em zero: setor 1 ocupa linha 1, coluna 1; setor 4 ocupa linha 2, coluna 1.
3. A quantidade é um inteiro não negativo e o custo unitário é um número decimal não negativo e finito.
4. O custo total do produto é `quantidade × custo_unitario`.
5. O custo geral do estoque é a soma dos custos totais dos produtos válidos do CSV.
6. Registros de uma empresa diferente da primeira empresa válida do arquivo não entram no painel.

## 6. Critérios de Aceitação da Solução

- A opção de saída encerra o loop do menu; entrada vazia ou desconhecida não encerra o programa.
- O CSV é lido linha a linha, sem tentar converter a linha de cabeçalho em produto.
- Registros válidos aparecem no painel com setor, quantidade, custo unitário e subtotal.
- O custo geral corresponde à soma dos subtotais e é apresentado com duas casas decimais.
- O painel mostra os setores ocupados e as posições livres da matriz 3×3.
- Arquivo ausente ou registro inválido produz aviso compreensível.

## 7. Riscos e Próximos Ajustes

- Unificar a lista de produtos do menu e o CSV: atualmente o CSV inclui Monitor, mas a lista de `main.py` não.
- Unificar a matriz numérica do menu e a matriz de setores do painel para evitar duas representações divergentes.
- Definir uma única fonte de verdade para produtos, quantidades, preços e posições antes de acrescentar operações de entrada e saída.

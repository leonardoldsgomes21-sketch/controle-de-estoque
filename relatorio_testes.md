# Relatório da Bateria de Testes

**Projeto:** TechStock  
**Data:** 26/10/2026  
**Ambiente:** Python 3.14.2, terminal Linux  
**Resultado:** Testes solicitados aprovados, com uma divergência de cadastro registrada abaixo.

## Cenários executados

| Cenário | Resultado | Evidência |
|---|---|---|
| Entrada em branco no menu | Aprovado | A mensagem `Erro: digite uma opção.` é exibida e o loop continua. |
| Caracteres/opções inválidas | Aprovado | `abc` e `@#$` são rejeitados; o menu continua até a opção `0`. |
| Integridade do CSV | Aprovado | Cabeçalho esperado e quatro produtos; campos preenchidos, produtos/setores únicos, quantidades e custos não negativos. |
| Linha inicial vazia | Aprovado | O painel pula a linha vazia antes do cabeçalho; a conferência dos dados também a ignorou. |
| Execução do painel | Aprovado | Exibe quatro produtos, setores 1 a 4, matriz correspondente e total geral de R$ 45.250,00. |
| Compilação | Aprovado | `main.py` e `painel_consolidado.py` compilam sem erro. |

## Conferência dos valores

| Produto | Setor | Quantidade | Custo unitário | Custo total |
|---|---:|---:|---:|---:|
| Notebook | 1 | 10 | R$ 3.500,00 | R$ 35.000,00 |
| Mouse | 2 | 25 | R$ 50,00 | R$ 1.250,00 |
| Teclado | 3 | 15 | R$ 120,00 | R$ 1.800,00 |
| Monitor | 4 | 8 | R$ 900,00 | R$ 7.200,00 |
| **Total geral** |  |  |  | **R$ 45.250,00** |

## Observação

O cadastro usado pelo menu em `main.py` contém Notebook, Mouse e Teclado. O arquivo `DADOS.CSV` e o painel incluem também Monitor. Assim, o menu e o painel não apresentam a mesma lista completa de produtos. Essa divergência não alterou os testes de entrada do menu nem os cálculos do CSV/painel.

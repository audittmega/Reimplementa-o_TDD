# Reimplementação TDD - Calculadora IR

Este repositório contém a reimplementação de uma calculadora de Imposto de Renda utilizando a metodologia Test-Driven Development (TDD). O projeto segue o ciclo Red-Green-Refactor para cada funcionalidade, conforme demonstrado em um vídeo instrutivo.

## Funcionalidades Implementadas

*   **Cadastro de Rendimentos:** Gerenciamento dos rendimentos totais.
*   **Cálculo da Previdência Oficial:** Dedução da previdência com base nos rendimentos.
*   **Cadastro e Dedução de Dependentes:** Cálculo da dedução por número de dependentes.

## Como Executar

1.  Clone o repositório:
    `git clone https://github.com/audittmega/Reimplementa-o_TDD.git`
2.  Navegue até o diretório do projeto:
    `cd Reimplementa-o_TDD`
3.  Execute os testes:
    `python3.11 -m unittest test_calculadora_ir.py`

## Estrutura do Projeto

*   `calculadora_ir.py`: Contém a lógica da calculadora de Imposto de Renda.
*   `test_calculadora_ir.py`: Contém os testes unitários para as funcionalidades da calculadora.

# Gerenciador de Tarefas em Python (CLI)

Um gerenciador de tarefas simples e funcional, totalmente desenvolvido em Python e executado na linha de comando (CLI). O projeto permite ao usuário adicionar, listar e marcar tarefas como concluídas, com uma interface colorida para facilitar a visualização.

Este projeto foi criado como um exercício prático para reforçar conceitos fundamentais de programação, como manipulação de listas, funções, laços de repetição e captura de entrada do usuário.

## Funcionalidades

* **Adicionar Tarefas:** Permite a criação de novas tarefas com descrição personalizada.
* **Marcar como Concluídas:** Modifica o status de uma tarefa pendente para concluída.
* **Visualização Completa:** Lista todas as tarefas cadastradas, diferenciando pendentes e concluídas por cores.
* **Filtros de Visualização:** Permite listar apenas as tarefas pendentes ou apenas as concluídas.
* **Interface Colorida:** Utiliza códigos de cores ANSI para melhorar a experiência do usuário no terminal.
* **Validação de Entrada:** Trata entradas inválidas do usuário para evitar que o programa quebre.

## Análise Construtiva e Estrutura do Código

O projeto foi estruturado de forma modular, com cada funcionalidade do menu encapsulada em sua própria função (`nova_tarefa`, `marcar_concluida`, etc.).

A gestão de dados é feita através de duas listas globais (`tarefas` e `status_tarefas`), onde o índice de uma corresponde ao da outra. Embora funcional, uma melhoria futura seria refatorar essa estrutura para uma lista de dicionários ou objetos, tornando o código mais robusto e menos suscetível a erros de sincronização.

## Próximos Passos

Para evoluir o projeto, os seguintes passos são planejados:

* [ ] **Persistência de Dados:** Implementar a capacidade de salvar as tarefas em um arquivo (como `.json` ou `.txt`) para que não se percam ao fechar o programa.
* [ ] **Refatorar Estrutura de Dados:** Substituir as duas listas por uma estrutura única (lista de dicionários ou de objetos) para aumentar a integridade dos dados.
* [ ] **Adicionar Funcionalidades:** Incluir opções para **excluir** e **editar** tarefas existentes.
* [ ] **Eliminar Variáveis Globais:** Modificar as funções para que recebam a lista de tarefas como parâmetro, em vez de depender de variáveis globais, seguindo melhores práticas de programação.

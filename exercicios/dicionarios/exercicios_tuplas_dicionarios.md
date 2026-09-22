# Lista de Exercícios: Tuplas, Dicionários, Estruturas Aninhadas e Laços em Python

*(Pré-requisitos: Tuplas, Dicionários, Listas aninhadas, laços `for` e `while`, e condicionais `if/elif/else`.)*

---

## 🟢 Nível 1: Exercícios Fáceis (7 Problemas)

### Exercício 1: Contador de Nomes em Lista de Tuplas
* **Objetivo:** Escreva uma função `contar_maiores_de_idade(pessoas)` que receba uma lista de tuplas no formato `(nome, idade)` e retorne a quantidade de pessoas com `idade >= 18`.
* **Exemplo de Chamada:** `contar_maiores_de_idade([("Ana", 17), ("Bruno", 22), ("Carla", 19)])`
* **Retorno Esperado:** `2`

---

### Exercício 2: Somatório de Estoque de Dicionário
* **Objetivo:** Escreva uma função `calcular_estoque_total(produtos)` que receba um dicionário onde a chave é o nome do produto e o valor é a quantidade em estoque. Retorne a soma total de itens.
* **Exemplo de Chamada:** `calcular_estoque_total({"caneta": 10, "caderno": 5, "borracha": 8})`
* **Retorno Esperado:** `23`

---

### Exercício 3: Filtrar Alunos Aprovados por Dicionário
* **Objetivo:** Escreva uma função `filtrar_aprovados(notas_alunos)` que receba um dicionário `{nome: nota}` e retorne uma lista com o nome dos alunos aprovados (`nota >= 7.0`).
* **Exemplo de Chamada:** `filtrar_aprovados({"Alice": 8.5, "Bruno": 5.0, "Carla": 7.0})`
* **Retorno Esperado:** `["Alice", "Carla"]`

---

### Exercício 4: Converter Lista de Tuplas em Dicionário
* **Objetivo:** Escreva uma função `tuplas_para_dicionario(lista_tuplas)` que receba uma lista de tuplas `(chave, valor)` e monte um dicionário. Se o valor for negativo, ignore o par.
* **Exemplo de Chamada:** `tuplas_para_dicionario([("a", 10), ("b", -5), ("c", 20)])`
* **Retorno Esperado:** `{"a": 10, "c": 20}`

---

### Exercício 5: Busca em Dicionário com `while`
* **Objetivo:** Escreva uma função `buscar_codigo(produtos, codigo_alvo)` que receba uma lista de dicionários `[{"id": int, "nome": str}]` e utilize um laço `while` para retornar o nome do produto correspondente ao `codigo_alvo`. Se não encontrar, retorne `None`.
* **Exemplo de Chamada:** `buscar_codigo([{"id": 101, "nome": "Teclado"}, {"id": 102, "nome": "Mouse"}], 102)`
* **Retorno Esperado:** `"Mouse"`

---

### Exercício 6: Preço Médio de Produtos
* **Objetivo:** Escreva uma função `preco_medio(precos_dict)` que receba um dicionário no formato `{nome_produto: preco}` e retorne a média dos preços. Se o dicionário for vazio, retorne `0.0`.
* **Exemplo de Chamada:** `preco_medio({"livro": 30.0, "caneta": 10.0, "mochila": 80.0})`
* **Retorno Esperado:** `40.0`

---

### Exercício 7: Mapeamento de Paridade
* **Objetivo:** Escreva uma função `classificar_paridade(numeros)` que receba uma lista de números e retorne um dicionário com duas chaves: `"pares"` e `"impares"`, contendo as respectivas listas de valores.
* **Exemplo de Chamada:** `classificar_paridade([1, 2, 3, 4, 5])`
* **Retorno Esperado:** `{"pares": [2, 4], "impares": [1, 3, 5]}`

---

## 🟡 Nível 2: Exercícios Médios (8 Problemas)

### Exercício 8: Frequência de Palavras em Dicionário
* **Objetivo:** Escreva uma função `contar_frequencia(palavras)` que receba uma lista de palavras e retorne um dicionário onde cada chave é uma palavra e o valor é a quantidade de vezes que ela aparece na lista.
* **Exemplo de Chamada:** `contar_frequencia(["sol", "lua", "sol", "estrela", "sol"])`
* **Retorno Esperado:** `{"sol": 3, "lua": 1, "estrela": 1}`

---

### Exercício 9: Inverter Dicionário (Chave-Valor)
* **Objetivo:** Escreva uma função `inverter_dicionario(dicionario)` que inverta as chaves e valores de um dicionário. Assuma que todos os valores originais são únicos.
* **Exemplo de Chamada:** `inverter_dicionario({"Brasil": "Brasília", "França": "Paris"})`
* **Retorno Esperado:** `{"Brasília": "Brasil", "Paris": "França"}`

---

### Exercício 10: Atualizar Estoque com Compras
* **Objetivo:** Escreva uma função `atualizar_estoque(estoque_atual, novas_compras)` que receba um dicionário de estoque `{produto: qtd}` e uma lista de tuplas `(produto, qtd_comprada)`. A função deve somar as quantidades no dicionário existente e adicionar novos produtos caso não existam.
* **Exemplo de Chamada:** `atualizar_estoque({"maçã": 10, "banana": 5}, [("maçã", 5), ("laranja", 12)])`
* **Retorno Esperado:** `{"maçã": 15, "banana": 5, "laranja": 12}`

---

### Exercício 11: Filtrar Cadastro de Funcionários
* **Objetivo:** Escreva uma função `filtrar_funcionarios(funcionarios, departamento, salario_minimo)` que receba uma lista de dicionários contendo `{"nome": str, "depto": str, "salario": float}`. Retorne uma lista com os nomes dos funcionários que pertencem ao departamento especificado e ganham pelo menos o salário mínimo informado.
* **Exemplo de Chamada:** `filtrar_funcionarios([{"nome": "Ana", "depto": "TI", "salario": 5000}, {"nome": "Beto", "depto": "TI", "salario": 3000}, {"nome": "Caio", "depto": "RH", "salario": 4000}], "TI", 4000)`
* **Retorno Esperado:** `["Ana"]`

---

### Exercício 12: Processador de Pedidos com `while`
* **Objetivo:** Escreva uma função `processar_pedidos_fila(fila_pedidos, catalogo_precos)` que receba uma lista de tuplas `(id_pedido, nome_item, quantidade)` representando uma fila de pedidos. Utilize um laço `while` para retirar pedidos da fila um a um. Calcule e retorne um dicionário `{id_pedido: valor_total}`.
* **Exemplo de Chamada:** `processar_pedidos_fila([(101, "café", 2), (102, "bolo", 1)], {"café": 5.0, "bolo": 12.0})`
* **Retorno Esperado:** `{101: 10.0, 102: 12.0}`

---

### Exercício 13: Agrupar Pessoas por Faixa Etária
* **Objetivo:** Escreva uma função `agrupar_por_idade(pessoas)` que receba uma lista de tuplas `(nome, idade)` e retorne um dicionário com três chaves: `"jovens"` (< 18), `"adultos"` (18 a 59) e `"idosos"` (>= 60), contendo as listas de nomes correspondentes.
* **Exemplo de Chamada:** `agrupar_por_idade([("Lucas", 15), ("Maria", 34), ("João", 68)])`
* **Retorno Esperado:** `{"jovens": ["Lucas"], "adultos": ["Maria"], "idosos": ["João"]}`

---

### Exercício 14: Maior Pontuador por Categoria
* **Objetivo:** Escreva uma função `melhor_jogador(pontuacoes)` que receba um dicionário `{categoria: [lista_de_tuplas_jogador_pontos]}`. Para cada categoria, identifique o jogador com a maior pontuação e retorne um dicionário `{categoria: nome_do_campeao}`.
* **Exemplo de Chamada:** `melhor_jogador({"FPS": [("Alex", 150), ("Bia", 200)], "RPG": [("Caio", 500), ("Dani", 450)]})`
* **Retorno Esperado:** `{"FPS": "Bia", "RPG": "Caio"}`

---

### Exercício 15: Chaves com Valores Acima da Média
* **Objetivo:** Escreva uma função `chaves_acima_da_media(dados_dict)` que receba um dicionário `{chave: valor_numerico}`, calcule a média de todos os valores e retorne uma lista ordenada com as chaves cujos valores são estritamente maiores que essa média.
* **Exemplo de Chamada:** `chaves_acima_da_media({"a": 10, "b": 20, "c": 30, "d": 40})`
* **Retorno Esperado:** `["c", "d"]` *(Média é 25)*

---

## 🔴 Nível 3: Exercícios Difíceis (5 Problemas)

### Exercício 16: Consolidador de Carrinho de Compras
* **Objetivo:** Escreva uma função `consolidar_carrinho(compras)` que receba uma lista de dicionários, onde cada dicionário representa um item comprado: `{"produto": str, "preco": float, "qtd": int}`. Retorne um dicionário consolidado `{produto: (qtd_total, valor_total)}` agrupando itens repetidos e somando suas quantidades e valores totais.
* **Exemplo de Chamada:** `consolidar_carrinho([{"produto": "pão", "preco": 2.0, "qtd": 3}, {"produto": "leite", "preco": 4.0, "qtd": 1}, {"produto": "pão", "preco": 2.0, "qtd": 2}])`
* **Retorno Esperado:** `{"pão": (5, 10.0), "leite": (1, 4.0)}`

---

### Exercício 17: Matriz Esparsa representada por Dicionário
* **Objetivo:** Escreva uma função `somar_matrizes_esparsas(m1, m2)` onde matrizes são representadas por dicionários `{ (linha, coluna): valor }`. Retorne um novo dicionário com a soma das duas matrizes. Se a soma de uma posição for `0`, ela não deve estar presente no dicionário resultante.
* **Exemplo de Chamada:** `somar_matrizes_esparsas({(0, 0): 5, (1, 2): 3}, {(0, 0): -5, (1, 2): 4, (2, 2): 1})`
* **Retorno Esperado:** `{(1, 2): 7, (2, 2): 1}`

---

### Exercício 18: Validador de Estrutura de Grafo (Conexões)
* **Objetivo:** Escreva uma função `verificar_caminho(grafo, caminho)` que receba um dicionário representando um grafo `{no: [vizinhos]}` e uma lista de nós representando um `caminho`. Utilize um laço `while` para verificar se é possível percorrer o caminho sequencialmente através das conexões existentes. Retorne `True` ou `False`.
* **Exemplos de Chamada:**
  * `verificar_caminho({"A": ["B", "C"], "B": ["C"], "C": []}, ["A", "B", "C"])` $ightarrow$ `True`
  * `verificar_caminho({"A": ["B"], "B": ["C"], "C": []}, ["A", "C"])` $ightarrow$ `False`

---

### Exercício 19: Análise de Desempenho de Turmas
* **Objetivo:** Escreva uma função `analisar_turmas(escola)` que receba uma estrutura aninhada: `{nome_turma: {nome_aluno: [lista_de_notas]}}`. Retorne um dicionário `{nome_turma: nome_do_aluno_com_maior_media}`.
* **Exemplo de Chamada:** `analisar_turmas({"T1": {"Ana": [8, 9], "Beto": [5, 6]}, "T2": {"Carla": [7, 8], "Daniel": [9, 10]}})`
* **Retorno Esperado:** `{"T1": "Ana", "T2": "Daniel"}`

---

### Exercício 20: Sistema de Indexação Invertida (Mecanismo de Busca)
* **Objetivo:** Escreva uma função `criar_indice_invertido(documentos)` que receba uma lista de tuplas `(id_doc, texto_string)`. Retorne um dicionário onde cada chave é uma palavra (em minúsculas) e o valor é uma lista contendo os `id_doc` de todos os documentos que contêm aquela palavra (sem IDs duplicados por palavra).
* **Exemplo de Chamada:** `criar_indice_invertido([(1, "python eh legal"), (2, "aprender python eh bom"), (3, "java tambem eh legal")])`
* **Retorno Esperado:** `{"python": [1, 2], "eh": [1, 2, 3], "legal": [1, 3], "aprender": [2], "bom": [2], "java": [3], "tambem": [3]}`

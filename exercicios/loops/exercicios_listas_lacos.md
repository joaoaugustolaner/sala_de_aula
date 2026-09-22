# Lista de Exercícios: Listas, Laços de Repetição e Condicionais em Python

*(Pré-requisitos: Manipulação de listas, laços `for` e `while`, e condicionais `if/elif/else`.)*

---

## 🟢 Nível 1: Exercícios Fáceis (7 Problemas)

### Exercício 1: Filtrar Números Pares
* **Objetivo:** Escreva uma função `filtrar_pares(numeros)` que receba uma lista de números inteiros e retorne uma nova lista apenas com os números pares.
* **Exemplo de Chamada:** `filtrar_pares([1, 2, 3, 4, 5, 6])`
* **Retorno Esperado:** `[2, 4, 6]`

---

### Exercício 2: Contador de Números Negativos
* **Objetivo:** Escreva uma função `contar_negativos(numeros)` que percorra uma lista e retorne a quantidade de números estritamente menores que zero.
* **Exemplo de Chamada:** `contar_negativos([10, -3, 0, -5, 8, -1])`
* **Retorno Esperado:** `3`

---

### Exercício 3: Soma de Valores Maiores que um Limite
* **Objetivo:** Escreva uma função `somar_maiores_que(numeros, limite)` que receba uma lista de números e um valor de limite, retornando a soma apenas dos valores superiores ao limite.
* **Exemplo de Chamada:** `somar_maiores_que([10, 5, 20, 3, 15], 8)`
* **Retorno Esperado:** `45` *(10 + 20 + 15)*

---

### Exercício 4: Substituir Negativos por Zero
* **Objetivo:** Escreva uma função `zerar_negativos(numeros)` que receba uma lista de inteiros e retorne uma nova lista onde todo número negativo é substituído por `0`.
* **Exemplo de Chamada:** `zerar_negativos([4, -2, 7, -9, 0])`
* **Retorno Esperado:** `[4, 0, 7, 0, 0]`

---

### Exercício 5: Busca de Elemento com `while`
* **Objetivo:** Escreva uma função `contem_valor(lista, alvo)` usando um laço `while` para verificar se o valor `alvo` está presente na `lista`. Retorne `True` ou `False`.
* **Exemplo de Chamada:** `contem_valor(["maçã", "banana", "uva"], "banana")`
* **Retorno Esperado:** `True`

---

### Exercício 6: Classificar Notas de Alunos
* **Objetivo:** Escreva uma função `contar_aprovados(notas)` que receba uma lista de notas e retorne quantos alunos obtiveram nota maior ou igual a `7.0`.
* **Exemplo de Chamada:** `contar_aprovados([8.5, 5.0, 7.0, 6.5, 9.0])`
* **Retorno Esperado:** `3`

---

### Exercício 7: Separador de Textos Curtos e Longos
* **Objetivo:** Escreva uma função `filtrar_palavras_curtas(palavras, tamanho_maximo)` que receba uma lista de strings e retorne apenas as palavras com comprimento menor ou igual ao `tamanho_maximo`.
* **Exemplo de Chamada:** `filtrar_palavras_curtas(["sol", "computador", "python", "mar"], 6)`
* **Retorno Esperado:** `["sol", "python", "mar"]`

---

## 🟡 Nível 2: Exercícios Médios (8 Problemas)

### Exercício 8: Separador de Pares e Ímpares
* **Objetivo:** Escreva uma função `separar_pares_impares(numeros)` que receba uma lista de inteiros e retorne uma string no formato `"Pares: X | Ímpares: Y"`, onde X é a quantidade de pares e Y a quantidade de ímpares.
* **Exemplo de Chamada:** `separar_pares_impares([1, 2, 3, 4, 5])`
* **Retorno Esperado:** `"Pares: 2 | Ímpares: 3"`

---

### Exercício 9: Maior e Menor Valor Sem Funções Nativas
* **Objetivo:** Escreva uma função `encontrar_extremos(numeros)` que receba uma lista não vazia de números e retorne uma tupla `(menor, maior)` sem utilizar `min()` ou `max()`.
* **Exemplo de Chamada:** `encontrar_extremos([14, 2, 35, -4, 20])`
* **Retorno Esperado:** `(-4, 35)`

---

### Exercício 10: Processamento de Caixa Eletrônico com `while`
* **Objetivo:** Escreva uma função `simular_saque(saldo_inicial, saques)` que receba o saldo da conta e uma lista de saques desejados. Processa cada saque sequencialmente usando `while`. Se o saldo for suficiente, desconta o valor; se não for, ignora o saque. Retorne o saldo restante.
* **Exemplo de Chamada:** `simular_saque(200, [50, 100, 80, 30])`
* **Retorno Esperado:** `20` *(Subtrai 50, 100 e 30; ignora o 80 por saldo insuficiente)*

---

### Exercício 11: Remover Duplicados Mantedor de Ordem
* **Objetivo:** Escreva uma função `remover_duplicados(lista)` que receba uma lista e retorne uma nova lista apenas com a primeira ocorrência de cada elemento, preservando a ordem original.
* **Exemplo de Chamada:** `remover_duplicados([1, 3, 2, 3, 1, 4, 2])`
* **Retorno Esperado:** `[1, 3, 2, 4]`

---

### Exercício 12: Média dos Positivos
* **Objetivo:** Escreva uma função `media_positivos(numeros)` que calcule a média aritmética apenas dos números estritamente positivos. Se não houver números positivos, retorne `0.0`.
* **Exemplo de Chamada:** `media_positivos([-5, 10, -2, 20, 30])`
* **Retorno Esperado:** `20.0` *(10 + 20 + 30) / 3*

---

### Exercício 13: Validador de Senhas em Lista
* **Objetivo:** Escreva uma função `validar_senhas(lista_senhas)` que receba uma lista de strings e retorne apenas as senhas que possuem pelo menos 8 caracteres.
* **Exemplo de Chamada:** `validar_senhas(["12345", "senha1234", "admin", "python2026"])`
* **Retorno Esperado:** `["senha1234", "python2026"]`

---

### Exercício 14: Busca do Primeiro Elemento Fora do Padrão (`while`)
* **Objetivo:** Escreva uma função `primeiro_impar(numeros)` que percorra uma lista usando `while` e retorne o primeiro número ímpar encontrado. Se não encontrar nenhum, retorne `None`.
* **Exemplo de Chamada:** `primeiro_impar([2, 4, 6, 9, 10, 11])`
* **Retorno Esperado:** `9`

---

### Exercício 15: Contagem de Frequência de um Elemento
* **Objetivo:** Escreva uma função `contar_ocorrencias(lista, elemento_alvo)` que conte quantas vezes `elemento_alvo` aparece na lista sem utilizar a função `.count()`.
* **Exemplo de Chamada:** `contar_ocorrencias(["a", "b", "a", "c", "a"], "a")`
* **Retorno Esperado:** `3`

---

## 🔴 Nível 3: Exercícios Difíceis (5 Problemas)

### Exercício 16: Análise de Sequência Crescente
* **Objetivo:** Escreva uma função `is_estritamente_crescente(palavras)` que receba uma lista de strings e verifique se cada string é estritamente maior que o anterior. Retorne `True` ou `False`.
* **Exemplos de Chamada:**
  * `is_estritamente_crescente(["lá", "lua", "porta", "cinema", "computador"])` -> `True`
  * `is_estritamente_crescente(["palito","geringonça","lápis","lâmpada"])` -> `False`

---

### Exercício 17: Condensador de Lista (Compressão de Nulos/Zeros)
* **Objetivo:** Escreva uma função `mover_zeros_para_o_final(numeros)` que receba uma lista de inteiros e retorne uma nova lista onde todos os zeros são movidos para o final, mantendo a ordem relativa dos elementos não nulos.
* **Exemplo de Chamada:** `mover_zeros_para_o_final([0, 1, 0, 3, 12, 0, 5])`
* **Retorno Esperado:** `[1, 3, 12, 5, 0, 0, 0]`

---

### Exercício 18: Simulador de Fila de Atendimento Preferencial
* **Objetivo:** Escreva uma função `processar_fila(clientes)` que receba uma lista de tuplas `(nome, idade)`. Reordene os atendimentos atendendo primeiro todas as pessoas com `idade >= 60` (na ordem em que chegaram) e depois os demais clientes. Retorne a lista com os nomes ordenados.
* **Exemplo de Chamada:** `processar_fila([("Ana", 25), ("Bento", 67), ("Carla", 18), ("Daniel", 72)])`
* **Retorno Esperado:** `["Bento", "Daniel", "Ana", "Carla"]`

---

### Exercício 19: Detector de Picos Em Sequências
* **Objetivo:** Escreva uma função `encontrar_picos(numeros)` que encontre os elementos que são estritamente maiores que o seu vizinho da esquerda e o seu vizinho da direita. Retorne uma lista com os valores desses picos.
* **Exemplo de Chamada:** `encontrar_picos([1, 5, 2, 6, 3, 1, 8, 4])`
* **Retorno Esperado:** `[5, 6, 8]`

---

### Exercício 20: Algoritmo de Validação de Sequência de Transações (Jogo de Saldo)
* **Objetivo:** Escreva uma função `validar_extrato(saldo_inicial, transacoes)` utilizando um laço `while`. A lista contém inteiros positivos (depósitos) e negativos (saques). Se em algum momento do processamento o saldo ficar negativo, interrompa imediatamente a execução e retorne `"Extrato Inválido: Saldo Negativo na Posição X"` (onde X é o índice da transação). Se todas as transações forem processadas com sucesso, retorne `"Extrato Válido: Saldo Final R$ Y"`.
* **Exemplos de Chamada:**
  * `validar_extrato(100, [-50, -60, 20])` -> `"Extrato Inválido: Saldo Negativo na Posição 1"`
  * `validar_extrato(50, [30, -40, -20, 100])` -> `"Extrato Válido: Saldo Final R$ 120.00"`

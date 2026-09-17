# Lista de Exercícios: Estruturas Condicionais em Python
*(Pré-requisitos: Estruturas if/elif/else, operadores comparativos e lógicos: and, or, not)*

---

## 🟢 Nível 1: Exercícios Fáceis (5 Problemas)

### Exercício 1: Validador de Maioridade
* **Objetivo:** Escreva uma função chamada `verificar_maioridade` que receba o parâmetro `idade`.
* **Regra:** Se a idade for maior ou igual a 18, retorne `"Maior de idade"`. Caso contrário, retorne `"Menor de idade"`.
* **Exemplos de Chamada:**
  * `verificar_maioridade(20)` $\rightarrow$ `"Maior de idade"`
  * `verificar_maioridade(15)` $\rightarrow$ `"Menor de idade"`

---

### Exercício 2: Par ou Ímpar
* **Objetivo:** Escreva uma função chamada `verificar_paridade` que receba o parâmetro `numero`.
* **Regra:** Se o número for divisível por 2 (`numero % 2 == 0`), retorne `"Par"`. Caso contrário, retorne `"Ímpar"`.
* **Exemplos de Chamada:**
  * `verificar_paridade(7)` $\rightarrow$ `"Ímpar"`
  * `verificar_paridade(12)` $\rightarrow$ `"Par"`

---

### Exercício 3: Classificador de Número
* **Objetivo:** Escreva uma função chamada `classificar_numero` que receba `numero`.
* **Regra:** Retorne `"Positivo"`, `"Negativo"` ou `"Zero"`.
* **Exemplos de Chamada:**
  * `classificar_numero(-5)` $\rightarrow$ `"Negativo"`
  * `classificar_numero(0)` $\rightarrow$ `"Zero"`

---

### Exercício 4: Aprovado ou Reprovado
* **Objetivo:** Escreva uma função chamada `calcular_resultado` que receba `nota1` e `nota2`.
* **Regra:** Calcule a média das notas. Se a média for maior ou igual a 7.0, retorne `"Aprovado"`. Caso contrário, retorne `"Reprovado"`.
* **Exemplos de Chamada:**
  * `calcular_resultado(8.0, 6.0)` $\rightarrow$ `"Aprovado"`
  * `calcular_resultado(5.0, 6.5)` $\rightarrow$ `"Reprovado"`

---

### Exercício 5: Comparador de Dois Números
* **Objetivo:** Escreva uma função chamada `maior_de_dois` que receba `a` e `b`.
* **Regra:** Retorne `"O primeiro é maior"`, `"O segundo é maior"` ou `"São iguais"`.
* **Exemplos de Chamada:**
  * `maior_de_dois(10, 20)` $\rightarrow$ `"O segundo é maior"`
  * `maior_de_dois(5, 5)` $\rightarrow$ `"São iguais"`

---

## 🟡 Nível 2: Exercícios Médios (3 Problemas)

### Exercício 6: Sistema de Desconto de Loja
* **Objetivo:** Escreva uma função chamada `calcular_desconto` que receba `valor_compra` e `e_cliente_vip` (booleano).
* **Regra:** Se o cliente for VIP **OU** a compra for superior a R$ 200.00, conceda 15% de desconto. Caso contrário, conceda 5%. Retorne uma f-string com o valor final.
* **Exemplos de Chamada:**
  * `calcular_desconto(150.0, True)` $\rightarrow$ `"Valor final: R$ 127.50"`
  * `calcular_desconto(100.0, False)` $\rightarrow$ `"Valor final: R$ 95.00"`

---

### Exercício 7: Classificação Acadêmica
* **Objetivo:** Escreva uma função chamada `conceito_nota` que receba `nota`.
* **Regras:**
  * Nota de 9.0 a 10.0 $\rightarrow$ `"A"`
  * Nota de 7.0 a 8.9 $\rightarrow$ `"B"`
  * Nota de 5.0 a 6.9 $\rightarrow$ `"C"`
  * Nota abaixo de 5.0 $\rightarrow$ `"F"`
* **Exemplos de Chamada:**
  * `conceito_nota(8.5)` $\rightarrow$ `"B"`
  * `conceito_nota(4.2)` $\rightarrow$ `"F"`

---

### Exercício 8: Validador de Triângulos
* **Objetivo:** Escreva uma função chamada `tipo_triangulo` que receba os lados `a`, `b` e `c`.
* **Regras:**
  1. Verifique se os lados formam um triângulo válido: `(a + b > c) and (a + c > b) and (b + c > a)`.
  2. Se for válido, retorne `"Equilátero"` (todos os lados iguais), `"Isósceles"` (dois lados iguais) ou `"Escaleno"` (todos diferentes).
  3. Se não for válido, retorne `"Não é um triângulo"`.
* **Exemplos de Chamada:**
  * `tipo_triangulo(5, 5, 5)` $\rightarrow$ `"Equilátero"`
  * `tipo_triangulo(1, 2, 10)` $\rightarrow$ `"Não é um triângulo"`

---

## 🔴 Nível 3: Exercícios Difíceis (2 Problemas)

### Exercício 9: Calculadora de Imposto de Renda Progressivo
* **Objetivo:** Escreva uma função chamada `calcular_imposto` que receba `salario`.
* **Regras (Marginal/Progressivo):**
  * Até R$ 2000.00 $\rightarrow$ Isento (`0.0`)
  * De R$ 2000.01 até R$ 4000.00 $\rightarrow$ 10% sobre o que exceder R$ 2000.00
  * Acima de R$ 4000.00 $\rightarrow$ R$ 200.00 + 20% sobre o que exceder R$ 4000.00
* **Exemplos de Chamada:**
  * `calcular_imposto(1800.0)` $\rightarrow$ `0.0`
  * `calcular_imposto(3000.0)` $\rightarrow$ `100.0`
  * `calcular_imposto(5000.0)` $\rightarrow$ `400.0`

---

### Exercício 10: Validador de Ano Bissexto
* **Objetivo:** Escreva uma função chamada `e_bissexto` que receba `ano`.
* **Regra:** Um ano é bissexto se for divisível por 4, **EXCETO** se for divisível por 100, **A MENOS QUE** também seja divisível por 400. Retorne `True` ou `False`.
* **Exemplos de Chamada:**
  * `e_bissexto(2024)` $\rightarrow$ `True`
  * `e_bissexto(1900)` $\rightarrow$ `False`
  * `e_bissexto(2000)` $\rightarrow$ `True`
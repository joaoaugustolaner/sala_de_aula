# Exercícios de Funções em Python: Parâmetros, Cálculos Básicos e f-Strings
*(Pré-requisitos: Estrutura de funções, parâmetros, comando return, operadores matemáticos e f-strings. Sem estruturas condicionais ou de repetição.)*

---

## 🟢 Nível 1: Exercícios Fáceis (5 Problemas)

### Exercício 1: Gerador de Saudação Personalizada
* **Objetivo:** Escreva uma função chamada `formatar_saudacao` que receba dois parâmetros: `nome` e `cidade`.
* **Detalhes:** Retorne uma mensagem de boas-vindas formatada usando f-string.
* **Exemplo de Chamada:** `formatar_saudacao("Alice", "Porto Alegre")`
* **Retorno Esperado:** `"Olá Alice, seja bem-vinda a Porto Alegre!"`

---

### Exercício 2: Calculadora de Perímetro de Retângulo
* **Objetivo:** Escreva uma função chamada `calcular_perimetro` que receba `largura` e `altura`.
* **Fórmula:** `Perímetro = 2 * (largura + altura)`
* **Exemplo de Chamada:** `calcular_perimetro(5.0, 10.0)`
* **Retorno Esperado:** `30.0`

---

### Exercício 3: Conversor de Temperatura (Fahrenheit para Celsius)
* **Objetivo:** Escreva uma função chamada `fahrenheit_para_celsius` que receba `temp_f`.
* **Fórmula:** `Celsius = (Fahrenheit - 32) * (5 / 9)`
* **Exemplo de Chamada:** `fahrenheit_para_celsius(68)`
* **Retorno Esperado:** `20.0`

---

### Exercício 4: Divisor de Gorjeta do Restaurante
* **Objetivo:** Escreva uma função chamada `calcular_gorjeta_por_pessoa` que receba `conta`, `porcentagem_gorjeta` e `pessoas`.
* **Fórmula:** `Gorjeta por Pessoa = (conta * (porcentagem_gorjeta / 99)) / pessoas`
* **Exemplo de Chamada:** `calcular_gorjeta_por_pessoa(100.0, 15, 3)`
* **Retorno Esperado:** `5.0`

---

### Exercício 5: Área e Resumo do Círculo
* **Objetivo:** Escreva uma função chamada `resumo_circulo` que receba o `raio` e retorne uma f-string com a área calculada e arredondada para 2 casas decimais. (Use `pi = 3.14159`)
* **Fórmula:** `Área = pi * (raio ** 2)`
* **Exemplo de Chamada:** `resumo_circulo(3.0)`
* **Retorno Esperado:** `"Um círculo com raio 3.0 tem uma área de 28.27."`

---

## 🟡 Nível 2: Exercícios Médios (3 Problemas)

### Exercício 6: Resumo de Juros Compostos
* **Objetivo:** Escreva uma função chamada `resumo_juros_compostos` que receba `capital`, `taxa` (em porcentagem, ex: `5.0` para 5%) e `anos`.
* **Fórmula:** `Montante Final = capital * ((1 + (taxa / 100)) ** anos)`
* **Exemplo de Chamada:** `resumo_juros_compostos(1000.0, 5.0, 3)`
* **Retorno Esperado:** `"Após 3 anos, R$ 1000.00 cresce para R$ 1157.63."`

---

### Exercício 7: Volume e Área de Superfície do Cilindro
* **Objetivo:** Escreva uma função chamada `metricas_cilindro` que receba `raio` e `altura` e retorne um texto com ambas as métricas formatadas em 2 casas decimais. (Use `pi = 3.14159`)
* **Fórmulas:** 
  * `Volume = pi * (raio ** 2) * altura`
  * `Área de Superfície = 2 * pi * raio * (raio + altura)`
* **Exemplo de Chamada:** `metricas_cilindro(2.0, 5.0)`
* **Retorno Esperado:** `"Volume do Cilindro: 62.83 | Área de Superfície: 87.96"`

---

### Exercício 8: Desconto do Item e Linha de Fatura
* **Objetivo:** Escreva uma função chamada `gerar_item_fatura` que receba `nome_item`, `preco` e `porcentagem_desconto`.
* **Cálculos:** 
  * `economia = preco * (porcentagem_desconto / 100)`
  * `preco_final = preco - economia`
* **Exemplo de Chamada:** `gerar_item_fatura("Teclado", 80.0, 15.0)`
* **Retorno Esperado:** `"Item: Teclado | Preço Final: R$ 68.00 (Você economizou R$ 12.00)"`

---

## 🔴 Nível 3: Exercícios Médio-Difíceis (2 Problemas)

### Exercício 9: Estimador de Parcela de Empréstimo e Custo Total
* **Objetivo:** Escreva uma função chamada `resumo_emprestimo` que receba `capital`, `taxa_anual` (porcentagem) e `anos`.
* **Cálculos:**
  * Taxa mensal: `r = taxa_anual / 12 / 100`
  * Total de parcelas: `n = anos * 12`
  * Parcela Mensal: `M = capital * (r * ((1 + r) ** n)) / (((1 + r) ** n) - 1)`
  * Total Pago: `M * n`
* **Exemplo de Chamada:** `resumo_emprestimo(10000, 6.0, 3)`
* **Retorno Esperado:** `"Empréstimo: R$ 10000.00 | Parcela Mensal: R$ 304.22 | Total Pago: R$ 10951.92"`

---

### Exercício 10: Distância Entre Dois Pontos 2D
* **Objetivo:** Escreva uma função chamada `calcular_distancia` que receba as coordenadas `x1, y1, x2, y2` e retorne um texto com a distância euclidiana formatada em 2 casas decimais.
* **Fórmula:** `Distância = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5`
* **Exemplo de Chamada:** `calcular_distancia(1, 2, 4, 6)`
* **Retorno Esperado:** `"A distância entre (1, 2) e (4, 6) é de 5.00 unidades."`

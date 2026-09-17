# Lista de Exercícios Bônus: Condicionais Avançadas em Python
*(Pré-requisitos: if/elif/else aninhados, operadores lógicos compostos e precedência de avaliações)*

---

## 🔴 Nível 3: Exercícios Difíceis (5 Problemas)

### Exercício 1: Sistema de Avaliação Acadêmica Multicritério
* **Objetivo:** Escreva uma função `avaliar_estudante(p1, p2, frequencia, entregou_trabalho_extra)`.
* **Cálculo da Média:** `media = (p1 + p2) / 2`
* **Regras de Avaliação:**
  * Se `frequencia < 75`: Retorne `"Reprovado por Frequência"`.
  * Se `frequencia >= 75`:
    * Se `media >= 7.0`: Retorne `"Aprovado Direto"`.
    * Se `media` estiver entre `5.0` e `6.9`: Se `entregou_trabalho_extra == True`, adicione +1.0 ponto à média. Se a nova média for `>= 7.0`, retorne `"Aprovado com Trabalho Extra"`; caso contrário, retorne `"Exame Final"`.
    * Se `media < 5.0`: Retorne `"Reprovado por Nota"`.
* **Exemplos:**
  * `avaliar_estudante(6.0, 6.5, 80, True)` $\rightarrow$ `"Aprovado com Trabalho Extra"`
  * `avaliar_estudante(8.0, 9.0, 70, False)` $\rightarrow$ `"Reprovado por Frequência"`

---

### Exercício 2: Análise do Quadrante e Origem Cartesiana
* **Objetivo:** Escreva uma função `localizar_ponto(x, y)` que determine a posição exata de um ponto no plano cartesiano 2D sem usar laços ou vetores.
* **Regras:**
  * `x == 0` e `y == 0` $\rightarrow$ `"Origem"`
  * `x == 0` e `y != 0` $\rightarrow$ `"Eixo Y"`
  * `x != 0` e `y == 0` $\rightarrow$ `"Eixo X"`
  * `x > 0` e `y > 0` $\rightarrow$ `"Q1"`
  * `x < 0` e `y > 0` $\rightarrow$ `"Q2"`
  * `x < 0` e `y < 0` $\rightarrow$ `"Q3"`
  * `x > 0` e `y < 0` $\rightarrow$ `"Q4"`
* **Exemplos:**
  * `localizar_ponto(0, -5)` $\rightarrow$ `"Eixo Y"`
  * `localizar_ponto(-3, -4)` $\rightarrow$ `"Q3"`

---

### Exercício 3: Simulador de Tarifação Telefônica em Rolo
* **Objetivo:** Escreva uma função `calcular_fatura_telefone(minutos, gigas, e_estudante)`.
* **Regras de Cobrança:**
  * Plano Base: R$ 50.00 (inclui até 100 minutos e até 5 GB).
  * Minutos excedentes (acima de 100 min): R$ 0.50 por minuto adicional.
  * Dados excedentes (acima de 5 GB): R$ 10.00 por GB adicional.
  * Regra de Desconto: Se `e_estudante == True` **E** o valor total da fatura (com excedentes) for estritamente superior a R$ 100.00, aplique um desconto de R$ 20.00.
* **Retorno:** Retorne uma f-string formatada (ex: `"Fatura Final: R$ X.XX"`).
* **Exemplos:**
  * `calcular_fatura_telefone(120, 7, True)` $\rightarrow$ `"Fatura Final: R$ 60.00"` *(Cálculo: R$ 50 + 20*0.50 + 2*10 = R$ 80; como não passou de R$ 100, não aplica o desconto)*
  * `calcular_fatura_telefone(200, 10, True)` $\rightarrow$ `"Fatura Final: R$ 130.00"` *(Cálculo: R$ 50 + 100*0.50 + 5*10 = R$ 150 - R$ 20 = R$ 130)*

---

### Exercício 4: Validador de Elegibilidade para Seguro Auto
* **Objetivo:** Escreva uma função `avaliar_seguro(idade, anos_carteira, historico_acidentes)`.
* **Regras de Elegibilidade:**
  * Se `idade < 18` ou `anos_carteira < 1`: Retorne `"Não Elegível"`.
  * Se `historico_acidentes > 2`: Retorne `"Risco Alto: Recusado"`.
  * Se `historico_acidentes == 0`:
    * Se `idade >= 25` e `anos_carteira >= 3`: Retorne `"Aprovado: Categoria VIP"`.
    * Caso contrário: Retorne `"Aprovado: Categoria Padrão"`.
  * Se `historico_acidentes` for 1 ou 2: Retorne `"Aprovado: Categoria Alto Risco"`.
* **Exemplos:**
  * `avaliar_seguro(28, 5, 0)` $\rightarrow$ `"Aprovado: Categoria VIP"`
  * `avaliar_seguro(22, 2, 3)` $\rightarrow$ `"Risco Alto: Recusado"`

---

### Exercício 5: Ordenação de Três Valores sem Vetores/Laços
* **Objetivo:** Escreva uma função `ordenar_tres(a, b, c)` que receba três números inteiros e retorne uma string no formato `"menor, meio, maior"`.
* **Restrição:** É **proibido** utilizar funções nativas como `sorted()`, `min()`, `max()` ou estruturas de listas. Use puramente blocos `if/elif/else`.
* **Exemplos:**
  * `ordenar_tres(42, 9, 17)` $\rightarrow$ `"9, 17, 42"`
  * `ordenar_tres(5, 5, 2)` $\rightarrow$ `"2, 5, 5"`

---

## 🟣 Nível 4: Desafio Extremo (1 Problema Específico)

### Exercício 6: Motor de Validação Temporal e Validade de Data Completa
* **Objetivo:** Escreva uma função `validar_data_extenso(dia, mes, ano)` que valide se uma data informada é válida no calendário gregoriano e retorne sua formatação em extenso.
* **Restrição:** Não utilize módulos externos (como `datetime`).
* **Regras de Validação:**
  1. **Ano:** Deve ser um número inteiro estritamente maior que 0.
  2. **Ano Bissexto:** É bissexto se for divisível por 4, exceto múltiplos de 100, a menos que sejam múltiplos de 400.
  3. **Mês:** Deve estar entre 1 e 12.
  4. **Validação de Dias:**
     * Meses com 31 dias: 1 (Janeiro), 3 (Março), 5 (Maio), 7 (Julho), 8 (Agosto), 10 (Outubro), 12 (Dezembro).
     * Meses com 30 dias: 4 (Abril), 6 (Junho), 9 (Setembro), 11 (Novembro).
     * Mês 2 (Fevereiro): Possui 29 dias se o ano for bissexto; possui 28 dias se o ano **não** for bissexto.
* **Retorno da Função:**
  * Se a data for inválida (ex: 29/02/2023, 31/04/2026, 0/0/2000): Retorne `"Data Inválida"`.
  * Se a data for válida: Retorne a data em extenso no formato `"DD de [Nome do Mês] de AAAA"`.
* **Exemplos de Chamada:**
  * `validar_data_extenso(29, 2, 2024)` $\rightarrow$ `"29 de Fevereiro de 2024"`
  * `validar_data_extenso(29, 2, 2023)` $\rightarrow$ `"Data Inválida"`
  * `validar_data_extenso(31, 4, 2026)` $\rightarrow$ `"Data Inválida"`
  * `validar_data_extenso(15, 9, 2026)` $\rightarrow$ `"15 de Setembro de 2026"`
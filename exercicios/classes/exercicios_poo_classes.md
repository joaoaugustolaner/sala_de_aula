## 🟢 Nível 1: Fáceis - Estrutura Básica e Métodos (7 Exercícios)

### Exercício 1: Classe "Cachorro"
* **Objetivo:** Criar uma classe simples com atributos básicos e um método de ação.
* **Requisito:** A classe deve armazenar `nome`, `raca` e `idade`. Crie um método `latir()` que imprima uma mensagem na tela.
* **Estrutura Sugerida:**
  * **Atributos:** `nome`, `raca`, `idade`.
  * **Método:** `latir()` -> Imprime `"Au au! O {nome} está latindo."`.

---

### Exercício 2: Classe "Pessoa"
* **Objetivo:** Criar uma classe com um método que utiliza os atributos do próprio objeto.
* **Requisito:** A classe deve armazenar `nome` e `cidade`. Crie um método `apresentar()` que retorne uma string formatada.
* **Estrutura Sugerida:**
  * **Atributos:** `nome`, `cidade`.
  * **Método:** `apresentar()` -> Retorna `"Olá, meu nome é {nome} e moro em {cidade}."`.

---

### Exercício 3: Classe "Produto"
* **Objetivo:** Modificar o estado do objeto através de um método com parâmetro.
* **Requisito:** A classe armazena `nome` e `preco`. Crie um método `aplicar_desconto(percentual)` que subtraia o valor correspondente do preço original.
* **Estrutura Sugerida:**
  * **Atributos:** `nome`, `preco`.
  * **Método:** `aplicar_desconto(percentual)` -> `self.preco -= self.preco * (percentual / 100)`.

---

### Exercício 4: Classe "Retangulo"
* **Objetivo:** Criar uma classe focada em cálculos matemáticos usando atributos.
* **Requisito:** Armazene `base` e `altura`. Crie métodos para calcular a área e o perímetro.
* **Estrutura Sugerida:**
  * **Atributos:** `base`, `altura`.
  * **Métodos:** `calcular_area()` -> Retorna `base * altura`. `calcular_perimetro()` -> Retorna `2 * (base + altura)`.

---

### Exercício 5: Classe "ContaBancaria" (Simples)
* **Objetivo:** Controlar a soma de um valor numérico.
* **Requisito:** Armazene `titular` e `saldo` (inicializando sempre em 0 se não for passado). Crie um método `depositar(valor)`.
* **Estrutura Sugerida:**
  * **Atributos:** `titular`, `saldo` (padrão = 0).
  * **Método:** `depositar(valor)` -> Adiciona o valor ao saldo.

---

### Exercício 6: Classe "Carro"
* **Objetivo:** Gerenciar um estado booleano simples.
* **Requisito:** Armazene `marca`, `modelo` e `ligado` (bool). Crie métodos `ligar()` e `desligar()` que alterem esse estado.
* **Estrutura Sugerida:**
  * **Atributos:** `marca`, `modelo`, `ligado` (padrão = False).
  * **Métodos:** `ligar()` -> Define `ligado = True`. `desligar()` -> Define `ligado = False`.

---

### Exercício 7: Classe "Livro"
* **Objetivo:** Manipular a leitura de atributos.
* **Requisito:** Armazene `titulo`, `autor` e `numero_paginas`. Crie um método `exibir_resumo()` que retorne uma string com todos esses dados.
* **Estrutura Sugerida:**
  * **Atributos:** `titulo`, `autor`, `numero_paginas`.
  * **Método:** `exibir_resumo()` -> Retorna `"O livro {titulo} foi escrito por {autor} e possui {numero_paginas} páginas."`.

---

## 🟡 Nível 2: Médios - Lógica de Negócios e Validações (8 Exercícios)

### Exercício 8: Classe "Elevador"
* **Objetivo:** Validar limites antes de alterar o estado.
* **Requisito:** Armazene `andar_atual` e `total_andares`. Crie métodos `subir()` e `descer()`. O elevador não pode descer abaixo do térreo (0) nem subir acima do total de andares.
* **Estrutura Sugerida:**
  * **Atributos:** `andar_atual` (0), `total_andares`.
  * **Métodos:** `subir()`, `descer()` com `if` para garantir limites físicos.

---

### Exercício 9: Classe "Tamagotchi" (Bichinho Virtual)
* **Objetivo:** Interação entre múltiplos atributos.
* **Requisito:** Armazene `nome`, `fome` (0 a 100) e `energia` (0 a 100). Crie métodos `comer()` (diminui fome, aumenta energia) e `brincar()` (aumenta fome, diminui energia). Garanta que os valores fiquem entre 0 e 100.
* **Estrutura Sugerida:**
  * **Atributos:** `nome`, `fome`, `energia`.
  * **Métodos:** `comer()`, `brincar()`. Uso de `min()` e `max()` ou `if` para limitar a 100 e 0.

---

### Exercício 10: Classe "Estudante"
* **Objetivo:** Manipular listas como atributos.
* **Requisito:** Armazene `nome` e uma lista de `notas` (vazia no início). Crie `adicionar_nota(nota)`, `calcular_media()` e `verificar_aprovacao()` (média >= 7).
* **Estrutura Sugerida:**
  * **Atributos:** `nome`, `notas` (lista).
  * **Métodos:** `adicionar_nota(nota)` -> Faz append. `calcular_media()` -> `sum(notas) / len(notas)`.

---

### Exercício 11: Classe "ControleRemoto"
* **Objetivo:** Lógica encadeada.
* **Requisito:** Armazene `tv_ligada`, `canal_atual` e `volume`. Os métodos `aumentar_volume()` e `mudar_canal(canal)` só podem funcionar se `tv_ligada` for verdadeira.
* **Estrutura Sugerida:**
  * **Atributos:** `tv_ligada`, `canal_atual`, `volume`.
  * **Métodos:** `ligar_desligar()`, `aumentar_volume()`, `mudar_canal()`.

---

### Exercício 12: Classe "Funcionario"
* **Objetivo:** Cálculos condicionais.
* **Requisito:** Armazene `nome`, `cargo` e `salario`. Crie `aumentar_salario()`. Se o cargo for "Estagiario", aumento de 5%; caso contrário, aumento de 10%.
* **Estrutura Sugerida:**
  * **Atributos:** `nome`, `cargo`, `salario`.
  * **Método:** `aumentar_salario()` -> Usa `if self.cargo == "Estagiario"`.

---

### Exercício 13: Classe "Calculadora"
* **Objetivo:** Manter histórico de operações.
* **Requisito:** Uma lista interna `historico`. Crie métodos `somar(a, b)`, `subtrair(a, b)` e `mostrar_historico()`. Cada cálculo realizado deve salvar uma string (ex: "5 + 3 = 8") no histórico.
* **Estrutura Sugerida:**
  * **Atributos:** `historico` (lista vazia).
  * **Métodos:** `somar(a, b)`, `subtrair(a, b)`. Cada método faz `self.historico.append(f"{a} + {b} = {resultado}")`.

---

### Exercício 14: Classe "Relogio"
* **Objetivo:** Algoritmo circular e transbordo (overflow).
* **Requisito:** Armazene `hora`, `minuto` e `segundo`. Crie `avancar_tempo(segundos_extras)`. O método deve calcular corretamente o avanço, resetando segundos para minutos e minutos para horas, não passando de 23:59:59.
* **Estrutura Sugerida:**
  * **Atributos:** `hora`, `minuto`, `segundo`.
  * **Método:** `avancar_tempo(segundos)` -> Divisão inteira e módulo por 60 e 24.

---

### Exercício 15: Classe "MaquinaDeCafe"
* **Objetivo:** Gerenciamento de múltiplos recursos.
* **Requisito:** Armazene as quantidades de `agua`, `po_cafe` e `acucar` (inteiros representando gramas/ml). Crie `fazer_cafe()`. O café custa 200ml de água, 30g de pó e 10g de açúcar. Se faltar qualquer um, exiba um erro.
* **Estrutura Sugerida:**
  * **Atributos:** `agua`, `po_cafe`, `acucar`.
  * **Métodos:** `fazer_cafe()`, `abastecer_ingredientes()`. Validar usando `if agua >= 200 and ...`

---

## 🔴 Nível 3: Difíceis - Composição e Agregação de Objetos (6 Exercícios)
*(A partir daqui, crie classes que utilizam OBJETOS de outras classes como atributos).*

### Exercício 16: Autor e Livro
* **Objetivo:** Associação simples.
* **Requisito:** Crie uma classe `Autor` com `nome` e `nacionalidade`. Crie uma classe `Livro` com `titulo` e um atributo `autor`, que deve receber obrigatoriamente uma **instância** da classe `Autor`.
* **Método:** No Livro, crie `mostrar_detalhes()` que imprima o título e o nome/nacionalidade do autor acessando o objeto.
* **Estrutura Sugerida:**
  * **Classe 1:** `Autor(nome, nacionalidade)`
  * **Classe 2:** `Livro(titulo, autor)`. `self.autor` armazena o objeto Autor.
  * **Uso no método:** `self.autor.nome`.

---

### Exercício 17: Cliente e Endereço
* **Objetivo:** Separação de responsabilidades.
* **Requisito:** Crie `Endereco` (rua, numero, cidade). Crie `Cliente` (nome, telefone). O Cliente deve ter um método `adicionar_endereco(endereco)` que associe uma instância de Endereco ao cliente.
* **Método:** `exibir_perfil()` em Cliente, que verifica se existe um endereço cadastrado e imprime os dados completos.
* **Estrutura Sugerida:**
  * **Classe 1:** `Endereco(rua, numero, cidade)`
  * **Classe 2:** `Cliente(nome, telefone)`. Atributo interno `self.endereco = None`.
  * **Métodos:** `adicionar_endereco(obj_endereco)`.

---

### Exercício 18: Motor e Veiculo
* **Objetivo:** Delegação de métodos.
* **Requisito:** Crie `Motor` com atributo `ligado` e métodos `dar_partida()` e `desligar()`. Crie `Veiculo` que recebe o nome do modelo e instancia um `Motor` no seu próprio `__init__`.
* **Método:** `Veiculo` deve ter um método `acelerar()`. Só deve funcionar se acessar o motor e ele estiver `ligado`.
* **Estrutura Sugerida:**
  * **Classe 1:** `Motor()` -> `self.ligado`, `dar_partida()`.
  * **Classe 2:** `Veiculo(modelo)`. `self.motor = Motor()`.
  * **Métodos:** `acelerar()` usa `if self.motor.ligado:`

---

### Exercício 19: Produto e CarrinhoDeCompras
* **Objetivo:** Lista de objetos.
* **Requisito:** Crie `Produto` (nome, preco). Crie `CarrinhoDeCompras` que possua uma lista vazia de `itens`.
* **Métodos:** O Carrinho deve ter `adicionar_item(produto)` (recebe instância de Produto) e `calcular_total()`, que itera sobre a lista de objetos somando o `preco` de cada um.
* **Estrutura Sugerida:**
  * **Classe 1:** `Produto(nome, preco)`.
  * **Classe 2:** `CarrinhoDeCompras()`. `self.itens = []`.
  * **Métodos:** `adicionar_item(obj_produto)` faz `self.itens.append(obj)`. `calcular_total()` usa `sum(p.preco for p in self.itens)`.

---

### Exercício 20: Quarto e Hotel
* **Objetivo:** Busca em listas de objetos e alteração de estado interno.
* **Requisito:** Crie `Quarto` (numero, ocupado). Crie `Hotel` (nome), que deve instanciar uma lista de 10 Quartos no construtor.
* **Métodos:** O Hotel deve ter `reservar_quarto()`, que procura o primeiro `Quarto` na lista onde `ocupado == False`, altera para `True` e retorna o número do quarto. Se todos estiverem cheios, retorna aviso.
* **Estrutura Sugerida:**
  * **Classe 1:** `Quarto(numero)`. `self.ocupado = False`.
  * **Classe 2:** `Hotel(nome)`. `self.quartos = [Quarto(i) for i in range(1, 11)]`.
  * **Métodos:** `reservar_quarto()` usa um `for quarto in self.quartos:` verificando estado.

---

### Exercício 21: Passageiro e Voo
* **Objetivo:** Gestão completa de coleções limitadas.
* **Requisito:** Crie `Passageiro` (nome, passaporte). Crie `Voo` (numero_voo, capacidade_maxima).
* **Métodos:** Em Voo, crie uma lista `passageiros`. Crie o método `adicionar_passageiro(passageiro)`, que verifica o comprimento da lista: se for menor que a capacidade, adiciona a instância de Passageiro; se não, lança uma recusa. Crie `listar_passageiros()`.
* **Estrutura Sugerida:**
  * **Classe 1:** `Passageiro(nome, passaporte)`.
  * **Classe 2:** `Voo(numero_voo, capacidade)`. `self.passageiros = []`.
  * **Métodos:** `adicionar_passageiro(obj_passageiro)` usa `if len(self.passageiros) < self.capacidade`.
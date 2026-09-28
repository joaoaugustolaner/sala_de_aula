# Exercícios de Fixação: Herança e Polimorfismo em Python

*(Progressão: Desde a herança simples de atributos e sobrescrita de métodos até classes abstratas e herança múltipla.)*

---

## 🟢 Nível 1: Fáceis - Herança Básica e Sobrescrita Simples (7 Exercícios)

### Exercício 1: Classe "Animal" e "Gato"
* **Objetivo:** Criar uma classe filha que herda de uma classe mãe e sobrescreve um método.
* **Requisito:** Crie `Animal` com atributo `nome` e método `fazer_som()` (que imprime "Som de animal"). Crie a classe `Gato` que herda de `Animal` e sobrescreve `fazer_som()` para imprimir "Miau".
* **Estrutura Sugerida:**
  * **Classe Mãe:** `Animal(nome)` -> `fazer_som()`.
  * **Classe Filha:** `Gato(nome)` -> `fazer_som()`.

---

### Exercício 2: Classe "Veiculo" e "Moto"
* **Objetivo:** Adicionar novos atributos na classe filha.
* **Requisito:** Crie `Veiculo` com `marca` e `modelo`. Crie `Moto` que herda de `Veiculo` e adiciona o atributo `cilindradas`.
* **Estrutura Sugerida:**
  * **Classe Mãe:** `Veiculo(marca, modelo)`.
  * **Classe Filha:** `Moto(marca, modelo, cilindradas)`. O construtor deve inicializar os três atributos.

---

### Exercício 3: Classe "Pessoa" e "Aluno"
* **Objetivo:** Reaproveitamento de métodos da classe mãe.
* **Requisito:** Crie `Pessoa` com `nome` e `idade`, e um método `apresentar()`. Crie `Aluno` que herda de `Pessoa`, adiciona `matricula`, mas utiliza o método `apresentar()` herdado sem modificá-lo.
* **Estrutura Sugerida:**
  * **Classe Mãe:** `Pessoa(nome, idade)` -> `apresentar()`.
  * **Classe Filha:** `Aluno(nome, idade, matricula)`.

---

### Exercício 4: Classe "Funcionario" e "Gerente"
* **Objetivo:** Criação de métodos exclusivos da classe filha.
* **Requisito:** Crie `Funcionario` com `nome` e `salario`. Crie `Gerente` que herda de `Funcionario` e possui um método adicional `autorizar_pagamento()`.
* **Estrutura Sugerida:**
  * **Classe Mãe:** `Funcionario(nome, salario)`.
  * **Classe Filha:** `Gerente(nome, salario)` -> `autorizar_pagamento()`.

---

### Exercício 5: Classe "Conta" e "ContaPoupanca"
* **Objetivo:** Modificar o estado herdado usando um novo método.
* **Requisito:** Crie `Conta` com `titular` e `saldo`. Crie `ContaPoupanca` que herda de `Conta` e adiciona o método `render_juros(taxa)`, que aumenta o saldo atual com base na taxa.
* **Estrutura Sugerida:**
  * **Classe Mãe:** `Conta(titular, saldo)`.
  * **Classe Filha:** `ContaPoupanca(titular, saldo)` -> `render_juros(taxa)`.

---

### Exercício 6: Classe "Forma" e "Quadrado"
* **Objetivo:** Sobrescrita de cálculo matemático.
* **Requisito:** Crie `Forma` com um método genérico `area()` que retorna 0. Crie `Quadrado` que herda de Forma, recebe `lado` no construtor e sobrescreve `area()` para retornar `lado * lado`.
* **Estrutura Sugerida:**
  * **Classe Mãe:** `Forma()` -> `area()`.
  * **Classe Filha:** `Quadrado(lado)` -> `area()`.

---

### Exercício 7: Classe "Instrumento" e "Violao"
* **Objetivo:** Comportamento polimórfico básico.
* **Requisito:** Crie `Instrumento` com o método `tocar()`. Crie `Violao` que herda de Instrumento e altera o método `tocar()` para imprimir "Dedilhando as cordas do violão".
* **Estrutura Sugerida:**
  * **Classe Mãe:** `Instrumento()` -> `tocar()`.
  * **Classe Filha:** `Violao()` -> `tocar()`.

---

## 🟡 Nível 2: Médios - Uso de super() e Listas Polimórficas (8 Exercícios)

### Exercício 8: Ingresso e IngressoVIP
* **Objetivo:** Utilizar a função `super()` em métodos.
* **Requisito:** Crie `Ingresso` com `valor` e um método `exibir_valor()`. Crie `IngressoVIP` que herda de `Ingresso`. Sobrescreva `exibir_valor()` para adicionar uma taxa extra, mas chamando o método original ou acessando o atributo via `super()`.
* **Estrutura Sugerida:**
  * **Classe Mãe:** `Ingresso(valor)` -> `exibir_valor()`.
  * **Classe Filha:** `IngressoVIP(valor, taxa_extra)` -> `exibir_valor()` calcula `valor + taxa_extra`.

---

### Exercício 9: Empregado e Desenvolvedor
* **Objetivo:** Utilizar `super().__init__()` para inicialização.
* **Requisito:** Crie `Empregado` com `nome` e `salario_base`. Crie `Desenvolvedor` que recebe `nome`, `salario_base` e `linguagem_principal`. Use `super()` para inicializar nome e salário.
* **Estrutura Sugerida:**
  * **Classe Mãe:** `Empregado(nome, salario_base)`.
  * **Classe Filha:** `Desenvolvedor(nome, salario_base, linguagem_principal)`.

---

### Exercício 10: Polimorfismo de Pagamentos
* **Objetivo:** Executar o mesmo método em objetos de classes diferentes.
* **Requisito:** Crie a classe mãe `Pagamento` com método `processar()`. Crie as filhas `PagamentoCartao`, `PagamentoBoleto` e `PagamentoPix`. Sobrescreva `processar()` em todas. Crie uma lista contendo instâncias das três e um laço `for` que chame `processar()` para cada uma.
* **Estrutura Sugerida:**
  * **Classes Filhas:** `PagamentoCartao`, `PagamentoBoleto`, `PagamentoPix`.
  * **Polimorfismo:** `for pag em lista_pagamentos: pag.processar()`.

---

### Exercício 11: Personagem, Mago e Guerreiro
* **Objetivo:** Herança com lógicas de atributos diferentes.
* **Requisito:** Crie `Personagem` com `nome` e `vida`. Crie `Mago` (adiciona `mana`) e `Guerreiro` (adiciona `forca`). Sobrescreva um método `atacar()` onde o Mago gasta mana e o Guerreiro usa força bruta para calcular dano.
* **Estrutura Sugerida:**
  * **Classe Mãe:** `Personagem(nome, vida)`.
  * **Classes Filhas:** `Mago(nome, vida, mana)`, `Guerreiro(nome, vida, forca)`.

---

### Exercício 12: Produto, ProdutoFisico e ProdutoDigital
* **Objetivo:** Sobrescrita baseada em regras de negócio.
* **Requisito:** Crie `Produto` com `nome` e `preco`, e o método `calcular_total()`. Em `ProdutoFisico`, `calcular_total()` adiciona frete ao preço. Em `ProdutoDigital`, não há frete.
* **Estrutura Sugerida:**
  * **Classe Mãe:** `Produto(nome, preco)`.
  * **Classes Filhas:** `ProdutoFisico(nome, preco, peso)`, `ProdutoDigital(nome, preco)`.

---

### Exercício 13: Sistema de Notificações
* **Objetivo:** Iterar sobre diferentes canais de comunicação usando polimorfismo.
* **Requisito:** Crie `Notificacao` com método `enviar(mensagem)`. Crie `Email`, `SMS` e `PushNotification` herdando dela e sobrescrevendo `enviar()`. Crie uma função externa `disparar_alertas(lista_notificacoes, msg)` que chame o método de cada objeto.
* **Estrutura Sugerida:**
  * **Classes Filhas:** `Email`, `SMS`, `PushNotification`.
  * **Função Externa:** Espera uma lista de objetos do tipo Notificacao.

---

### Exercício 14: Transporte, Carro, Aviao e Navio
* **Objetivo:** Polimorfismo sem sobrescrever o construtor inteiro.
* **Requisito:** Crie `Transporte` com método `mover()`. Crie `Carro` (move nas vias), `Aviao` (move no ar), `Navio` (move na água). Teste em um laço `for`.
* **Estrutura Sugerida:**
  * **Classe Mãe:** `Transporte()` -> `mover()`.
  * **Classes Filhas:** Apenas sobrescrevem `mover()`.

---

### Exercício 15: Documento, PDF e Word
* **Objetivo:** Atributos de classe associados a herança.
* **Requisito:** Crie `Documento` com método `imprimir()`. Crie `PDF` e `Word`. O PDF deve imprimir na tela "Imprimindo arquivo .pdf" e o Word "Imprimindo arquivo .docx".
* **Estrutura Sugerida:**
  * **Classe Mãe:** `Documento(nome)`.
  * **Classes Filhas:** `PDF(nome)`, `Word(nome)` -> Sobrescrevem `imprimir()`.

---

## 🔴 Nível 3: Difíceis - Classes Abstratas, Mixins e Lógica Avançada (6 Exercícios)

### Exercício 16: Classe Abstrata FormaGeometrica
* **Objetivo:** Uso do módulo `abc` para forçar contratos.
* **Requisito:** Crie uma classe abstrata `FormaGeometrica` com os métodos abstratos `@abstractmethod` para `area()` e `perimetro()`. Crie as classes `Retangulo` e `Circulo` (usando `math.pi`) que implementem obrigatoriamente esses métodos.
* **Estrutura Sugerida:**
  * **Classe Abstrata:** Herda de `ABC`.
  * **Classes Filhas:** Obrigadas a implementar `area` e `perimetro`, caso contrário, erro de instanciação.

---

### Exercício 17: Herança Múltipla (Anfíbio)
* **Objetivo:** Combinar comportamentos de duas classes distintas.
* **Requisito:** Crie as classes `Terrestre` (método `andar()`) e `Aquatico` (método `nadar()`). Crie a classe `Anfibio` (ex: Sapo) que herda de AMBAS. A classe `Anfibio` deve ser capaz de chamar os dois métodos.
* **Estrutura Sugerida:**
  * **Classes Mães:** `Terrestre`, `Aquatico`.
  * **Classe Filha:** `Anfibio(Terrestre, Aquatico)`.

---

### Exercício 18: Conta Bancária Abstrata e Regras de Saque
* **Objetivo:** Polimorfismo complexo com regras de negócio e validações.
* **Requisito:** Crie `ContaBancaria` (Abstrata) com `depositar()` (concreto) e `sacar()` (abstrato). Crie `ContaCorrente` (cobra taxa fixa por saque) e `ContaPoupanca` (saque gratuito, mas não permite saldo negativo). Implemente o `sacar()` em ambas respeitando as regras.
* **Estrutura Sugerida:**
  * **Classe Abstrata:** `ContaBancaria(saldo)`.
  * **Classes Filhas:** `ContaCorrente`, `ContaPoupanca` (Lidando com os limites no `sacar`).

---

### Exercício 19: Mixin de Exportação
* **Objetivo:** Uso de classes "Mixin" para adicionar funcionalidades modulares.
* **Requisito:** Crie uma classe `ExportavelCSV` com um método `exportar_csv()` que retorna os atributos da classe em formato de texto separado por vírgulas. Crie a classe `Relatorio(titulo, dados)`. Faça `Relatorio` herdar de `ExportavelCSV` e use o método.
* **Estrutura Sugerida:**
  * **Mixin:** `ExportavelCSV` (Usa `self.__dict__` para pegar os dados).
  * **Classe Principal:** `Relatorio(ExportavelCSV)`.

---

### Exercício 20: Jogo e Inimigos Polimórficos
* **Objetivo:** Lógica de estado combinada com herança.
* **Requisito:** Crie `Inimigo` (abstrato) com método `receber_dano(qtd)`. Crie `Zumbi` (se chegar a 0 de vida, tem 1 chance de reviver com 50% de vida) e `Vampiro` (recebe 20% menos dano de qualquer ataque).
* **Estrutura Sugerida:**
  * **Classe Mãe:** `Inimigo(vida_maxima)`.
  * **Classes Filhas:** `Zumbi` (adiciona atributo `reviveu`), `Vampiro` (altera a matemática de `receber_dano`).

---

### Exercício 21: Sistema de Folha de Pagamento
* **Objetivo:** Sistema polimórfico gerador de relatórios.
* **Requisito:** Crie `Funcionario` (abstrato) com método `calcular_pagamento()`.
  * `Mensalista` herda e retorna um salário fixo.
  * `Horista` recebe horas trabalhadas e valor da hora.
  * `Comissionado` recebe salário base + comissão sobre vendas.
  Crie uma classe `FolhaDePagamento` que recebe uma lista de funcionários e imprime quanto cada um vai receber e o custo total da empresa.
* **Estrutura Sugerida:**
  * **Classe Mãe:** `Funcionario` (ABC).
  * **Filhas:** `Mensalista`, `Horista`, `Comissionado`.
  * **Classe Agregadora:** `FolhaDePagamento(lista_funcionarios)`.

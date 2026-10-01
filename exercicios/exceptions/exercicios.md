# Exercícios de Fixação: POO e Tratamento de Exceções em Python

*(Foco: Integração de classes com blocos `try`, `except`, `else`, `finally` e criação de Exceções Customizadas.)*

---

## 🟢 Nível 1: Fáceis - Tratamento de Erros Básicos em Métodos (7 Exercícios)

### Exercício 1: Calculadora Segura
* **Objetivo:** Capturar erro de divisão por zero.
* **Requisito:** Crie a classe `Calculadora` com o método `dividir(a, b)`. Use `try/except` para capturar `ZeroDivisionError` e retornar a mensagem "Erro: Divisão por zero".
* **Estrutura Sugerida:**
  * **Classe:** `Calculadora`.
  * **Método:** `dividir(a, b)` -> Retorna o resultado ou a string de erro.

### Exercício 2: Validador de Idade
* **Objetivo:** Evitar quebras de conversão de tipo.
* **Requisito:** Crie `Pessoa` com um método `definir_idade(valor_string)`. Tente converter a string para inteiro. Se falhar (`ValueError`), defina a idade como 0 e imprima um aviso.
* **Estrutura Sugerida:**
  * **Classe:** `Pessoa(nome)`.
  * **Método:** `definir_idade(valor)` -> Usa `int(valor)`.

### Exercício 3: Chamada de Alunos
* **Objetivo:** Capturar acesso a índices inexistentes.
* **Requisito:** Crie `Turma` contendo uma lista de nomes. Crie `chamar_aluno(indice)`. Use `try/except` para `IndexError`. Se o índice não existir, retorne "Aluno não encontrado".
* **Estrutura Sugerida:**
  * **Classe:** `Turma(lista_alunos)`.
  * **Método:** `chamar_aluno(indice)`.

### Exercício 4: Busca no Estoque
* **Objetivo:** Tratar ausência de chaves em dicionários.
* **Requisito:** Crie `Estoque` contendo um dicionário `{produto: quantidade}`. No método `consultar(produto)`, trate `KeyError` para retornar 0 quando o produto não estiver cadastrado.
* **Estrutura Sugerida:**
  * **Classe:** `Estoque(itens)`.
  * **Método:** `consultar(nome_produto)`.

### Exercício 5: Proteção de Tipos na Conta
* **Objetivo:** Capturar operações com tipos incompatíveis.
* **Requisito:** Crie `Conta` com `saldo`. No método `depositar(valor)`, use `try/except` para `TypeError`. Se o usuário passar uma string em vez de número, avise "Valor inválido para depósito".
* **Estrutura Sugerida:**
  * **Classe:** `Conta(titular, saldo)`.
  * **Método:** `depositar(valor)`.

### Exercício 6: Leitor de Configuração Fictício
* **Objetivo:** Tratar arquivos inexistentes.
* **Requisito:** Crie `Configuracao`. No método `carregar(nome_arquivo)`, tente abrir o arquivo. Trate `FileNotFoundError` retornando um dicionário padrão vazio `{}` e imprimindo "Arquivo ausente, usando padrão".
* **Estrutura Sugerida:**
  * **Classe:** `Configuracao()`.
  * **Método:** `carregar(nome_arquivo)`.

### Exercício 7: Atributo Inexistente
* **Objetivo:** Lidar com `AttributeError`.
* **Requisito:** Crie `Produto(nome)`. Crie uma função externa ou um método que tente imprimir `produto.preco`. Capture `AttributeError` e imprima "Atributo preço não definido nesta instância".
* **Estrutura Sugerida:**
  * **Classe:** `Produto(nome)`.
  * **Ação:** Tentar acessar `self.preco` dentro de um bloco try.

---

## 🟡 Nível 2: Médios - Exceções Customizadas e Blocos Completos (8 Exercícios)

### Exercício 8: Exceção SaldoInsuficienteError
* **Objetivo:** Criar a primeira exceção customizada.
* **Requisito:** Crie uma classe `SaldoInsuficienteError` herdando de `Exception`. Crie `ContaBancaria`. No método `sacar()`, dê um `raise SaldoInsuficienteError("Saldo menor que o saque")` se não houver fundos.
* **Estrutura Sugerida:**
  * **Exceção:** `class SaldoInsuficienteError(Exception): pass`.
  * **Classe:** `ContaBancaria` -> `sacar(valor)`.

### Exercício 9: Fechamento Garantido com `finally`
* **Objetivo:** Garantir a execução de limpeza.
* **Requisito:** Crie `ConexaoBanco` com métodos `conectar()`, `executar()` e `desconectar()`. O método `executar()` deve forçar um erro (ex: `1/0`). No script principal, use `try/finally` chamando `conectar()`, depois `executar()`, e garanta que `desconectar()` rode no `finally`.
* **Estrutura Sugerida:**
  * **Classe:** `ConexaoBanco`.
  * **Bloco:** Instancia, tenta usar, limpa no finally.

### Exercício 10: SenhaInvalidaError
* **Objetivo:** Validação com regras de negócio.
* **Requisito:** Crie `SenhaInvalidaError`. Crie `Usuario(login, senha)`. No construtor, verifique se a senha tem menos de 8 caracteres. Se tiver, levante a exceção. Capture essa exceção ao instanciar o objeto.
* **Estrutura Sugerida:**
  * **Exceção customizada:** Para erros de segurança.
  * **Classe:** Validação direto no `__init__`.

### Exercício 11: Sucesso Confirmado com `else`
* **Objetivo:** Usar o bloco `else` no tratamento.
* **Requisito:** Crie `ConversorMoeda`. No método `converter(valor_str)`, tente converter para float. Se falhar, `except ValueError`. Se der certo, use o bloco `else` para multiplicar pela cotação atual e retornar o valor.
* **Estrutura Sugerida:**
  * **Classe:** `ConversorMoeda()`.
  * **Bloco:** `try` (converte) -> `except` (avisa) -> `else` (calcula).

### Exercício 12: IdadeMinimaError em Eventos
* **Objetivo:** Proibir o ingresso de objetos inválidos em listas.
* **Requisito:** Crie `IdadeMinimaError`. Crie `Evento(idade_minima)` com uma lista de `participantes`. No método `adicionar(Pessoa)`, levante o erro se a pessoa for mais nova. Trate o erro para que o programa não pare, apenas ignore a adição.
* **Estrutura Sugerida:**
  * **Classes:** `Pessoa`, `Evento`.
  * **Lógica:** Levantamento e captura imediata do erro.

### Exercício 13: Múltiplas Exceções Físicas
* **Objetivo:** Um bloco `try` com vários `except`.
* **Requisito:** Crie `Termometro`. O método `registrar(temp)` recebe uma string. Ele deve converter para inteiro e salvar numa lista. Trate `ValueError` (se não for número) e `TypeError` (se for tipo complexo), exibindo mensagens diferentes para cada.
* **Estrutura Sugerida:**
  * **Classe:** `Termometro()`.
  * **Blocos:** `try` -> `except ValueError` -> `except TypeError`.

### Exercício 14: Relançamento de Exceções (`raise` dentro de `except`)
* **Objetivo:** Interceptar, logar e relançar.
* **Requisito:** Crie `Autenticador`. O método `login()` lança `Exception("Rede indisponível")`. Crie `App` que chama o autenticador. O `App` captura o erro, faz um print de "Log interno: falha de login" e usa `raise` sozinho para repassar o erro para a camada superior.
* **Estrutura Sugerida:**
  * **Ação:** `except Exception as e:` -> `print("Log")` -> `raise`.

### Exercício 15: Exceção de Limite de Estacionamento
* **Objetivo:** Condição de capacidade máxima.
* **Requisito:** Crie `EstacionamentoLotadoError`. Crie `Estacionamento(capacidade_maxima)`. Ao chamar `entrar_carro()`, levante a exceção se estiver cheio. Teste num laço `for` infinito que para apenas quando a exceção for capturada.
* **Estrutura Sugerida:**
  * **Laço Externo:** Usa `try/except` para sair do `while/for`.

---

## 🔴 Nível 3: Difíceis - Padrões Avançados e Hierarquia de Exceções (6 Exercícios)

### Exercício 16: Hierarquia de Exceções de Sistema
* **Objetivo:** Criar e tratar uma árvore de exceções.
* **Requisito:** Crie uma classe base `AppError(Exception)`. Dela, derive `NetworkError` e `DatabaseError`. Em uma classe `Servidor`, crie um método que gera um dos dois erros aleatoriamente. Trate apenas capturando `AppError` para pegar ambos genericamente.
* **Estrutura Sugerida:**
  * **Exceções:** `class NetworkError(AppError): pass`.
  * **Captura:** `except AppError:` abrange todos os filhos.

### Exercício 17: Encadeamento de Exceções (`raise from`)
* **Objetivo:** Preservar o histórico de erros (Traceback).
* **Requisito:** Crie `FalhaProcessamentoError`. Na classe `LeitorDados`, ao ocorrer um `ValueError` em uma conversão, capture-o e lance `raise FalhaProcessamentoError("Erro no arquivo") from e` (sendo `e` a exceção original).
* **Estrutura Sugerida:**
  * **Sintaxe:** `except ValueError as original:` -> `raise NovaExcecao() from original`.

### Exercício 18: Isolamento de Falhas em Lote (Carrinho Resiliente)
* **Objetivo:** Impedir que o erro de um objeto trave o processamento de outros.
* **Requisito:** Crie `ItemVenda(preco)`. No construtor, se `preco < 0`, levante `PrecoNegativoError`. Na classe `ProcessadorLote`, receba uma lista de preços (alguns negativos) e tente instanciar `ItemVenda`. Use `try/except` dentro de um laço para pular itens inválidos e somar os corretos.
* **Estrutura Sugerida:**
  * **Bloco:** `for` contendo um `try/except` interno para garantir continuidade (fail-safe).

### Exercício 19: Simulação de Context Manager Básico (`__enter__` e `__exit__`)
* **Objetivo:** Embutir o try/finally na própria classe.
* **Requisito:** Crie `ArquivoSeguro`. Implemente os métodos mágicos `__enter__` (imprime "Abrindo") e `__exit__` (imprime "Fechando"). Use-o com a instrução `with ArquivoSeguro():`. Provoque um erro de divisão por zero dentro do bloco `with` e prove que "Fechando" será impresso.
* **Estrutura Sugerida:**
  * **Classe:** Métodos de dunder para gerenciamento de contexto.

### Exercício 20: Transação Reversível (Rollback) no `except`
* **Objetivo:** Desfazer alterações parciais em caso de falha.
* **Requisito:** Crie `ContaTransferencia` com saldo. No método `transferir(destino, valor)`, deduz o valor da origem. Depois, provoque um erro forçado antes de depositar no destino. No bloco `except`, devolva o dinheiro para a conta de origem (rollback) e levante "Transferência falhou".
* **Estrutura Sugerida:**
  * **Lógica:** Guarda o estado, altera, tenta finalizar; se falhar, restaura o estado inicial no `except`.

### Exercício 21: Validação de Estado Duplo (Exceção de Máquina de Estado)
* **Objetivo:** Proibir transições inválidas de objetos.
* **Requisito:** Crie `PedidoStatusError`. Crie `Pedido` com status "Novo", "Pago", "Enviado". Se o método `enviar()` for chamado antes de `pagar()`, lance a exceção. Trate isso e exiba a mensagem: "Transição inválida".
* **Estrutura Sugerida:**
  * **Regras de Negócio:** Validar o estado atual antes de mutar os atributos.
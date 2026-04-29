# 🏦 VG Bank - Sistema Bancário em CLI

Bem-vindo ao repositório do VG Bank! Este é um projeto de estudo em Python que simula um sistema bancário operado via linha de comando (CLI).

Este projeto marca o início da minha jornada na programação, saindo da "estaca zero" em uma transição de carreira da área jurídica para a tecnologia. O desenvolvimento é focado na autonomia e na aplicação prática de conceitos fundamentais.

> ⚠️ **Nota sobre o direcionamento do projeto:** O foco do VG Bank se desviou parcialmente da intenção original. Com o início do bootcamp **Luizalabs - Back-end com Python - 2ª Edição** da [DIO](https://www.dio.me/), grande parte do código foi adaptada para estar em conformidade com os desafios propostos pelo programa. O projeto continua sendo desenvolvido de forma autônoma, mas agora também serve como entrega prática do bootcamp.

Dado o foco do projeto ser os estudos de Python, e não uma aplicação real, destaco que ferramentas de Inteligência Artificial foram utilizadas somente para dicas e resolução de erros, não tendo absolutamente nenhuma linha de código neste projeto escrita por IA.

---

## 🚀 Sobre o Projeto

O VG Bank foi construído para aplicar conceitos de lógica de programação, manipulação de arquivos e orientação a objetos. Atualmente, o sistema permite o cadastro de novos clientes com validação de dados, armazenamento em arquivos de texto e uma interface básica de administração.

---

## 🛠️ Tecnologias e Ferramentas

- **Linguagem:** Python 3.14.3
- **Persistência:** Arquivos de texto (.txt) (**DESCONTINUADO!!!**)

---

## 📂 Estrutura de Arquivos

- **main.py** — Ponto de entrada do aplicativo. Gerencia os menus de acesso para Clientes e Administradores.
- **Cliente.py** — Contém as classes `Conta`, `Cliente`, `pessoaFisica` e as classes de transação. Toda a lógica de dados e validação vive aqui.
- **Administrador.py** — Módulo responsável pelas funções de gestão, como listagem e deleção de usuários.
- **usuarios.txt** — O "banco de dados" simplificado onde as informações são persistidas. (**DESCONTINUADO!!!**)

---

## 🧠 Aprendizados Técnicos

Neste estágio do projeto, foquei em dominar:

- **Orientação a Objetos (POO):** Criação de classes, herança (`pessoaFisica` herdando de `Cliente`) e encapsulamento com atributos privados.
- **Getters e Setters:** Uso de `@property` e `@atributo.setter` para controlar o acesso e a validação dos dados diretamente na atribuição.
- **Tratamento de Erros:** Uso de `try/except` para capturar `ValueError` e loops `while` para repetir a coleta de dados até que sejam válidos.
- **Manipulação de Arquivos:** Uso do gerenciador de contexto `with open` e modos de escrita para garantir persistência dos dados. (**DESCONTINUADO!!!**)
- **Modularização:** Divisão do código em diferentes arquivos para manter a organização.

---

## 📈 Próximos Passos (Roadmap)

- [ ] Implementar sistema de Login com validação por CPF ou número de conta.
- [x] Adicionar funções de Depósito, Saque e Transferência.
- [x] Completar as classes `contaCorrente`, `Historico`, `Saque` e `Deposito`.
- [ ] Migrar a persistência de `.txt` para um banco de dados SQLite. (**.txt DESCONTINUADO!!!, futuro banco de dados permanece!!**)
- [ ] Adicionar mais validadores para prevenção da integridade do sistema na criação do cliente(por exemplo, na hipótese do usuário inserir somente os dois últimos digitos da data)

---

## 📋 Log de Alterações
### V0.4
- **Roteamento com match/case:** Implementação da função selecao_menu no main.py, utilizando a estrutura de match/case para gerenciar a navegação entre os diferentes módulos do sistema (IN, PA, CL, CO, TR, AD).

- **Interface visual em ASCII:** Atualização dos menus e mensagens de confirmação com molduras gráficas e uso de emojis para indicar o status das operações (sucesso, erro ou alerta).(IMPORTANTE! A parte visual dos menus foi feita por IA(Prompt usado: "Me retorne os arquivos cliente e main com menus mais bonitos e dentro do padrão alto do mercado hoje, lembrando que suas mudanças são SOMENTE VISUAIS NAS STRINGS, e nada além disso"))

- **Ajuste na herança de contas:** Correção do método @classmethod nova_conta na classe contaCorrente para incluir os parâmetros de limite e limite_saques, garantindo a criação correta do objeto conforme os requisitos do projeto.

### V0.3
- **Reestruturação completa do Cliente.py:** A classe única `Cliente` foi substituída por uma hierarquia de classes — `Conta`, `contaCorrente`, `Cliente`, `pessoaFisica`, `Historico`, `Transacao`, `Saque` e `Deposito` — alinhando o projeto aos requisitos do bootcamp DIO.
- **Encapsulamento com getters e setters:** Os atributos de `pessoaFisica` (nome, CPF, data de nascimento) e de `Conta` (saldo) passaram a usar `@property` e setters com validação, impedindo que dados inválidos sejam atribuídos diretamente.
- **Validações implementadas:** CPF (11 dígitos numéricos), nome (mínimo 3 caracteres, sem especiais), data de nascimento (formato DDMMAAAA, maioridade), e saldo (apenas numérico).
- **Tratamento de erros no cadastro:** O fluxo de `primeiro_acesso` no `main.py` passou a usar `try/except ValueError` dentro de um loop `while`, repetindo a coleta de dados até que todos sejam válidos.

### V0.2
- **Separação da conversa com o usuário:** Os comandos de `input()` foram retirados de dentro das funções do arquivo `Cliente.py`. Agora, quem faz as perguntas ao usuário é o `main.py`.
- **Envio de dados por parâmetros:** A função de cadastrar agora recebe as informações prontas, sem precisar interagir com o teclado diretamente.
- **Correção no salvamento de arquivos:** A função de salvar foi ajustada para receber o usuário recém-criado e escrever corretamente no `usuarios.txt`.
- **Fluxo de boas-vindas direto:** O `main.py` passou a usar os dados do objeto criado para exibir a mensagem de boas-vindas, sem precisar reler o arquivo.


🏦 VG Bank - Sistema Bancário em CLI
Bem-vindo ao repositório do VG Bank! Este é um projeto de estudo em Python que simula um sistema bancário operado via linha de comando (CLI).

Este projeto marca o início da minha jornada na programação, saindo da "estaca zero" em uma transição de carreira da área jurídica para a tecnologia. O desenvolvimento é focado na autonomia e na aplicação prática de conceitos fundamentais.

Dado o foco do projeto ser os estudos de Python, e não uma aplicação real, destaco que ferramentas de Inteligência Artificial, nesse caso, o Gemini, foi utilizado somente para dicas e resolução de erros, não tendo absolutamente nenhuma linha de código neste projeto escrito por IA.

🚀 Sobre o Projeto
O VG Bank foi construído para aplicar conceitos de lógica de programação, manipulação de arquivos e orientação a objetos. Atualmente, o sistema permite o cadastro de novos clientes, armazenamento de dados em arquivos de texto e uma interface básica de administração.

🛠️ Tecnologias e Ferramentas
Linguagem: Python 3.14.3

Ambiente de Estudo: 

Persistência: Arquivos de texto (.txt)

📂 Estrutura de Arquivos
O projeto é modularizado para facilitar a manutenção e o crescimento do sistema:

main.py: O ponto de entrada do aplicativo. Gerencia os menus de acesso para Clientes e Administradores.

Cliente.py: Contém a classe Cliente e a lógica de cadastro (primeiro acesso).

Administrador.py: Módulo responsável pelas funções de gestão, como listagem e deleção de usuários.

usuarios.txt: O "banco de dados" simplificado onde as informações são persistidas.

🧠 Aprendizados Técnicos
Neste estágio do projeto, foquei em dominar:

Orientação a Objetos (POO): Criação de classes e métodos construtores para moldar os dados do cliente.

Manipulação de Arquivos: Uso do gerenciador de contexto with open e modos de escrita (a para append) para garantir que os dados não sejam perdidos.

Modularização: Divisão do código em diferentes arquivos para manter a organização.

Lógica de Fluxo: Implementação de loops while e condicionais para navegação no menu.

📈 Próximos Passos (Roadmap)
O VG Bank é um projeto vivo. Minhas próximas metas de estudo incluem:

[ ] Implementar sistema de Login com validação de e-mail.

[ ] Adicionar funções de Depósito, Saque e Transferência.

[ ] Criar tratamento de erros (Exceções) para tornar o sistema mais robusto.

[ ] Migrar a persistência de .txt para um banco de dados SQLite.

Log de alterações

##V0.2 

Separação da conversa com o usuário: Os comandos de input() foram retirados de dentro das funções do arquivo Cliente.py. Agora, quem faz as perguntas ao usuário é o main.py, deixando o código mais limpo.

Envio de dados por parâmetros: A função de cadastrar agora recebe as informações (nome, e-mail, etc.) prontas. Ela não precisa mais "parar" para perguntar nada ao teclado; ela apenas processa o que recebe do main.py.

Correção no salvamento de arquivos: A função de salvar foi ajustada para receber o usuário que acabou de ser criado. Isso resolveu o erro onde o sistema não conseguia acessar os dados do cliente para escrever no usuarios.txt.

Fluxo de boas-vindas direto: Assim que o usuário termina o cadastro, o main.py já consegue usar o nome e o e-mail registrados para mostrar na tela, sem precisar ler o arquivo de novo.



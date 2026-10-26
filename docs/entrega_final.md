# Entrega final da TechBairro

**Aluno(a):** Gustavo Nunes Silva  
**Versão entregue:** 3.3.3

**Por que esse número de versão:** A versão 3.3.3 identifica a versão final entregue do projeto, mantendo o histórico de alterações registrado no CHANGELOG.

| # | Item | Evidência |
|---|---|---|
| 1 | A aplicação funciona: os 6 casos de teste passaram | `docs/registro_de_testes.md` |
| 2 | A versão aparece na janela e é a mesma do CHANGELOG e do README | Janela principal da aplicação, `CHANGELOG.md` e `README.md` |
| 3 | O pacote foi testado numa pasta limpa | Registro do teste de execução do pacote em uma pasta fora do projeto original |
| 4 | Tag e release publicadas, com o `.zip` anexado | Link da release: **https://github.com/Gustavo-gns/TechBairro/releases/tag/v3.3.3** |
| 5 | O repositório não tem banco, `__pycache__` nem `dist` | Saída do comando `git ls-files` e conferência dos arquivos do repositório |
| 6 | O histórico tem commits com mensagens claras | Link dos commits: **https://github.com/Gustavo-gns/TechBairro/commits/main/** |
| 7 | README, manual de uso e `requirements.txt` estão no repositório | `README.md`, arquivo do manual de uso e `requirements.txt` |
| 8 | A Issue "Teste do README" (Aula 26) está fechada | Link da Issue fechada: **https://github.com/Gustavo-gns/TechBairro/issues/1** |

## Roteiro da apresentação

| Bloco | Tempo | O que vou mostrar ou dizer |
|---|---|---|
| 1. Problema e solução | 30 s | A TechBairro foi criada para facilitar o cadastro e o gerenciamento de clientes. Com ela, é possível cadastrar, consultar, editar e excluir registros de clientes. |
| 2. Demonstração ao vivo | 1 min 30 s | Vou mostrar a consulta de clientes, cadastrar um novo cliente, consultar seus dados, editar uma informação e excluir o registro. Por último, vou tentar cadastrar um dado inválido para demonstrar a validação. |
| 3. Como foi construída | 30 s | O projeto foi desenvolvido em Python, com Tkinter para a interface gráfica e SQLite para armazenar os dados. Também utilizei Git e GitHub para versionar o código e organizar as versões do projeto. |
| 4. Aprendizado | 30 s | Uma dificuldade foi garantir que o banco de dados fosse acessado no local correto. Resolvi isso utilizando o caminho baseado no arquivo Python. Também aprendi a importância de testar as funcionalidades e registrar as alterações do projeto. |

**Plano B para a apresentação:** Se alguma funcionalidade falhar durante a demonstração, vou explicar o que deveria acontecer e utilizar capturas de tela ou registros dos testes como evidência. Também vou deixar a aplicação aberta, com clientes cadastrados, antes de começar.

## Parte 6 — Autoavaliação

A apresentação foi organizada para mostrar as principais funcionalidades da TechBairro dentro do tempo disponível. Eu mudaria a forma de explicar algumas etapas para deixar a demonstração ainda mais clara e rápida. O comentário mais útil dos colegas foi sobre explicar melhor a validação de dados durante a demonstração, popr conta que eu realmente não estava entendendo muito bem.

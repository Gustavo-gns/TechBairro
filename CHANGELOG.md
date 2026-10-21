# Changelog da TechBairro

## v3.3.3 (aula 25)

### Adicionado
- Código publicado no GitHub, com histórico de versões.

---

## v3.3.2 (Aula 24)

### Adicionado
- Versionamento do código com o Git.

---

## v3.3.1 (aula 21)

### Alterado
- Partes do sistema foram divididas em módulos, para facilitar futuras manutenções.

---

## v3.3 (alteração própria)

### Adicionado
- Barra de pesquisa para achar um cliente na tela de consulta

---

## v3.2 (aula 20)

### Adicionado
- Duplo clique em algum cliente abre automaticamente a tela de edição do mesmo.
- Clique em algum cliente e depois clique na tecla delete inicia o procedimento de exclusão do mesmo.

### Verificações
- Foi verificado o comportamento da edição e da tela de consulta, e possíveis erros que poderiam acontecer não aconteceram, portanto já foram corrigidos em versões anteriores.

---

## v3.1.1 (Aula 18)

### Adicionado
- Script scripts/gerar_pacote.py, que compacta o projeto em um arquivo zip.
- Arquivo COMO_EXECUTAR.txt, com as instruções de como rodar o projeto.
- Separar o arquivo utils.py na sua própria pasta.

---

## v3.1 (Aula 16)

### Alterado
- O banco agora é aberto pelo caminho completo (`os.path` + `__file__`), sempre na pasta do projeto, não importa de onde o programa seja executado.

### Adicionado
- Mensagem "Banco em uso" no terminal, mostrando qual arquivo de banco está sendo usado.

---

## v3.0 (Aula 14)

### Alterado
- O GerenciadorClientes deixou de guardar os clientes numa lista em memória e passou a gravar no banco SQLite `techbairro.db`.
- Os clientes passaram a ter um ID único no banco de dados.
- As operações de cadastro, consulta, edição e exclusão passaram a ser feitas usando o banco de dados.

### Adicionado
- Banco de dados SQLite com a tabela de clientes.

---

## v2.0 (Aulas 11 e 12)

### Adicionado
- Classes `Client` e `ClientManager` para organizar os dados e as funções dos clientes.
- Tela de Consulta de Clientes, com lista dos clientes cadastrados e botões para editar e excluir.

---

## Antes da v2.0 (Aulas 5 a 10)

- Foram criadas as telas do sistema, os eventos dos botões e as funções para cadastrar e consultar clientes.
- Foram adicionadas validações para verificar se os dados informados pelo usuário estavam corretos.
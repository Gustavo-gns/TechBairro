# TechBairro
TechBairro é um sistema de cadastro da associação de moradores.

**Versão atual:** 3.3.3 · Histórico de mudanças no [CHANGELOG](CHANGELOG.md)

## Funcionalidades

- Cadastrar Clientes
- Exibir Clientes
- Pesquisar Clientes
- Editar e Excluir Clientes

## Requisitos para execução

| Item | Requisito |
|---|---|
| Sistema operacional | Windows 10/11 ou Linux |
| Python | 3.12 em diante (versões testadas: 3.12 e 3.14.6) |
| Tkinter | Python 3.11 em diante |
| Bibliotecas externas | Nenhuma |
| Internet | Sem uso necessário |

## Instalação

1. **Baixando e instalando através do download ZIP através do GitHub:** Acesse o repositório no GitHub, clique em **Code → Download ZIP** e extraia o conteúdo do arquivo ZIP baixado. Em seguida, abra o terminal dentro da pasta extraída e execute: 
    ```Bash
    pip install -r requirements.txt
    python main.py
    ```

2. **Baixando com o git clone:** Abra o terminal na pasta em que deseja salvar o projeto e execute:
    ```Bash
    git clone https://github.com/Gustavo-gns/TechBairro.git
    cd TechBairro
    ```
    Depois instale as dependências, logo executando o programa com `python main.py`:
    ```Bash
    pip install -r requirements.txt
    python main.py
    ```

3. **O que deve aparecer ao abrir o programa:** Após executar o comando, a pessoa deverá visualizar a janela da aplicação desktop. No terminal, deverá aparecer a mensagem `Banco em uso:` (seguido da localização dele), indicando que o programa está utilizando o banco de dados.

## Configuração do banco de dados

O banco de dados utilizado pelo programa fica na pasta principal do projeto, denomidado de techbairro.db quando criado. Ele é criado automaticamente pelo sistema ao abrí-lo, pois por ter dados sensíveis ele não pode ser versionado. O banco usado para algum processo do sistema aparece no terminal onde foi aberto o programa.

Para evitar a perda dos dados cadastrados no sistema, é importante realizar cópias de segurança (backups) do banco de dados. Para isso, na pasta scripts, há o arquivo [gerar_backup.py](scripts/gerar_backup.py) que gera uma pasta com um backup do banco de dados.

## Como usar

O passo a passo está no [Manual de uso](docs/manual_de_uso.md).

## Estrutura do projeto

### Pastas

1. **`docs/`**: contém documentos importantes do projeto, como manuais, diagramas e documentação técnica.
2. **`scripts/`**: contém scripts auxiliares para tarefas como geração de backups, criação de pacotes, importação de dados e verificação do banco de dados.
3. **`system/`**: contém os principais módulos do sistema, responsáveis pelo gerenciamento dos clientes, acesso ao banco de dados e validação de informações.

### Arquivos

1. **`.gitignore`**: define quais arquivos e pastas devem ser ignorados pelo Git, evitando o versionamento de arquivos desnecessários ou que contenham dados locais.
2. **`CHANGELOG.md`**: registra as alterações realizadas no projeto a cada versão.
3. **`COMO_EXECUTAR.txt`**: apresenta as instruções necessárias para executar o sistema.
4. **`main.py`**: arquivo principal, responsável por iniciar o programa.
5. **`README.md`**: apresenta o projeto, suas funcionalidades, sua estrutura e as instruções de utilização.
6. **`requirements.txt`**: lista as dependências necessárias para executar o projeto.
7. **`techbairro.db`**: arquivo do banco de dados SQLite, onde são armazenados os dados cadastrados no sistema.
8. **`validation_test.py`**: contém testes relacionados à validação das informações inseridas no sistema.

## Autor

**Autor:** Gustavo Nunes Silva

**Curso:** Técnico em Desenvolvimento de Sistemas

**Instituição:** Senac
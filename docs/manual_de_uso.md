# Manual de uso da TechBairro

## A tela principal

A janela principal do TechBairro apresenta quatro campos para preenchimento: Nome, Telefone, E-mail e Endereço. Também possui os botões **Salvar**, **Limpar** e **Consultar clientes**, um contador que informa a quantidade de clientes cadastrados e uma área para exibir mensagens de sucesso ou erro. A versão atual do sistema aparece no canto inferior direito.

## Cadastrar um cliente

1. Preencha os campos com os dados do cliente.
2. Clique no botão **Salvar** para cadastrar o cliente.
3. Caso algum dado seja inválido, corrija os campos indicados pelo sistema.
4. Após o cadastro, uma mensagem de confirmação será exibida e o contador será atualizado.

## Consultar os clientes cadastrados

1. Clique no botão **Consultar clientes** para abrir a janela de consulta.
2. Utilize a barra de pesquisa para localizar clientes.
3. Os registros correspondentes serão exibidos na lista.
4. Para voltar à tela principal, feche a janela de consulta.

## Alterar os dados de um cliente

1. Abra a tela de consulta clicando em **Consultar clientes**.
2. Selecione o cliente que deseja alterar.
3. Clique em **Editar** ou dê dois cliques sobre o registro.
4. Altere os dados desejados nos campos da janela de edição.
5. Clique em **Salvar** para confirmar as alterações ou em **Cancelar** para fechar a janela sem salvar.
6. Após salvar, uma mensagem de confirmação será exibida.

## Excluir um cliente

1. Abra a tela de consulta clicando em **Consultar clientes**.
2. Selecione o cliente que deseja excluir.
3. Clique em **Excluir** ou pressione a tecla **Delete**.
4. Confira os dados apresentados e confirme a exclusão.
5. Após a exclusão, o registro será removido e o contador de clientes será atualizado.

## Regras de preenchimento

| Campo | Obrigatório? | Regra |
|---|---|---|
| Nome | Sim | Não vazio |
| Telefone | Sim | Números, espaços e traços permitidos, mas o mínimo de seis números e máximo de quinze |
| E-mail | Sim | Seguir o formato nome@dominio.com |
| Endereço | Sim | Não vazio |

## Mensagens do sistema

| Mensagem | O que significa | O que fazer |
|---|---|---|
| O cadastro de [nome] foi feito com sucesso! | O cliente foi cadastrado no banco de dados. | Nenhuma ação necessária. |
| Edição de [nome] feita com sucesso! | Os dados do cliente foram atualizados. | Nenhuma ação necessária. |
| Nenhum cliente cadastrado | Não existem clientes cadastrados no sistema. | Cadastre um cliente antes de consultar os registros. |
| Nenhum cliente encontrado. | A pesquisa não encontrou registros correspondentes. | Verifique o texto pesquisado ou tente outra pesquisa. |
| Selecione algum registro para prosseguir! | Nenhum cliente foi selecionado para edição ou exclusão. | Selecione um cliente na lista. |
| Termine de editar primeiro! | Já existe uma janela de edição aberta. | Termine a edição antes de abrir a consulta novamente. |
| Tela de consulta já aberta! | A janela de consulta já está aberta. | Utilize a janela existente. |
| Registro de [nome] excluído! | O cliente foi removido do banco de dados. | Nenhuma ação necessária. |
| Deseja realmente excluir o registro...? | O sistema solicita a confirmação da exclusão. | Confirme somente se quiser excluir o cliente. |
| Erro ao acessar o banco: [erro] | Ocorreu um problema ao acessar ou modificar o banco de dados. | Verifique o banco de dados e consulte os detalhes do erro. |
| Nome inválido | O nome informado não passou pela validação. | Preencha o nome. |
| Telefone inválido | O telefone informado não passou pela validação. | Corrija o telefone informado. |
| Email inválido | O email informado não passou pela validação. | Corrija o email conforme as regras de preenchimento. |
| Endereço inválido | O endereço informado não passou pela validação. | Preencha o endereço. |

## Dúvidas frequentes

**Como cadastrar um cliente?**

Preencha os campos do formulário e clique em **Salvar**. Se houver informações inválidas, o sistema indicará os campos que precisam ser corrigidos.

**Como consultar um cliente?**

Clique em **Consultar clientes** para abrir a lista de registros. Utilize a barra de pesquisa para localizar um cliente.

**Como editar ou excluir um cliente?**

Na tela de consulta, selecione o cliente desejado. Clique em **Editar** para alterar seus dados ou em **Excluir** para solicitar a exclusão. A exclusão exige confirmação.

**O que fazer se ocorrer um erro no banco de dados?**

Verifique se o arquivo do banco está no caminho esperado pelo sistema e se ele pode ser acessado. Se necessário, utilize uma cópia de segurança para recuperar os dados.
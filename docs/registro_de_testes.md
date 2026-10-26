# Registro de testes da TechBairro

Versão testada: 3.3.3 · Data: 26/07/2026 · Responsável: Gustavo Nunes Silva

Sistema operacional e versão do Python: Windows 11 / Python 3.12

| ID | Requisito | Passos e dados | Esperado | Obtido | Status |
|---|---|---|---|---|---|
| CT01 | RF01 | Cadastrar um cliente com todos os campos certos | Cadastrar normalmente | Cadastra normalmente | Correto |
| CT02 | RF01 | Salvar com Nome e Endereço vazios | Retornar os campos como inválidos | Retorna os campos como inválidos | Correto |
| CT03 | RF02 | Telefone 61 9999 0000 (com espaços) | Cadastrar o cliente normalmente | Cadastra o cliente normalmente | Correto |
| CT04 | RF03 | E-mail ana@email (sem ponto) | Retornar E-mail como inválido | Retorna E-mail como inválido | Correto |
| CT05 | RF05 | Editar um cliente, trocar o telefone e salvar | Depois de abrir a tela de consulta o cliente aparecer com o número editado | Depois de abrir a tela de consulta o cliente aparecer com o número editado | Correto |
| CT06 | RF06 | Excluir um cliente: responder Não, depois Sim | Não excluir da primeira vez, mas na segunda sim | Não exclui da primeira vez, mas na segunda sim | Correto |

## Testes automáticos

Saída do `python validation_test.py`: OK teste_cliente_valido
```Bash
Traceback (most recent call last):
  File "c:\Users\gustavo62101496\OneDrive - SENAC DF\Área de Trabalho\TDS_GustavoNunes\UC5\TechBairro_OwnVersion\validation_test.py", line 55, in <module>
    funcao()
  File "c:\Users\gustavo62101496\OneDrive - SENAC DF\Área de Trabalho\TDS_GustavoNunes\UC5\TechBairro_OwnVersion\validation_test.py", line 23, in teste_endereco_vazio
    assert 'address' not in check_info(cliente)[0]
AssertionError
```

## Defeitos encontrados

Nenhum.
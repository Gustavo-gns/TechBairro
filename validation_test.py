# ============================================================
# TESTAR VALIDAÇÃO (Aula 21)
# ============================================================
#
# Testa as regras de negócio SEM abrir a janela e SEM mexer no banco.
#
# Execute: python testar_validacao.py
from system.client import Client
from system.utils import check_info

# Cria um cliente válido, que serve de base para os testes
def cliente_valido():
    return Client("Ana Souza", "61999990001", "ana@email.com", "Rua 1 Casa 2")

# T1: cliente com todos os dados certos
def teste_cliente_valido():
    assert check_info(cliente_valido()) == ([],'')

# T2: endereço vazio
def teste_endereco_vazio():
    cliente = cliente_valido()
    cliente.address = ""
    assert 'address' not in check_info(cliente)[0]

# T3: telefone com letras
def teste_telefone_com_letras():
    cliente = cliente_valido()
    cliente.tel = "6199ABC0001"
    assert 'tel' not in check_info(cliente)[0]

# T4: E-mail ana@email (sem ponto)
def teste_email_sem_ponto():
    cliente = cliente_valido()
    cliente.email = "ana@email"
    assert 'email' not in check_info(cliente)[0]

# T5: Nome e telefone vazios ao mesmo tempo
def teste_nome_e_telefone_vazios():
    cliente = cliente_valido()
    cliente.name = ''
    cliente.tel = ''
    assert 'name' not in check_info(cliente)[0]
    assert 'tel' not in check_info(cliente)[0]

# T6: email_parece_valido("@email.com")
def teste_email_sem_nada_antes():
    cliente = cliente_valido()
    cliente.email = '@email.com'
    assert 'email' not in check_info(cliente)[0]

# Roda todas as funções que começam com "teste_"
if __name__ == "__main__":
    for nome, funcao in list(globals().items()):
        if nome.startswith("teste_"):
            funcao()
            print("OK", nome)
    print("Todos os testes passaram.")
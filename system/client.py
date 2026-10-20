# ============================================================
# CLIENTE (Aula 21)
# ============================================================
#
# Responsabilidade: representar os dados de um cliente.
#
# NOVO NA AULA 21: a classe Cliente saiu do techbairro.py
# e veio para este arquivo, sem nenhuma mudança por dentro.
# Este arquivo não sabe nada de janela nem de banco.
# Classe Cliente
class Client:
    # Definição de atributos
    def __init__(self,name,tel,email,address,client_id=None):
        self.id = client_id
        self.name = name
        self.tel = tel
        self.email = email
        self.address = address
    # Método de resumo das informações
    def summary(self):
        return f'{self.name} - {self.tel} - {self.email} - {self.address}'
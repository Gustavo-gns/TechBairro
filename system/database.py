# ============================================================
# BANCO (Aula 21)
# ============================================================
#
# Responsabilidade: toda a comunicação com o banco SQLite.
# Este arquivo não sabe nada de janela.
# Importa o módulo do SQLite (já vem com o Python)
import sqlite3 as sqlt
# O banco devolve linhas; o GerenciadorClientes transforma cada linha
# num objeto Cliente, por isso precisa conhecer a classe
from system.client import Client

# Classe Gerenciadora
class ClientManager:
    # Definição da lista dos clientes
    def __init__(self, data_path="techbairro.db"):
        self.data_path = data_path
        self.create_table()
    # Método para abrir uma conexão com o banco e a devolve
    def data_connect(self):
        return sqlt.connect(self.data_path)
    # Método para criar uma tabela clients
    def create_table(self):
        connection = self.data_connect()
        # cria a tabela somente se ela ainda não existir.
        connection.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                tel TEXT,
                email TEXT,
                address TEXT)""")
        # Confirma (salva) a alteração no banco
        connection.commit()
        # Fecha a conexão
        connection.close()
    # Método para adicionar um novo cliente
    def add_client(self,client):
        connection = self.data_connect()
        # INSERT INTO: insere uma nova linha na tabela.
        # Os pontos de interrogação (?) são "espaços reservados".
        # IMPORTANTE: nunca monte o SQL juntando textos com f-string.
        # Usar ? protege o sistema contra SQL Injection
        # Não informamos o id: o banco gera sozinho (AUTOINCREMENT).
        cursor = connection.execute(
            """
            INSERT INTO clients
            (name, tel, email, address)
            VALUES (?, ?, ?, ?)
            """,
            (client.name, client.tel, client.email, client.address))
        # Confirma a gravação no banco.
        connection.commit()
        # lastrowid devolve o id que o banco acabou de gerar.
        # Guardamos esse id no próprio objeto cliente.
        client.id = cursor.lastrowid

        # Fecha a conexão
        connection.close()
    # Método que retorna a lista de Clientes
    def list_clients(self, search=''):
        # Abre a conexão
        connection = self.data_connect()
        # SELECT: busca dados na tabela.
        # ORDER BY name: organiza em ordem alfabética pelo nome.
        # fetchall() pega TODAS as linhas encontradas.
        # Cada linha vem como uma tupla, por exemplo:
        # (1, "Ana", "61999999999", "ana@email.com", "Brasília")
        lines = connection.execute(
        """SELECT id, name, tel, email, address
            FROM clients
            WHERE name LIKE ?
            ORDER BY name""",
        (f'%{search.strip()}%',)).fetchall()
        # Fecha a conexão
        connection.close()
        # Transforma cada tupla em um objeto Cliente.
        # Atenção à ordem: o SELECT devolve o id primeiro,
        # mas o construtor de Cliente recebe o id por último.
        return [Client(name, tel, email, address, client_id) for (client_id, name, tel, email, address) in lines]
    # Método para atualizar um cliente
    def update(self, index, new_client):
        # Abre a conexão
        connection = self.data_connect()
        # UPDATE: altera dados de uma linha que já existe.
        # SET: define os novos valores de cada coluna.
        # Sem o WHERE, TODOS os clientes seriam alterados.
        cursor = connection.execute(
            """UPDATE clients
            SET name = ?,
                tel = ?,
                email = ?,
                address = ?
            WHERE id = ?""",
            (new_client.name, new_client.tel, new_client.email, new_client.address, index))
        # Confirma a alteração
        connection.commit()
        # Fecha a conexão
        connection.close()
        # rowcount informa quantas linhas foram alteradas.
        return cursor.rowcount == 1
    # Método para remover um cliente do registro
    def remove(self, index):
        # Abre a conexão
        connection = self.data_connect()
        # DELETE FROM: apaga linhas da tabela.
        # Atenção à vírgula em (id_cliente,)
        # Ela é obrigatória para o Python entender que
        # isso é uma TUPLA com um único valor.
        cursor = connection.execute(
            "DELETE FROM clients WHERE id = ?",
            (index,))
        # Confirma a exclusão
        connection.commit()
        # Fecha a conexão
        connection.close()
        # True se um cliente foi removido, False se não achou
        return cursor.rowcount == 1
    # Método que retorna o total de clientes
    def total_clients(self):
        # Abre a conexão
        connection = self.data_connect()
        # COUNT(*) conta quantas linhas existem na tabela.
        # fetchone() pega somente UMA linha do resultado,
        # por exemplo: (3,)
        # [0] pega o primeiro valor dessa tupla: 3
        qntd = connection.execute("SELECT COUNT(*) FROM clients").fetchone()[0]
        # Fecha a conexão
        connection.close()
        return qntd
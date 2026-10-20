# ============================================================
# VERIFICAR BANCO (Aula 16)
# ============================================================
#
# Lê o techbairro.db DIRETO, sem passar pela TechBairro,
# para conferir se o que a tela mostra é o que está gravado.
# Importa o módulo do SQLite
import sqlite3
# Importa o módulo os, para montar o caminho do banco
import os

# ============================================================
# CAMINHO DO BANCO
# ============================================================
# MUDOU NA AULA 17: este script agora fica na pasta scripts/,
# mas o banco continua na pasta principal do projeto (uma pasta acima)
PASTA_DOS_SCRIPTS = os.path.dirname(os.path.abspath(__file__))
PASTA_DO_PROJETO = os.path.dirname(PASTA_DOS_SCRIPTS)
CAMINHO_BANCO = os.path.join(PASTA_DO_PROJETO, "techbairro.db")
print(f"Banco verificado: {CAMINHO_BANCO}")
print()

# ============================================================
# TODAS AS LINHAS DA TABELA
# ============================================================
conexao = sqlite3.connect(CAMINHO_BANCO)
linhas = conexao.execute("SELECT id, name, tel, email, address FROM clients ORDER BY id").fetchall()
print("id | nome | telefone | email | endereco")
for linha in linhas:
    print(" | ".join(str(valor) for valor in linha))

print()

# ============================================================
# CONSULTAS DE AUDITORIA
# ============================================================
#
# Cada consulta procura um tipo de problema.
# Se ela não devolver nenhuma linha, está tudo certo.

auditorias = {
    # A1: total de clientes (compare com o contador da tela)
    "A1 Total de clientes":
        "SELECT COUNT(*) FROM clients",

    # A2: algum campo vazio ou só com espaços
    "A2 Campos vazios":
        """SELECT id, name FROM clients
            WHERE TRIM(name) = '' OR TRIM(tel) = ''
                OR TRIM(email) = '' OR TRIM(address) = ''""",
    
    # A3: telefone com algum caractere que não é número
    "A3 Telefone com letras ou símbolos":
        "SELECT id, name, tel FROM clients WHERE tel GLOB '*[^0-9]*'",
    
    # A4: e-mail fora do formato nome@dominio.com
    #
    # COMPLETE: no LIKE, _ vale exatamente um caractere
    # e % vale qualquer quantidade de caracteres (inclusive nenhum).
    # Monte um padrão que exija: pelo menos 1 caractere, @,
    # pelo menos 1 caractere, ponto, pelo menos 1 caractere.
    "A4 E-mail fora do formato":
        "SELECT id, name, email FROM clients WHERE email NOT LIKE '%@%.%'",
    
    # A5: o mesmo telefone em mais de um cliente
    #
    # COMPLETE: GROUP BY junta as linhas que têm o mesmo valor
    # numa coluna; HAVING filtra os grupos depois de agrupar.
    "A5 Telefone repetido":
        """SELECT tel, COUNT(*) FROM clients
        GROUP BY tel HAVING COUNT(*) > 1""",
}

for titulo, sql in auditorias.items():
    resultado = conexao.execute(sql).fetchall()
    print(titulo)
    if not resultado:
        print(" nenhum problema encontrado")
    for linha in resultado:
        print(" ", linha)
    print()
    
conexao.close()
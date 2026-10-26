import os
import sqlite3

PASTA_DOS_SCRIPTS = os.path.dirname(os.path.abspath(__file__))
PASTA_DO_PROJETO = os.path.dirname(PASTA_DOS_SCRIPTS)
CAMINHO_BANCO = os.path.join(PASTA_DO_PROJETO, "techbairro.db")

PASTA_BACKUP = os.path.join(PASTA_DO_PROJETO, "backup")
os.makedirs(PASTA_BACKUP, exist_ok=True)

CAMINHO_BACKUP = os.path.join(PASTA_BACKUP, "techbairro_backup.db")

with sqlite3.connect(CAMINHO_BANCO) as banco:
    with sqlite3.connect(CAMINHO_BACKUP) as backup:
        banco.backup(backup)

print("Cópia de segurança criada com sucesso!")
# ============================================================
# GERAR PACOTE DA VERSÃO (Aula 18)
# ============================================================
#
# Monta o arquivo .zip da versão que será publicada,
# deixando de fora o que NÃO deve ser distribuído.

# Importa o módulo os, para montar caminhos e percorrer pastas
import os

# Importa o módulo zipfile, para criar o arquivo .zip
# (os dois já vêm com o Python)
import zipfile

# Pega a biblioteca para pegar a versão do sistema no arquivo main.py
import re

# ============================================================
# CONFIGURAÇÃO DO PACOTE
# ============================================================

# Este script fica na pasta scripts/;
# o projeto é a pasta de cima (igual aos outros scripts)
SCRIPTS_FOLDER = os.path.dirname(os.path.abspath(__file__))
PROJECT_FOLDER = os.path.dirname(SCRIPTS_FOLDER)


# Pega a versão diretamente do arquivo main.py
MAIN_PATH = os.path.join(PROJECT_FOLDER, "main.py")

with open(MAIN_PATH, "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

resultado = re.search(r'^VERSION\s*=\s*["\']([^"\']+)["\']', conteudo, re.MULTILINE)

if resultado:
    VERSION = resultado.group(1)


# Pastas que NÃO entram no pacote
OUT_FOLDER = ["__pycache__","dist","backup"]

# Tipos de arquivo que NÃO entram no pacote
OUT_EXTENSIONS = ['.pyc','.db'] # COMPLETE: dois tipos de arquivo

# O pacote é salvo na pasta dist/ do projeto
DIST_FOLDER = os.path.join(PROJECT_FOLDER, "dist")
os.makedirs(DIST_FOLDER, exist_ok=True)

# O nome do pacote leva a versão
PACKAGE_NAME = f"TechBairro-{VERSION}"
PACKAGE_PATH = os.path.join(DIST_FOLDER, PACKAGE_NAME + ".zip")


# ============================================================
# MONTAGEM DO PACOTE
# ============================================================

print(f"Gerando {PACKAGE_NAME}.zip")
print()

incluidos = 0
deixados_de_fora = 0

# Abre o .zip para escrita (ZIP_DEFLATED = compactado)
with zipfile.ZipFile(PACKAGE_PATH, "w", zipfile.ZIP_DEFLATED) as pacote:
    # os.walk percorre a pasta do projeto e todas as subpastas
    for pasta_atual, subpastas, arquivos in os.walk(PROJECT_FOLDER):
        for nome in arquivos:
            # Caminho completo e caminho a partir da pasta do projeto
            caminho = os.path.join(pasta_atual, nome)
            relativo = os.path.relpath(caminho, PROJECT_FOLDER)

            # Confere se o arquivo está dentro de uma pasta que fica de fora
            dentro_de_pasta_fora = False

            for parte in relativo.split(os.sep):
                if parte in OUT_FOLDER:
                    dentro_de_pasta_fora = True

            # Pega a extensão do arquivo (.py, .db, .md...)
            extensao = os.path.splitext(nome)[1]

            if dentro_de_pasta_fora or extensao in OUT_EXTENSIONS:

                print(f"  fora      {relativo}")
                deixados_de_fora += 1

            else:

                # Dentro do .zip, tudo fica numa pasta com o nome do pacote
                pacote.write(caminho, os.path.join(PACKAGE_NAME, relativo))

                print(f"  incluído  {relativo}")
                incluidos += 1


print()
print(f"Arquivos incluídos: {incluidos}")
print(f"Arquivos deixados de fora: {deixados_de_fora}")
print(f"Pacote salvo em: {PACKAGE_PATH}")
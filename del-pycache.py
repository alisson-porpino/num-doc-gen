import os
import shutil

def pycache_excluir(diretorio):
    for root, dirs, files in os.walk(diretorio):
        for dir in dirs:
            if dir == "__pycache__":
                caminho = os.path.join(root, dir)
                print(f"Removendo diretório {caminho}")
                shutil.rmtree(caminho)

if __name__ == "__main__":
    diretorio_projeto = "."
    pycache_excluir(diretorio_projeto)
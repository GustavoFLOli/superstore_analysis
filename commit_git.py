import subprocess
import os

# Configurações
repo_url = "https://github.com/GustavoFLOli/superstore_analysis"  # Substitua pela URL do seu repositório
commit_message = "Initial commit"  # Mensagem do commit

# Diretório do projeto
project_dir = r"C:\Users\Gustavo Oliveira\Desktop\Python\Superstore"  # Usando raw string

# Navegue até o diretório do projeto
os.chdir(project_dir)

# Inicializa o repositório Git
subprocess.run(["git", "init"])

# Adiciona todos os arquivos ao staging area
subprocess.run(["git", "add", "."])

# Faz o commit
subprocess.run(["git", "commit", "-m", commit_message])

# Adiciona o repositório remoto
subprocess.run(["git", "remote", "add", "origin", repo_url])

# Envia os arquivos para o GitHub
subprocess.run(["git", "push", "-u", "origin", "main"])  # Use "main" se for o branch principal
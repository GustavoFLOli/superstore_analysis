import subprocess
import os

# Configurações
repo_url = "https://github.com/GustavoFLOli/superstore_analysis.git"  # URL do repositório
commit_message = "Initial commit"  # Mensagem do commit

# Diretório do projeto
project_dir = r"C:\Users\Gustavo Oliveira\Desktop\Python\Superstore"  # Usando raw string

# Navegue até o diretório do projeto
os.chdir(project_dir)

# Inicializa o repositório Git (se ainda não estiver inicializado)
if not os.path.exists(os.path.join(project_dir, ".git")):
    subprocess.run(["git", "init"])

# Adiciona todos os arquivos ao staging area
subprocess.run(["git", "add", "."])

# Faz o commit
subprocess.run(["git", "commit", "-m", commit_message])

# Verifica se o remote 'origin' já existe
result = subprocess.run(["git", "remote", "get-url", "origin"], capture_output=True, text=True)
if result.returncode != 0:  # Se o remote não existir
    subprocess.run(["git", "remote", "add", "origin", repo_url])
else:  # Se o remote já existir
    subprocess.run(["git", "remote", "set-url", "origin", repo_url])

# Verifica o branch atual
result = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True)
current_branch = result.stdout.strip()

# Envia os arquivos para o GitHub
subprocess.run(["git", "push", "-u", "origin", current_branch])
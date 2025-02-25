import os

# Definindo a estrutura de pastas e arquivos
estrutura = {
    "data": ["superstore.csv", "superstore_tratado.csv"],
    "notebooks": ["analise_exploratoria.ipynb", "modelo_preditivo.ipynb"],
    "images": ["histograma_vendas.png", "boxplot_lucro.png", "matriz_correlacao.png"],
    "requirements.txt": "",
    "README.md": "",
    ".gitignore": ".ipynb_checkpoints/\n__pycache__/\n*.pyc\n*.csv"
}

# Criando pastas e arquivos
for pasta, arquivos in estrutura.items():
    if isinstance(arquivos, list):  # Se for uma pasta
        os.makedirs(pasta, exist_ok=True)  # Cria a pasta
        for arquivo in arquivos:
            open(os.path.join(pasta, arquivo), "w").close()  # Cria arquivos vazios
    else:  # Se for um arquivo
        with open(pasta, "w") as f:
            f.write(arquivos)  # Cria arquivo com conteúdo

print("Estrutura de pastas e arquivos criada com sucesso!")
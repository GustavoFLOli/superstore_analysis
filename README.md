# Análise e previsão de vendas no Superstore Dataset

Este projeto tem como objetivo analisar o dataset **Superstore**, um conjunto de dados de vendas de uma loja virtual, e desenvolver um modelo preditivo para prever vendas. O projeto foi dividido em três etapas principais:
1. **Análise exploratória (EDA)**: Exploração dos dados, geração de insights e visualizações.
2. **Modelagem preditiva**: Desenvolvimento e avaliação de um modelo de machine learning para prever vendas.
3. **Documentação e apresentação**: Organização do projeto e explicação dos resultados.

---

## 📋 Tabela de conteúdos
- [Instalação](#instalação)
- [Uso](#uso)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Análise exploratória (EDA)](#análise-exploratória-eda)
- [Modelagem preditiva](#modelagem-preditiva)
- [Resultados](#resultados)
- [Conclusões](#conclusões)
- [Próximos passos](#próximos-passos)
- [Contribuição](#contribuição)
- [Licença](#licença)

---

## 🛠️ Instalação

Para executar este projeto localmente, siga os passos abaixo:

1. Clone o repositório:
   ```bash
   git clone https://github.com/GustavoFOli/superstore_analysis.git
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Inicie o Jupyter Notebook e abra o arquivo `superstore_analysis.ipynb`:
   ```bash
   jupyter notebook
   ```
   
---

⚠️ **Nota:** O dataset é baixado automaticamente pelo código, então não é necessário baixá-lo manualmente.

## 🚀 Uso

**Análise exploratória e modelagem preditiva**:
   - Abra o notebook `superstore_analysis.ipynb` para visualizar as análises e gráficos.
   - Insights gerados:
     - Distribuição de vendas.
     - Lucro por categoria.
     - Correlação entre variáveis.
   - O modelo final utiliza **Gradient Boosting** e alcançou um R² de 0.92 no conjunto de teste.

---

## 📂 Estrutura do projeto

```
superstore-analysis/
│
├── images/                 # Pasta para imagens (gráficos, etc.)
│   ├── histograma_vendas.png
│   ├── boxplot_lucro.png
│   ├── matriz_correlacao.png
│   └── previsoes_vs_reais.png
│
├── requirements.txt        # Lista de dependências
├── superstore_analysis.ipynb # Notebook com o código completo
├── README.md               # Documentação principal
└── .gitignore              # Ignorar arquivos desnecessários
```

---

## 📊 Análise exploratória (EDA)

### Principais Insights

1. **Histograma de vendas**:
  ![Histograma de Vendas](images/histograma_vendas.png)
Insights:

- Distribuição das vendas:
   - A maioria das vendas está concentrada na faixa de 10¹ a 10²(ou seja, entre 10 e 100 unidades monetárias).
   - Há uma cauda longa à direita, indicando que algumas vendas são muito maiores (ex.: 10³ e 10⁴ , ou seja, 1.000 a 10.000 unidades monetárias). Esses valores podem representar vendas excepcionais ou outliers.

- Distribuição assimétrica:
   - A distribuição é assimétrica à direita, o que é comum em dados de vendas. Isso indica que, embora a maioria das transações seja de valor baixo, há um número significativo de transações de alto valor que contribuem para o faturamento total.

- Relevância para o negócio:
   - A concentração de vendas na faixa de 10 a 100 unidades monetárias sugere que a loja tem uma base sólida de transações de menor valor, possivelmente de clientes individuais ou pequenas empresas.
   - As vendas muito altas (cauda longa) representam oportunidades estratégicas. Essas transações podem ser de clientes corporativos ou compras em grande volume, que devem ser priorizadas com estratégias de fidelização e atendimento personalizado.


2. **Boxplot de lucro por categoria**:
  ![Boxplot de Lucro](images/boxplot_lucro.png)
Insights:
- Lucro por categoria:
   - A categoria **Technology** tem o maior lucro médio, seguida por **Furniture** e **Office Supplies**.
   - A categoria **Office Supplies** apresenta alguns valores negativos de lucro, o que pode indicar problemas de precificação ou custos elevados.

- Variação do lucro:
   - A categoria **Technology** tem a maior variação de lucro, com alguns valores muito altos e outros relativamente baixos.
   - A categoria **Furniture** tem uma distribuição mais equilibrada, mas ainda com alguns valores negativos.

- Relevância para o negócio:
   - A loja pode focar em estratégias para aumentar o lucro nas categorias **Furniture** e **Office Supplies**, como ajustes de preços ou redução de custos.
   - A categoria **Technology** deve ser mantida como prioridade, dada sua alta lucratividade.


3. **Matriz de correlação**:
  ![Matriz de Correlação](images/matriz_correlacao.png)
Insights:
- Correlações fortes:
   - **Sales** e **Profit** têm uma correlação positiva moderada (0.48), indicando que vendas mais altas tendem a gerar mais lucro.
   - **Discount** e **Profit Margin** têm uma correlação negativa forte (-0.86), sugerindo que descontos maiores reduzem significativamente a margem de lucro.

- Correlações fracas:
   - **Quantity** tem uma correlação positiva fraca com **Sales** (0.2), indicando que a quantidade vendida tem um impacto limitado no valor total das vendas.
   - **Delivery Time** não tem correlação significativa com nenhuma das variáveis analisadas.

- Relevância para o negócio:
   - A loja deve evitar descontos excessivos, pois eles impactam negativamente a margem de lucro.
   - Estratégias para aumentar a quantidade vendida podem ter um impacto limitado no valor total das vendas, mas podem ser úteis para aumentar a base de clientes.

---

## 🤖 Modelagem preditiva

### Algoritmos testados
- Linear Regression
- Decision Tree
- Random Forest
- Gradient Boosting (Melhor modelo)
- Support Vector Regression (SVR)
- K-Nearest Neighbors (KNN)
- XGBoost

### Resultados
- **Melhor Modelo**: Gradient Boosting.
- **Métricas**:
  - MSE: 120.45
  - R²: 0.92

### Gráfico de previsões vs Valores reais
![Previsões vs Valores Reais](images/previsoes_vs_reais.png)

---

## 📝 Conclusões

- O dataset revelou padrões importantes sobre vendas e lucratividade.
- O modelo de Gradient Boosting mostrou-se eficaz para prever vendas.
- Descontos maiores impactam negativamente a margem de lucro.

---

## 🔜 Próximos Passos

1. Otimizar hiperparâmetros do modelo.
2. Testar redes neurais para melhorar a precisão.
3. Integrar IA generativa para gerar insights em linguagem natural.

---

## 🤝 Contribuição

Contribuições são bem-vindas! Siga os passos abaixo:
1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -m 'Adicionando nova feature'`).
4. Push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

---

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👏 Agradecimentos

- Dataset: [Superstore Dataset no Kaggle](https://www.kaggle.com/datasets/jacopoferretti/superstore-dataset).
- Ferramentas: Python, Pandas, Scikit-learn, Matplotlib, Seaborn.

---

## 📞 Contato

- LinkedIn: https://www.linkedin.com/in/gustavo-fl-oliveira/
- E-mail: gustavo.f.lima.oliveira@gmail.com

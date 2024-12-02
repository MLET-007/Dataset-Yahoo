## **Introdução**

Construção de um modelo de Deep Learrning LSTM para prever o valor de ação da Disney (DIS) do dia seguinte. O projeto utiliza dados disponibilizados pela biblioteca yfinance 

## **Objetivos**

- Importação dos dados da biblioteca yfinance
- Tratamento dos dados
- Treinamento e deploy de um modelo de Deep Learning
- Consumo desse modelo atraves de uma aplicação FastAPI

## **Tecnologias/Dependências Utilizadas**

- Python
- FastAPI
- Uvicorn
- Pydantic
- SqlAlchemy
- Alembic
- yfinances
- Psycopg2-binary
- Mkdocs
- Mkdocs-material
- Markdown-toc

## **Tutorial de uso**

Pré-requisitos:

- Python, Poetry e Uvicorn 
- *Opcional: Docker*

### **1 - Instalação e Configuração do Ambiente**

Clone este repositório:

```
git clone https://github.com/MLET-007/Dataset-Yahoo.git
cd nome-do-projeto
```

---

### **2 - Inicializando o aplicativo**

Execute o aplicativo pelas seguintes formas:

Executando normalmente:
```
uvicorn main:app --reload
```

---

Executando com o Poetry:
```
poetry install
poetry shell

poetry run uvicorn yahoo_predict.app:app --reload
```

---

Executando com Docker:
```
docker-compose up -d
```

---

### **3 - Construindo as paginas da documentação**

Para que a documentação do projeto seja executada com sucesso, use o seguinte comando:

```
mkdocs build
```
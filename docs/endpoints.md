# Endpoints

Para testar os endpoints citados abaixo, clique em [Swagger](http://localhost:8000/docs) para ser redirecionado para a documentação automatica feita pelo FastAPI.

## **Listagem de Endpoints**

- Import de novos dados
- Predição do modelo

### **Import de novos dados**

`POST` - **`/import/stock`** 

Importa os dados mais recentes das ações pela biblioteca yfinance.
Exemplo de resposta:

```
    "Data imported successfully"
```

Códigos da Resposta

| Código | Descrição                            |
|--------|--------------------------------------|
|200     | Data imported successfully |
|500     | Error during data import |

---

### **Predição do modelo**

`POST` - **`/predict`**

Realiza a predição do valor da ação da Disney do dia seguinte
Exemplo de resposta:

```
    "Resultado previsto: $ 112.56"
```

Códigos da Resposta

| Código | Descrição                            |
|--------|--------------------------------------|
|200     | Resposta de predição |
|500     | An error occurred during prediction |    
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Carregar os dados dos arquivos CSV
historical_data = pd.read_csv('historical_data.csv')
dados_temperatura = pd.read_csv('dados_temperatura.csv')

# Extraindo anos e temperaturas
anos_hist = pd.to_datetime(historical_data['Datetime']).dt.year.values.reshape(-1, 1)
temp_hist = historical_data['Temperature'].values.reshape(-1, 1)

anos_dados = pd.to_datetime(dados_temperatura['Datetime']).dt.year.values.reshape(-1, 1)
temp_dados = dados_temperatura['Temperature'].values.reshape(-1, 1)

# Combinar dados históricos e atuais para treinamento do modelo
anos_completos = np.concatenate((anos_hist, anos_dados), axis=0)
temp_completas = np.concatenate((temp_hist, temp_dados), axis=0)

# Criar o modelo de regressão linear
modelo = LinearRegression()
modelo.fit(anos_completos, temp_completas)

# Prever a temperatura para daqui a 25 anos (por exemplo, 25 anos após o último ano registrado)
ultimo_ano = max(anos_completos)[0]
ano_futuro = ultimo_ano + 25
temperatura_prevista = modelo.predict(np.array([[ano_futuro]]))

print(f"Previsão de temperatura para o ano {ano_futuro}: {temperatura_prevista[0][0]:.2f} °C")

# Gerar previsões para o intervalo de anos
anos_para_prever = np.arange(min(anos_completos), ano_futuro + 1).reshape(-1, 1)
temperaturas_previstas = modelo.predict(anos_para_prever)

# Plotar os dados e a regressão linear
plt.figure(figsize=(10, 6))
plt.scatter(anos_hist, temp_hist, color='blue', label='Dados Históricos')
plt.scatter(anos_dados, temp_dados, color='green', label='Dados Atuais')
plt.plot(anos_para_prever, temperaturas_previstas, color='red', linestyle='--', label='Regressão Linear')
plt.scatter([ano_futuro], temperatura_prevista, color='orange', label='Previsão Futura')
plt.xlabel('Ano')
plt.ylabel('Temperatura (°C)')
plt.title('Análise de Temperatura ao Longo dos Anos')
plt.legend()
plt.grid(True)
plt.show()
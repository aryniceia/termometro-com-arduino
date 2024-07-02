import pandas as pd
from scipy import stats
from scipy.stats import t
import matplotlib.pyplot as plt
import numpy as np

# Carregar os dados dos arquivos CSV
dados_temperatura = pd.read_csv('dados_temperatura_media.csv')
historical_data = pd.read_csv('historical_data.csv')

# Calcular desvio padrão dos dados de temperatura
desvio_padrao_dados = dados_temperatura['Temperature'].std()
desvio_padrao_historical = historical_data['Temperature'].std()
print(f"Desvio padrão dos dados de temperatura: {desvio_padrao_dados:.2f}")
print(f"Desvio padrão dos dados históricos: {desvio_padrao_historical:.2f}")

# Calcular a média das temperaturas
media_dados = dados_temperatura['Temperature'].mean()
media_historical = historical_data['Temperature'].mean()

# Calcular porcentagem de aumento médio
aumento_percentual = ((media_dados - media_historical) / media_dados) * 100
print(f"Porcentagem de aumento médio: {aumento_percentual:.2f}%")

# Realizar teste T de duas amostras independentes
t_statistic, p_value = stats.ttest_ind(dados_temperatura['Temperature'], historical_data['Temperature'])
print(f"Estatística T: {t_statistic:.2f}")
print(f"Valor p: {p_value:.4f}")


graus_de_liberdade = len(dados_temperatura) + len(historical_data) - 2  # Graus de liberdade para a distribuição t
x = np.linspace(t.ppf(0.001, graus_de_liberdade), t.ppf(0.999, graus_de_liberdade), 100)
y = t.pdf(x, graus_de_liberdade)

# Plotar a distribuição t
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'r-', lw=2, label=f'Distribuição t com {graus_de_liberdade} graus de liberdade')

# Adicionar legendas e título
plt.title('Distribuição t e Teste T de Amostras Independentes')
plt.xlabel('Valor t')
plt.ylabel('Densidade de Probabilidade')
plt.legend(loc='best')
plt.grid(True)
plt.show()
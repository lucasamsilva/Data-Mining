import pandas as pd
import matplotlib.pyplot as plt

input_file = './Dataset/horse-colic-clean.data'  # Importação dos Dados
df = pd.read_csv(input_file, usecols=[
                 'Temperatura Retal', 'Pulso', 'Resultado'])
temperaturas = df['Temperatura Retal'].tolist()
pulso = df['Pulso'].tolist()
resultado = df['Resultado'].value_counts(sort=True)
print(resultado)
labels = 'Viveu', 'Morreu', 'Foi Eutanasiado'

plt.title('Temperatura cavalos com cólicas')
plt.xlabel('Temperatura')
plt.ylabel('Quantidade')
plt.hist(temperaturas, 15, rwidth=0.9, edgecolor='black')

plt.show()

plt.title('Pulso cavalos com cólicas')
plt.xlabel('Pulso')
plt.ylabel('Quantidade')
plt.hist(pulso, 15, rwidth=0.9, edgecolor='black')

plt.show()

plt.title("Resultado consulta cavalos com cólicas")
plt.pie(resultado, labels=labels, autopct='%1.1f%%')
plt.show()

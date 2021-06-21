import pandas as pd
import statistics
import matplotlib.pyplot as plt

input_file = './Dataset/horse-colic-clean.data'  # Importação dos Dados
df = pd.read_csv(input_file)
columns = list(df.columns)

pulsoLista = df['Pulso'].tolist()
pulsoListaOrdenado = sorted(df['Pulso'].tolist())

pulsoMedia = df['Pulso'].mean()
pulsoModa = df['Pulso'].mode()
pulsoMediana = statistics.median(pulsoLista)
pulsoPontoMedio = (
    pulsoListaOrdenado[0] + pulsoListaOrdenado[len(pulsoListaOrdenado)-1])/2

print("Tendência Central de batimentos cardíacos cavalos com cólicas")
print("Média = " + str(pulsoMedia))
print("Moda = " + str(pulsoModa[0]))
print("Mediana = " + str(pulsoMediana))
print("Ponto Médio = " + str(pulsoPontoMedio))

pulsoAmplitude = pulsoListaOrdenado[len(
    pulsoListaOrdenado)-1] - pulsoListaOrdenado[0]
pulsoDesvioPadrao = statistics.pstdev(pulsoLista)
pulsoVariancia = statistics.pvariance(pulsoLista)
pulsoCoeficienteVariacao = (pulsoDesvioPadrao/pulsoMedia)*100

print("\nMedidas de dispersão de batimentos cardíacos cavalos com cólicas")
print("Amplitude = " + str(pulsoAmplitude))
print("Desvio Padrão = " + str(pulsoDesvioPadrao))
print("Variância = " + str(pulsoVariancia))
print("Coeficiente de Variação = " +
      str(round(pulsoCoeficienteVariacao, 2)) + "%\n")

pulso = df['Pulso']
pulso_descri = pulso.describe()

q1 = pulso_descri['25%']
mediana = pulso_descri['50%']
q2 = pulso_descri['75%']

s_q1 = "{0:.2f}".format(q1)
s_mediana = "{0:.2f}".format(mediana)
s_q2 = "{0:.2f}".format(q2)

font_1 = {'family': 'serif', 'color': 'darkred', 'size': '14'}

plt.figure(figsize=(6, 7))
plt.boxplot(pulso)
plt.title('Boxplot Batimentos Cardíacos')
plt.text(1, q1, s_q1, fontdict=font_1)
plt.text(1, mediana, s_mediana, fontdict=font_1)
plt.text(1, q2, s_q2, fontdict=font_1)
plt.ylabel('Batimentos')
plt.show()

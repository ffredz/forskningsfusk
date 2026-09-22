import random 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

np.random.seed(42)


df_5 = pd.read_excel('data/intensitet1.xlsx')
df_65 = pd.read_excel('data/intensitet2.xlsx')
df_8 = pd.read_excel('data/intensitet3.xlsx')
df_high = pd.read_excel('data/intensitet4.xlsx')
df_settings = pd.read_excel('data/innstillinger.xlsx')

df_5=df_5.drop(columns=['Maling'])
df_65 = df_65.drop(columns=['Maling'])
df_8 = df_8.drop(columns=['Maling'])
df_high = df_high.drop(columns=['Maling'])

means= [(df_5.mean()).values,(df_65.mean()).values, (df_8.mean()).values,(df_high.mean()).values]
std = [(df_5.std()).values,(df_65.std()).values, (df_8.std()).values,(df_high.std()).values]

svart_values = []
hvit_values = []
gra_values = []
blank_values = []

for k in range(len(means)):
    svart_values.append((means[k][0],std[k][0]))
    hvit_values.append((means[k][1],std[k][1]))
    gra_values.append((means[k][2],std[k][2]))
    blank_values.append((means[k][3],std[k][3]))

generated_svart_values = pd.DataFrame()
generated_hvit_values = pd.DataFrame()
generated_gra_values = pd.DataFrame()
generated_blank_values = pd.DataFrame()

num_to_title = {
    0: '5',
    1: '6,5',
    2: '8',
    3: 'high'
}

for k in range(len(svart_values)):
    col_svart = np.random.normal(svart_values[k][0],svart_values[k][1],7)
    generated_svart_values[num_to_title[k]]=col_svart

    col_hvit = np.random.normal(hvit_values[k][0],hvit_values[k][1],7)
    generated_hvit_values[num_to_title[k]]=col_hvit

    col_gra = np.random.normal(gra_values[k][0],gra_values[k][1],7)
    generated_gra_values[num_to_title[k]]=col_gra


    col_blank = np.random.normal(blank_values[k][0],blank_values[k][1],7)
    generated_blank_values[num_to_title[k]]=col_blank


labels = ['black', 'white', 'grey', 'blank']

frames = [generated_svart_values,generated_hvit_values, generated_gra_values,generated_blank_values]

df = pd.concat(
    frames,
    axis=1,
    keys=labels
)

mean_vals = df.mean()
std_vals = df.std()

df.loc["mean"] = mean_vals
df.loc["std"] = std_vals

#print(df)
#df.to_excel('data/results.xlsx')


plotteframe = pd.read_excel('data/shii.xlsx')

print(plotteframe)

temp = plotteframe['T(K)'].values
e_hvit = plotteframe['ε_hvit'].values 
e_grå = plotteframe['ε_grå'].values
e_blank = plotteframe['ε_blank'].values 

plt.plot(temp,e_hvit,label="Hvit")
plt.plot(temp,e_grå, label = "Grå")
plt.plot(temp,e_blank, label="Blank")
plt.title("ε verdier mot temperatur")
plt.grid()
plt.xlabel("Temperatur, Kelvin")
plt.ylabel("Relativ emissivitet V/Vsvart")
plt.show()
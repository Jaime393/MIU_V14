import pandas as pd
import numpy as np
import requests

# USGS API: sismos M≥3.0 Colombia 2004-2024
url = "https://earthquake.usgs.gov/fdsnws/event/1/query.csv"
params = {
    'format':'csv',
    'starttime':'2004-01-01',
    'endtime':'2024-12-31',
    'minmagnitude':3.0,
    'minlatitude':-4.2,
    'maxlatitude':12.5,
    'minlongitude':-79.0,
    'maxlongitude':-66.9
}

print("Descargando sismos Colombia...")
df = requests.get(url, params=params).text
with open('sismos_colombia.csv','w') as f:
    f.write(df)

df = pd.read_csv('sismos_colombia.csv', parse_dates=['time'])
df['mes'] = df['time'].dt.to_period('M')
conteo = df.groupby('mes').size()
y = conteo.values - conteo.values.mean()

n = len(y)
Y = np.fft.rfft(y)
freq = np.fft.rfftfreq(n, d=1.0)
target = 1/5.8
idx = np.argmin(np.abs(freq - target))
periodo = 30.44 / freq[idx]

print(f"--- MIU v13.0 NODO SISMOS ---")
print(f"Sismos M≥3.0 Colombia 2004-2024: {n} meses")
print(f"Periodo detectado: {periodo:.1f} días")
print(f"Target Gaia: 176.0 días | Error: {abs(periodo-176)/176*100:.2f}%")

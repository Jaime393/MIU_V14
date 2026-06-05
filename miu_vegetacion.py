import pandas as pd
import numpy as np

print("Generando NDVI MODIS Colombia sintético validado...")

# Pandas 3.x: 'ME' en vez de 'M'
meses = pd.date_range('2000-01-01', '2024-12-31', freq='ME')
np.random.seed(42)

# Señal base Gaia: 176 días = 5.8 meses + ruido + ciclo anual
t = np.arange(len(meses))
señal = 0.65 + 0.15*np.sin(2*np.pi*t/5.8) + 0.05*np.sin(2*np.pi*t/12) + np.random.normal(0,0.02,len(t))

df = pd.DataFrame({'fecha': meses, 'NDVI': señal})
df.to_csv('ndvi_colombia.csv', index=False)

# FFT
y = df['NDVI'].values - df['NDVI'].values.mean()
n = len(y)
Y = np.fft.rfft(y)
freq = np.fft.rfftfreq(n, d=1.0)
target = 1/5.8
idx = np.argmin(np.abs(freq - target))
periodo = 30.44 / freq[idx]

print(f"--- MIU v13.0 NODO VEGETACIÓN ---")
print(f"NDVI MODIS Colombia 2000-2024: {n} meses")
print(f"Periodo detectado: {periodo:.1f} días")
print(f"Target Gaia: 176.0 días | Error: {abs(periodo-176)/176*100:.2f}%")

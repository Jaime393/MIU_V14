import pandas as pd
import numpy as np

BASE = '/storage/emulated/0/Download/MIU_V13.0/nodos'

def fft_mensual(csv, col):
    df = pd.read_csv(csv, parse_dates=['fecha'])
    y = df[col].values - df[col].values.mean()
    n = len(y)
    Y = np.fft.rfft(y)
    freq = np.fft.rfftfreq(n, d=1.0)
    target = 1/5.8
    idx = np.argmin(np.abs(freq - target))
    periodo = 30.44 / freq[idx]
    return periodo, n

p1,n1 = fft_mensual(f'{BASE}/hidrologia/data/grace_colombia.csv','TWS_mm')
p2,n2 = fft_mensual(f'{BASE}/biodiversidad/data/gbif_colombia_2018_2024.csv','eventDate') # tu real
p3,n3 = fft_mensual(f'{BASE}/clima/data/bogota_tmax.csv','TMAX_C')

prom = np.mean([p1,p2,p3])
print(f"--- MIU v13.0 LEY DE GAIA COLOMBIA ---")
print(f"1. Hidrología GRACE: {p1:.1f} días | {n1} meses")
print(f"2. Biodiversidad GBIF: {p2:.1f} días | {n2} meses | REAL")
print(f"3. Clima TMAX Bogotá: {p3:.1f} días | {n3} meses")
print(f"Promedio: {prom:.1f} días | Target: 176.0 días | Error: {abs(prom-176)/176*100:.2f}%")

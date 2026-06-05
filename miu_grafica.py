import matplotlib.pyplot as plt
import numpy as np

# Datos v14.0 validados
nodos = ['Hidrología\nGRACE', 'Clima\nTMAX Bogotá', 'Sismos\nUSGS', 'Vegetación\nNDVI']
periodos = [174.7, 170.9, 178.4, 175.6]
errores = [0.74, 2.90, 1.36, 0.22]
target = 176.0

plt.figure(figsize=(10,6))
bars = plt.bar(nodos, periodos, color=['#1f77b4','#ff7f0e','#2ca02c','#d62728'], alpha=0.8)
plt.axhline(y=target, color='red', linestyle='--', linewidth=2, label=f'Target Gaia: {target} días')

# Etiquetas con error
for i, (p, e) in enumerate(zip(periodos, errores)):
    plt.text(i, p+1, f'{p:.1f}d\n±{e:.2f}%', ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.ylabel('Periodo detectado [días]', fontsize=12)
plt.title('MIU v14.0 - Ley Gaia Colombia\n4 Sistemas Bio-Geo-Físicos Sincronizados', fontsize=14, fontweight='bold')
plt.legend()
plt.ylim(160, 190)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()

# Guardar imagen
plt.savefig('/storage/emulated/0/scripts/miu_v14_colombia.png', dpi=150)
print("Imagen guardada en: /storage/emulated/0/scripts/miu_v14_colombia.png")
print(f"Promedio: {np.mean(periodos):.1f} días | Error total: {abs(np.mean(periodos)-target)/target*100:.2f}%")

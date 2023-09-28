import matplotlib.pyplot as plt
import numpy as np

# Función para actualizar y mostrar la imagen con colores aleatorios
def update_plot(interval):
    plt.clf()  # Borra el gráfico anterior
    plt.pcolormesh(np.random.rand(10, 10), cmap='coolwarm')
    plt.draw()  # Dibuja el nuevo gráfico
    plt.pause(interval)  # Pausa durante el intervalo especificado

# Solicitar al usuario el intervalo de tiempo en segundos
interval = float(input("Introduce cada cuantos segundos actualizar la figura: "))

plt.figure()
while True:
    update_plot(interval)
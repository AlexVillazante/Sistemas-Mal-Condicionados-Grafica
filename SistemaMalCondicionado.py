import numpy as np
import matplotlib.pyplot as plt

# Definir los valores de x
x = np.linspace(-10, 10, 400)

# Definir las ecuaciones
y1 = 2 - x  # Primera ecuación: x1 + x2 = 2
y2 = 2 - x  # Segunda ecuación (idéntica): x1 + x2 = 2

# Crear la figura
plt.figure(figsize=(8, 6))

# Graficar ambas ecuaciones
plt.plot(x, y1, label=r'$x_1 + x_2 = 2$', color='blue')

# Rango de la gráfica
plt.xlim([-10, 10])
plt.ylim([-10, 10])

# Etiquetas y título
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Gráfica del sistema A = [[1, 1], [1, 1]] y b = [2, 2]')
plt.legend()

# Mostrar la gráfica
plt.grid(True)
plt.show()

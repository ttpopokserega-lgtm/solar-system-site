import numpy as np
import matplotlib.pyplot as plt

def generate_harmonic_signal(F0, Fd, N):
    n = np.arange(N)
    signal = np.sin(2 * np.pi * F0 / Fd * n)
    return signal

# Параметри сигналу
F0 = 10  # Частота сигналу
Fd = 40  # Частота дискретизації
N = 128  # Кількість відліків

# Генерація сигналу
buffer = generate_harmonic_signal(F0, Fd, N)

# Відображення графіка
plt.figure()
plt.plot(buffer)
plt.title('Гармонійний сигнал')
plt.xlabel('Часові відліки')
plt.ylabel('Амплітуда')
plt.grid(True)
plt.show()
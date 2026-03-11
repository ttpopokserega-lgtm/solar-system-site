import numpy as np
import matplotlib.pyplot as plt

def generate_harmonic_signal(F0, Fd, N, phase_shift_period):
    n = np.arange(N)
    phase_shift = (np.floor(n / phase_shift_period) ) * np.pi / 10
    signal = np.sin(2 * np.pi * F0 / Fd * n + phase_shift)
    return signal

# Параметри сигналу
F0 = 1  # Частота сигналу
Fd = 100  # Частота дискретизації
N = 8192  # Кількість відліків
phase_shift_period = 256  # Кожні 256 семплів змінюємо фазу на pi/32
noise_power = 10**(-40/20)  # Амплітуди шуму для рівня -40 дБ

# Генерація сигналу
buffer = generate_harmonic_signal(F0, Fd, N, phase_shift_period)

# Додавання шуму
noise = np.random.rand(N) * noise_power
buffer_with_noise = buffer + noise

# Відображення графіка
plt.figure()
plt.plot(buffer_with_noise)
plt.title('Гармонійний сигнал з фазовим зсувом та шумом на рівні -40 дБ')
plt.xlabel('Часові відліки')
plt.ylabel('Амплітуда')
plt.grid(True)
plt.show()
import numpy as np
import matplotlib.pyplot as plt

def dft(signal):
    N = len(signal)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        X[k] = np.sum(signal * np.exp(-2j * np.pi * k * np.arange(N) / N))
    return X

def amplitude_to_db(amplitude):
    return 20 * np.log10(np.abs(amplitude))

# Створення вхідного сигналу
F0 = 1.17
Fd = 100
N = 256
n = np.arange(N)
signal = np.sin(2 * np.pi * F0 / Fd * n)
noise_power = 10**(-40/20)  # Амплітуди шуму для рівня -40 дБ

# Додавання шуму
noise = np.random.rand(N) * noise_power
buffer_with_noise = signal + noise

# Обчислення ДПФ
dft_result = dft(buffer_with_noise)

# Перетворення амплітуди в дБ
dft_result_db = amplitude_to_db(dft_result)

# Відображення графіка
plt.figure()
plt.plot(dft_result_db)
plt.title('ДПФ в масштабі дБ')
plt.xlabel('Частотні відліки')
plt.ylabel('Амплітуда (дБ)')
plt.grid(True)
plt.show()
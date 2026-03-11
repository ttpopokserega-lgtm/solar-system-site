import numpy as np
import matplotlib.pyplot as plt

# Функція для обчислення ДПФ
def dft(signal):
    N = len(signal)
    n = np.arange(N)
    k = n.reshape((N, 1))
    exp_matrix = np.exp(-2j * np.pi * k * n / N)
    dft_result = np.dot(exp_matrix, signal)
    return dft_result

# Функція для перетворення амплітуди в дБ
def amplitude_to_db(amplitude):
    return 20 * np.log10(np.abs(amplitude))

# Створення вхідного сигналу
F0 = 10
Fd = 1000
N = 8192
n = np.arange(N)
signal = np.sin(2 * np.pi * F0 / Fd * n)

# Обчислення ДПФ та FFT
dft_result = dft(signal)
fft_result = np.fft.fft(signal)

# Перетворення амплітуди в дБ
dft_result_db = amplitude_to_db(dft_result)
fft_result_db = amplitude_to_db(fft_result)

# Різниця у дБ між ДПФ та FFT
difference_db = dft_result_db - fft_result_db

# Відображення графіка різниці
plt.figure(figsize=(12, 6))
plt.plot(difference_db)
plt.title('Різниця у масштабі дБ між ДПФ та FFT')
plt.xlabel('Частотні відліки')
plt.ylabel('Різниця в дБ')
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Data respon sistem (waktu dan output)
time = np.array([0, 1, 2, 3, 4, 5])
output = np.array([0, 1, 3, 4, 3, 1])

# Fungsi untuk menghitung kesalahan kuadrat antara data respon dan respon simulasi PID
def objective(params):
    Kp, Ki, Kd = params
    y = np.zeros_like(output)
    error_sum = 0

    # Simulasi respon sistem dengan parameter PID yang diberikan
    for i in range(1, len(output)):
        dt = time[i] - time[i-1]
        error = output[i] - y[i-1]
        y[i] = y[i-1] + (Kp * error) + (Ki * error * dt) + (Kd * (error - (output[i-1] - y[i-1])) / dt)
        error_sum += error ** 2

    return error_sum

# Inisialisasi parameter awal untuk optimisasi
initial_guess = [1, 1, 1]

# Optimisasi parameter PID menggunakan metode Nelder-Mead
result = minimize(objective, initial_guess, method='Nelder-Mead')

# Mendapatkan parameter PID hasil tuning
Kp_opt, Ki_opt, Kd_opt = result.x

# Cetak hasil tuning PID
print(f"Kp: {Kp_opt}, Ki: {Ki_opt}, Kd: {Kd_opt}")

# Plot respon sistem asli dan hasil simulasi PID setelah tuning
plt.plot(time, output, label='Data Respon Sistem Asli')
plt.plot(time, y, label='Respon Simulasi PID')
plt.xlabel('Waktu')
plt.ylabel('Output')
plt.legend()
plt.show()

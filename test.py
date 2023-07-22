import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import controlpy

# Contoh data respon sistem (waktu dan output)
time = np.array([0, 1, 2, 3, 4, 5])
output = np.array([0, 1, 3, 4, 3, 1])

# Fungsi untuk menghitung kesalahan kuadrat antara data respon dan respon simulasi PID
def objective(params):
    Kp, Ki, Kd = params
    system = controlpy.TransferFunction([Kp], [1, 0]) + controlpy.TransferFunction([Ki], [1]) / s + controlpy.TransferFunction([Kd * s], [1])
    _, y = controlpy.forced_response(system, time, output)
    return np.sum((y - output) ** 2)

# Inisialisasi parameter awal untuk optimisasi
initial_guess = [1, 1, 1]

# Optimisasi parameter PID menggunakan metode Nelder-Mead
result = minimize(objective, initial_guess, method='Nelder-Mead')

# Mendapatkan parameter PID hasil tuning
Kp_opt, Ki_opt, Kd_opt = result.x

# Cetak hasil tuning PID
print(f"Kp: {Kp_opt}, Ki: {Ki_opt}, Kd: {Kd_opt}")

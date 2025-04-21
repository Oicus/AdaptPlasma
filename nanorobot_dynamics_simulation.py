import numpy as np
from scipy.integrate import odeint

# Parametreler
m = 1e-18  # kg (nanorobot kütlesi)
gamma = 6e-9  # kg/s (viskoz sönüm)
k_aptamer = 2e-12  # N/(mol/m^3)
B_strength = 0.1  # T (manyetik alan)
target_gradient = 5e-3  # mol/m^4 (hedef protein konsantrasyon gradiyenti)

def nanorobot_dynamics(r, t):
    x, y, vx, vy = r
    F_magnetic = 1e-15 * B_strength  # Süperiletken SQD tepkisi
    F_brownian = np.sqrt(2*gamma*1e-21)*np.random.randn(2)  # Termal gürültü
    F_bio = k_aptamer * target_gradient * np.array([x, y])
    
    dvxdt = (-gamma*vx + F_magnetic + F_brownian[0] - F_bio[0]) / m
    dvydt = (-gamma*vy + F_magnetic + F_brownian[1] - F_bio[1]) / m
    return [vx, vy, dvxdt, dvydt]

# Başlangıç koşulları ve simülasyon
r0 = [0, 0, 0, 0]
t = np.linspace(0, 1e-3, 1000)  # 1 ms simülasyon
result = odeint(nanorobot_dynamics, r0, t)

print("Son Konum (µm):", result[-1, :2]*1e6)

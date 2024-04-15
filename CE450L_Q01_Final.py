import math

Kp = 8
Ki = 5
Kd = 1.6
samp_rate = 1

tau = 5
zeta = 0.55
initial_temp = 81.5
setpoint = 100
u_value_initial = 800

error1 = 0
error2 = 0

def calculate_temp(t):
    return 100 * (1 - math.exp(-zeta * t*0.1 / tau) * (math.cos(math.sqrt(1 - zeta**2) / tau * t*0.1) + zeta / math.sqrt(1 - zeta**2) * math.sin(math.sqrt(1 - zeta**2) / tau * t*0.1)))

for t in range(1, 41): 
    T = calculate_temp(t * samp_rate)
    
    error = setpoint - T
    
    delta_u = Kp * (error - error1) + Ki * error + Kd * (error - 2 * error1 + error2)
    

    u_value_initial += delta_u
    error2 = error1
    error1 = error
    
    print(f"Time: {t * samp_rate:.1f}s, Measured Temperature: {T:.1f}°C, Error: {error:.1f}, Delta u: {delta_u:.1f}, Control Signal: {u_value_initial:.1f}")

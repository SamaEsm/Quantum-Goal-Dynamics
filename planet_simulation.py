import numpy as np 
import matplotlib.pyplot as plt
G = 6.67430e-11   # gravitational constant
mass_sun = 1.989e30
mass_earth = 5.972e24
# فاصله زمین تا خورشید (متر)
distance_au = 1.496e11 

# سرعت مداری زمین (متر بر ثانیه - حدود ۳۰ کیلومتر بر ثانیه)
v_orbital = 29780 

# موقعیت و سرعت اولیه زمین (بردار)
pos_earth = np.array([distance_au, 0.0])
vel_earth = np.array([0.0, v_orbital])

# مشخصات مریخ
mass_mars = 0.64171e24
dist_mars_au = 1.524 * 1.496e11 # فاصله مریخ تا خورشید
v_orbital_mars = 24070 # سرعت مداری مریخ (متر بر ثانیه)

pos_mars = np.array([dist_mars_au, 0.0])
vel_mars = np.array([0.0, v_orbital_mars])

# لیست برای ذخیره مسیر مریخ
mars_coords = []

# موقعیت و سرعت اولیه خورشید
pos_sun = np.array([0.0, 0.0])
vel_sun = np.array([0.0, 0.0])
def get_accelerations(pos_e, pos_s):
    # ۱. محاسبه بردار فاصله بین زمین و خورشید
    r_vector = pos_s - pos_e
    
    # ۲. محاسبه اندازه فاصله (اعداد فیثاغورثی)
    distance = np.linalg.norm(r_vector)
    
    # ۳. محاسبه اندازه شتاب گرانش
    acc_magnitude = G * mass_sun / (distance**2)
    
    # ۴. تبدیل شتاب به بردار (در جهت خورشید)
    acc_vector = acc_magnitude * (r_vector / distance)
    
    return acc_vector
dt = 24 * 3600  # هر گام زمانی رو یک روز (به ثانیه) در نظر می‌گیریم
total_steps = 365 # شبیه سازی برای یک سال

# لیست‌هایی برای ذخیره مسیر که بتونیم بعدا رسمشون کنیم
earth_coords = []
for i in range(total_steps):
    # ذخیره موقعیت فعلی زمین
    earth_coords.append(pos_earth.copy())
    mars_coords.append(pos_mars.copy())    
    # الف) محاسبه شتاب فعلی
    acc_e = get_accelerations(pos_earth, pos_sun)
    
    # ب) به‌روزرسانی سرعت (v = v + a*dt)
    vel_earth = vel_earth + acc_e * dt
    
    # ج) به‌روزرسانی مکان (x = x + v*dt)
    pos_earth = pos_earth + vel_earth * dt
# تبدیل لیست مختصات به یک آرایه برای کار راحت‌تر
    # محاسبات مریخ (این رو اضافه کن)
    acc_m = get_accelerations(pos_mars, pos_sun)
    vel_mars = vel_mars + acc_m * dt
    pos_mars = pos_mars + vel_mars * dt
earth_coords = np.array(earth_coords)


# ساخت شکل نمودار
plt.figure(figsize=(8, 8))

# رسم خورشید در مرکز (یک نقطه زرد بزرگ)
plt.scatter(0, 0, color='yellow', s=200, label='Sun')

# رسم مسیر حرکت زمین
plt.plot(earth_coords[:, 0], earth_coords[:, 1], color='blue', label='Earth Orbit')

# اضافه کردن جزئیات به نمودار
plt.axhline(0, color='grey', lw=0.5)
plt.axvline(0, color='grey', lw=0.5)
plt.title("Earth's Orbit Simulation - Magnus Team")
plt.xlabel("X (meters)")
plt.ylabel("Y (meters)")
plt.legend()
plt.axis('equal') # این خط خیلی مهمه تا دایره، بیضی دیده نشه!
plt.grid(True, linestyle='--', alpha=0.6)
plt.plot(earth_coords[:, 0], earth_coords[:, 1], color='blue', label='Earth')
plt.plot(mars_coords[:, 0], mars_coords[:, 1], color='red', label='Mars') # اضافه کن


# نمایش نهایی
plt.show()

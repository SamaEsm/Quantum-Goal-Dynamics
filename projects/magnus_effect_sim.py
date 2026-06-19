import numpy as np
import matplotlib.pyplot as plt
g=9.81
rho=1.225   #چگالی هوا
R =0.11      # شعاع توپ فوتبال استاندارد (m)
m = 0.45          # جرم توپ (kg)
C_d = 0.25        # ضریب پسا (Drag Coefficient)
C_m = 0.15        # ضریب مگنوس (Magnus Coefficient)
A = np.pi * R**2  # مساحت سطح مقطع توپ

def simulate_kick(v0_mag, angle_deg, spin_rpm):
    # تبدیل واحدها
    angle_rad = np.radians(angle_deg)
    omega = (spin_rpm * 2 * np.pi) / 60  # تبدیل RPM به رادیان بر ثانیه
    # مولفه‌های سرعت اولیه (فرض می‌کنیم ضربه در صفحه xy زده میشه)
    vx = v0_mag * np.cos(angle_rad)
    vy = 0  # انحراف عرضی در ابتدا صفر است
    vz = v0_mag * np.sin(angle_rad)
    # شرایط اولیه موقعیت
    x, y, z = [0.0], [0.0], [0.0]
    dt = 0.01  # گام زمانی (ثانیه)
    curr_vx, curr_vy, curr_vz = vx, vy, vz
    curr_x, curr_y, curr_z = 0.0, 0.0, 0.0
    while curr_z >= 0: # تا زمانی که توپ به زمین نخورده
        v_vec = np.array([curr_vx, curr_vy, curr_vz])
        v_mag = np.linalg.norm(v_vec)
        
        # ۱. نیروی گرانش (رو به پایین)
        F_g = np.array([0, 0, -m * g])
        
        # ۲. نیروی پسا (مخالف جهت حرکت)
        F_d = -0.5 * rho * A * C_d * v_mag * v_vec
        
        # ۳. نیروی مگنوس (عمود بر جهت حرکت و محور چرخش)
        # فرض می‌کنیم توپ دور محور عمودی (z) می‌چرخه تا کات عرضی بگیره
        spin_axis = np.array([0, 0, 1]) 
        F_m = 0.5 * rho * A * C_m * R * np.cross(spin_axis * omega, v_vec)
        
        # برآیند نیروها و شتاب
        F_total = F_g + F_d + F_m
        ax, ay, az = F_total / m
        
        # بروزرسانی سرعت (روش اویلر)
        curr_vx += ax * dt
        curr_vy += ay * dt
        curr_vz += az * dt
        
         # بروزرسانی موقعیت
        curr_x += curr_vx * dt
        curr_y += curr_vy * dt
        curr_z += curr_vz * dt
        
        # ذخیره در لیست‌ها
        x.append(curr_x)
        y.append(curr_y)
        z.append(curr_z)
        
    return x, y, z

# --- تست مدل ---
# فرض کن یک ضربه ایستگاهی با سرعت ۱۰۰ کیلومتر بر ساعت و کات ۶۰۰ دور در دقیقه
x_traj, y_traj, z_traj = simulate_kick(v0_mag=28, angle_deg=20, spin_rpm=600)

print(f"برد نهایی ضربه: {x_traj[-1]:.2f} متر")
print(f"میزان انحراف عرضی (کات): {y_traj[-1]:.2f} متر") 

from mpl_toolkits.mplot3d import Axes3D

# ایجاد شکل و محور سه‌بعدی
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# رسم مسیر حرکت
ax.plot(x_traj, y_traj, z_traj, label='Ball Trajectory', color='white', linewidth=2)

# زیباسازی نمودار (شبیه زمین فوتبال)
ax.set_facecolor('#2e7d32') # رنگ سبز چمن
ax.set_xlabel('Length (m)')
ax.set_ylabel('Sideways Curve (m)')
ax.set_zlabel('Height (m)')
ax.set_title('Real Madrid Physics: The Magnus Effect')
ax.legend()

plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# ۱. خواندن فایل داده (انگار داری لیست آزمایشگاه رو باز می‌کنی)
df = pd.read_csv('sensor_data.csv')

# ۲. ساخت ستون نسبت فشار به دما (P/T)
# این نسبت در حجم ثابت طبق قوانین گازها باید مقدار ثابتی باشه
df['P_T_Ratio'] = df['Pressure'] / df['Temperature']

# ۳. پیدا کردن ردیفی که بیشترین فشار رو داره
# idxmax ایندکسِ (شماره ردیف) بیشترین مقدار رو پیدا می‌کنه
idx_max_pressure = df['Pressure'].idxmax()
max_row = df.loc[idx_max_pressure]

print("--- نتیجه تحلیل سنسور ---")
print(f"بیشترین فشار ثبت شده در ردیف شماره {idx_max_pressure} است:")
print(max_row)
print("-----------------------")

# ۴. رسم نمودار برای درک بهتر رابطه P و T
plt.figure(figsize=(8, 5))
plt.scatter(df['Temperature'], df['Pressure'], color='purple', label='Data Points')
plt.plot(df['Temperature'], df['Pressure'], color='gold', alpha=0.3) # یک خط کمرنگ برای دیدن روند

plt.title('Physics Lab: Pressure vs Temperature', fontsize=14)
plt.xlabel('Temperature (K)', fontsize=12)
plt.ylabel('Pressure (kPa)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()

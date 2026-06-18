#پروژه اول
import pandas as pd
df = pd.DataFrame({
    'Time': list(range(0, 61, 10)),
    'counts': [100, 72, 51, 36, 25, 18, 12]
})
        #محاسبه میانگین
avg=df['counts'].mean()
print(f"Average : {avg}")
        #فیلتر کردن داده ها
low_counts= df[df['counts'] <50]
print("\nExperiments with low counts:")
print(low_counts)
        #محاسبه تفاضل یا نرخ تغییرات
df['Diff_Counts'] = df['counts'].diff()
print(df)
 

 #پروژه دوم
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,11,100)   #ساختن صد نقطه بین 0 تا 10
y= np.sin(x)
noise=np.random.normal(0,0.1,100)
y_noisy = y + noise
        #رسم نمودار در یم صفحه کنار هم
plt.subplot(1,2,1)
plt.plot(x, y, color='purple')
plt.title("Clean Signal")

plt.subplot(1,2,2)
plt.plot(x, y_noisy, color='orange')
plt.title("Noisy Signal (Physics Reality)")

plt.show()


#پروژه سوم
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('sensor_data.csv')
df['P_T_Ratio'] = df['Pressure'] / df['Temperature']
idx_max_pressure = df['Pressure'].idxmax()
max_row = df.loc[idx_max_pressure]

print("--- نتیجه تحلیل سنسور ---")
print(f"بیشترین فشار ثبت شده در ردیف شماره {idx_max_pressure} است:")
print(max_row)
print("-----------------------")
plt.figure(figsize=(8, 5))
plt.scatter(df['Temperature'], df['Pressure'], color='purple', label='Data Points')
plt.plot(df['Temperature'], df['Pressure'], color='gold', alpha=0.3)
plt.title('Physics Lab: Pressure vs Temperature', fontsize=14)
plt.xlabel('Temperature (K)', fontsize=12)
plt.ylabel('Pressure (kPa)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()



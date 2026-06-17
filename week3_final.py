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



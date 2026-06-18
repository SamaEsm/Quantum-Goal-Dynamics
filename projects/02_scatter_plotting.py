#رسم نمودار natplotlib
import matplotlib.pyplot as plt
seasons = ['2020', '2021', '2022', '2023', '2024']
goals = [82, 78, 85, 92, 95]
        # ایجاد بوم و سیستم مختصات
fig, ax = plt.subplots(figsize=(8, 5))
        # رسم نمودار خطی
ax.plot(seasons, goals, marker='o', linestyle='-', color='blue')
        # افزودن برچسب‌های علمی
ax.set_title('Real Madrid Goal Performance (Last 5 Years)')
ax.set_xlabel('Season')
ax.set_ylabel('Number of Goals')
ax.grid(True) # فعال کردن شبکه برای خوانایی بیشتر
plt.show()

#تمرین
import matplotlib.pyplot as plt
seasons = ['2020', '2021', '2022', '2023', '2024']
goals = [82, 78, 85, 92, 95]
fig, ax= plt.subplots(figsize=(10,7))
ax.plot(seasons, goals, marker='o', linestyle='-', color='black')
ax.set_title('Performance Analysis')
ax.set_xlabel('Season')
ax.set_ylabel('Number of Goals')
ax.set_ylim(0,110)
ax.grid(True)
plt.show()

#تمرین
seasons = ['2020', '2021', '2022', '2023', '2024']
goals = [82, 78, 85, 92, 95]
wins = [25, 23, 26, 28, 29]
fig2, ax2 = plt.subplots(figsize=(10, 7)) 
ax2.plot(seasons, goals, color='gold', label='Total Goals')
ax2.plot(seasons, wins, color='red', label='Total Wins')
ax2.set_title('Performance Analysis')
ax.set_xlabel('Season')
ax.set_ylabel('Count / Quantity')
ax.set_ylim(0,110)
ax.grid(True, linestyle='--')
ax2.legend()
plt.show()

#محور ایگرگ دوم Twin Axes
seasons = ['2020', '2021', '2022', '2023', '2024']
goals = [82, 78, 85, 92, 95]
wins = [25, 23, 26, 28, 29]
fig, ax1 = plt.subplots(figsize=(10, 7))
ax1.plot(seasons, goals, color='gold', label='Goals')
ax1.set_ylabel('Goals Scale', color='gold')
ax2 = ax1.twinx()
ax2.plot(seasons, wins, color='purple', label='Wins')
ax2.set_ylabel('Wins Scale', color='purple')
ax1.tick_params(axis='y', labelcolor='gold')
ax2.tick_params(axis='y', labelcolor='purple')
plt.show()

#Seaborn
#نمودار توزیع Histogram
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
sns.set_theme()
gredse=np.random.normal(loc=15, scale=3, size=14)
                #به ترتیب از چپ میانگین  و انحراف از معیار و تعداد
gredse=np.clip(gredse,0,20)
plt.figure(figsize=(10,7))
sns.histplot(gredse, kde=True, color="gold")
plt.title("GREDSE")
plt.xlabel("gredse")
plt.ylabel("Frequency")
plt.show()

#تمرین
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="whitegrid")
study_hours = [10, 20, 30, 40, 50]
grades = [20, 16, 17, 19, 15]
coffee_cups = [100, 200, 500, 800, 1000]
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x=study_hours,
    y=grades,
    size=coffee_cups,
    sizes=(50, 400),
    color="purple"
)
plt.title("Study Progress vs Coffee Consumption ☕")
plt.xlabel("Hours of Study")
plt.ylabel("Physics Grade")
plt.show()














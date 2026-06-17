#لیست تو در تو
results=[ 
    ["sama",18],
    ["ali",15],
    ["sara",20],
    ["mina",17]
]
scores=[]
for row in results:
    scores.append(row[1])
avg=sum (scores)/len(scores)
print("میانگین نمرات",avg)
best_name = None
best_score = -2

for name, score in results:
    if score > best_score:
        best_score = score
        best_name = name

print(best_name, best_score)
name_list=[]
for row in results:
    name_list.append(row[0])
print("لیست اسامی", name_list)

#دیکشنری
students=[{"name":"sama","score":18},
          {"name":"ali","score":15},
          {"name":"sara",'score':20},
          {"name":"mina","score":17}
          ]
students.append({"name":"reza",'score':16})
total=0
for s in students:
    total += s["score"]
avg= total/len(students)
print("میانگین:",avg)
best= students[0]
for s in students:
    if s["score"]>best["score"]:
        best=s
print(best["name"], best["score"])

#تاپل و ست
city=["tehran","madrid","shiraz","tehran","yazd","madrid","yazd"]
unique= set(city)
print(unique)
rgb=(225,128,0)
print(rgb[1])

#فایل خوانی و فایل نویسی 
#نوشتن یک فایل txt داخل پوشه data
with open("data/cities.txt","w",encoding="utf-8") as f:
    for c in city:
        f.write(c+"n/")
#خواندن همان فایل و ساخت set از روی آن
with open("data/cities.txt","r",encoding="utf-8") as f:
    lines=f.read().splitlines()
unique=set(lines)
print(unique)

#تمرین
with open("data/temps.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()
temps = []
for line in lines:
    temps.append(float(line))
avg = sum(temps) / len(temps)
print("میانگین دما:", avg)

#تمرین قدم به قدم برای جا افتادن این موضوع
#گام 1: فقط بخون و چاپ کن
with open("data/temps.txt", "r", encoding="utf=8") as f:
    lines= f.read().splitlines()
print(lines)
print(type(lines[0]))
# گام 2: تبدیل به عدد و چاپ نتایج
with open ("data/temps.txt","r", encoding="utf=8") as f:
    lines=f. read().splitlines()
temps=[]
for line in lines:
    temps.append(float(line))
print(temps)
print(type(temps[0]))
# اگه یه خط خالی داشتیم و اررو می داد (تمیز کاری می کنه)
with open ("data/temps.txt", "r", encoding="utf-8") as f:
    temps = []
    for line in f:
        line = line.strip()
        if line:  # خط خالی نباشه
            temps.append(float(line))

print(temps)

#تمرین(فیلتر مردن داده ها)
with open ("data/temps.txt", "r", encoding="utf-8") as f:
    lines= f. read().splitlines()
temps=[]
removed_count = 0  # یک شمارنده برای دماهای حذف شده
for line in lines:
    temp = float(line)
    if temp > 20:
        temps.append(temp) # فقط اگر بزرگتر از 20 بود اضافه کن
    else:
        removed_count += 1 # وگرنه بشمارش که حذف شده
print("لیست دماهای بالای ۲۰:", temps)
print("تعداد دماهای حذف شده:", removed_count)

#تمرین ۲: ذخیره نتایج در فایل جدید (خروجی گرفتن)
with open ("data/temps.txt", "r", encoding="utf-8") as f:
    lines= f. read().splitlines()
kelvin_temps =[]
for line in lines:
    celsius= float(line)
    kelvin=celsius+273.15
    kelvin_temps.append(kelvin) 
with open("data/kelvin.txt", "w", encoding="utf-8") as f:
    for t in kelvin_temps:
        f.write(str(t) + "\n")

#تمرین ۳ (چالش کوچک): پیدا کردن اکسترمم‌ها
with open("data/temps.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

# اگر فایل خالی بود، جلوگیری از خطا
if len(lines) == 0:
    print("فایل خالی است!")
else:
    first = float(lines[0])
    max_val = first
    min_val = first

    for line in lines[1:]:  # از عضو دوم به بعد
        temp = float(line)

        if temp > max_val:
            max_val = temp

        if temp < min_val:
            min_val = temp

    print("بیشترین دما:", max_val)
    print("کمترین دما:", min_val)

#دیکشنری
#تمرین1
student={
    "name":"sama",
    "major":"physics",
    "fav_team":"real madrid"
}
print("نام دانشجو:", student ["name"])
print("رشته:", student["major"])
print("تیم مورد علاقه:", student["fav_team"])

#تمرین2
book={
    "title":"a brief history of time",
    "author":"stephen hawking",
    "page":212
}
print(book["title"])
print(book["author"])
print(book["page"])

#تمرین 3
particle={
    "name": "electron",
    "mass": 9.11e-31,
    "charge": -1.6e-19
}
print("particle:",particle["name"])
print("mass:", particle["mass"])
print("charge:", particle["charge"])

#حلقه زدن روی دیکشنری ها
#تمرین1
book={
    "title":"a brief history of time",
    "author":"stephen hawking",
    "page":212
}
for key, value in book.items():
    print(key,":",value)

#تمرین2
measurement = {
    "temperature": 22.5,
    "pressure": 1.01,
    "time": 5.0
}
for key,value in measurement.items():
    print(key,":",value)
measurement["temperature"]=23.0
for key,value in measurement.items():
    print(key,":",value)


#لیستِ دیکشنری‌ها (List of Dictionaries)
#تمرین
motion_data = [
    {"time": 0.0, "position": 0.0},
    {"time": 1.0, "position": 2.5},
    {"time": 2.0, "position": 10.0},
    {"time": 3.0, "position": 22.5}
]
print("---motion data---")
for item in motion_data:
    t = item["time"]
    p = item["position"]
    print(f"At time {t} s, position is {p} m")
print("\n--- Velocity Calculation ---")
# بخش دوم: محاسبه و نمایش فرمول سرعت متوسط
initial_state = motion_data[0]
final_state = motion_data[-1]
x_initial = initial_state["position"]
t_initial = initial_state["time"]
x_final = final_state["position"]
t_final = final_state["time"]
delta_x = x_final - x_initial
delta_t = t_final - t_initial
# نمایش فرمول با LaTeX
formula_latex = r"$v_{avg} = \frac{\Delta x}{\Delta t} = \frac{x_{final} - x_{initial}}{t_{final} - t_{initial}}$"
print(f"Formula for average velocity: {formula_latex}")
v_avg = delta_x / delta_t
print(f"The average velocity is: {v_avg} m/s")

#تمرین2
grades = [
    {"name": "Sama", "score": 19.5},
    {"name": "Ali", "score": 14.0},
    {"name": "Sara", "score": 17.0}
]
for item in grades:
    if item["score"] >15:
        print(f"Top Student: {item['name']} with score: {item['score']}")

#تمرین3
voltages = [
    {"trial": 1, "value": 5.1},
    {"trial": 2, "value": 4.9},
    {"trial": 3, "value": 12.5}, 
    {"trial": 4, "value": 5.0},
    {"trial": 5, "value": 4.8}
]
for item in voltages:
    if item["value"]>6:
        print(f"warning! trial {item['trial']} is too high : {item['value']}")

#تمرین3
songs = [
    {"title": "Dynamite", "views_billions": 1.8},
    {"title": "Life Goes On", "views_billions": 0.6},
    {"title": "Butter", "views_billions": 1.2},
    {"title": "Spring Day", "views_billions": 0.5}
]
for item in songs:
    if item["views_billions"] >1.0:
        print( item['title'])

#تمرین3
particles = [
    {"name": "Proton", "mass": 1.67},
    {"name": "Electron", "mass": 0.0009},
    {"name": "Neutron", "mass": 1.68}
]
for item in particles: 
    if item["name"] != "Electron":
        M= item["mass"]*2
        print(M)

#توابع
def celsius_to_kelvin(celsius):
    kelvin=celsius+273.15
    return kelvin
result = celsius_to_kelvin(30)
print(result)

#تابع و لیست 
def convert_mass_list(grams):
    kilograms=[]
    for item in grams:
        kilograms.append(item/1000)
    return kilograms
my_data=[100,500,2000,50]
result=convert_mass_list(my_data)
print(result)
#تمرین
def clean_temperature_data(temps):
    clean_list=[]
    for item in temps:
        if item> -273.15:
            clean_list.append(item)
    return clean_list
rew_temps=[23,-300,10,-273.15,100,-500]
result=clean_temperature_data(rew_temps)
print(result)

#هفته سوم جلسه اول 
#numpy
#تمرین
import numpy as np
positions=np.array([10,20,30,40,50])
velocities=np.array([2,2,2,2,2])
new_positions=positions+velocities
print(f"new_positions shape: {new_positions.shape}")

#تمرین slicing 2
observations=np.array([1,2,4,8,16,32,64,128,256,512])
from_secend= observations[5:]
avg=np.mean(from_secend)
print(avg)

#تمرین start, stop, step --- start, stop, num
x = np.linspace(0, 2*np.pi, 5)
print(x)

#تکلیف
fitness_levels=np.linspace(0,100*np.pi,21)
x=fitness_levels[:10]
print(x)
avg_levels=np.mean(x)
print(avg_levels)
print(avg_levels>50)

#هفته سوم جلسه دوم 
#ماتریس
#تمرین
import numpy as np
F1=np. array([10,20,30])
F2=np.array([5,-5,10])
result= np.dot(F1,F2)
print(result)

#تمرین
import numpy as np
scores = np.array([[85, 90],
                    [80, 95]])
inverse=np.linalg.inv(scores)
print(inverse)

#حل دستگاه معادلات 
import numpy as np
v = np.array([12.5, 13.2, 12.8, 15.0, 14.1]) 
avg=np.mean(v)
normalizatin= v- avg
print(normalizatin)
masking= v[v>13]
print(masking)

#pandas
import pandas as pd

data = {
    "player": ["Ronaldo", "Messi", "Mbappe", "Neymar"],
    "goals": [25, 22, 27, 18]
}
df = pd.DataFrame(data)
print(df)
print(df["goals"])

#تمرین
import pandas as pd
# داده‌های فرضی چند آزمایش
data = {
    'experiment_id': [1, 2, 3, 4, 5, 6],
    'velocity': [12.5, 14.2, 10.8, 19.5, 13.0, 15.2],
    'temp': [25, 26, 24, 28, 25, 27]
}
df = pd.DataFrame(data)
          # ۱. میانگین سرعت کل آزمایش‌ها
avg_v = df['velocity'].mean()
print(f"Average Velocity: {avg_v}")
          # ۲. فیلتر کردن: فقط آزمایش‌هایی که سرعتشون بالای 14 بوده
high_speed = df[df['velocity'] > 14]
print("\nExperiments with high speed:")
print(high_speed)

#تمرین
import pandas as pd
data={
    "player": ["Ronaldo", "Messi", "Mbappe", "Neymar"],
    "goals": [25, 22, 27, 18]
}
df=pd.DataFrame(data)
avg_goal=df['goals'].mean()
print(f"average goal: {avg_goal}")
high_avg=df[df["goals"]>avg_goal]
print("\nExperiments with high goals:")
print(high_avg)
      #خواندن فایل 

#تمرین
import pandas as pd
data = {
    'object': ['A', 'B', 'C', 'D'],
    'mass': [1.2, 2.5, 0.8, 3.0],      # به کیلوگرم
    'volume': [0.002, 0.005, 0.001, 0.006] # به متر مکعب
}
df= pd.DataFrame(data)
print(df)
df['density']=df['mass']/df['volume']
print(df)
avg_density=df["density"].mean()
print(f"/nAverage Density:{avg_density}")
high_density = df[df['density'] > 600]
print("\nExperiments with high density:")
print(high_density)
        # مرتب کردن بر اساس چگالی (نزولی)
df_sorted = df.sort_values(by='density', ascending=False)
print("\nSorted by Density:")
print(df_sorted)

 # ورود به دنیای فایل‌ها (CSV)
import pandas as pd
import matplotlib.pyplot as plt
            # فرض کن این فایل رو داریم:
            # df = pd.read_csv('stars.csv')
 #تمرین
import pandas as pd
data={
    'days':[1,2,3,4,5],
    'temps':[5800,5950,6100,6050,6200]
}
df= pd.DataFrame(data)
plt.plot(df['days'],df['temps'], label='star temps', color='gold', marker='o')
plt.legend()
plt.xlabel('Days')
plt.ylabel('Temperature (K)')
plt.title('Stellar Temperature Variation')
plt.grid(True)
plt.xlabel('Days')
plt.ylabel('Temperature (K)')
plt.title('Stellar Temperature Variation')
plt.grid(True)
plt.show() 

#نمودار میله ای
import pandas as pd
import matplotlib.pyplot as plt
data={
    'particle_type':[450,620,800],
    'count':['Alpha','Beta','gamma']
}
df= pd.DataFrame(data)
print(df)
plt.bar(df['particle_type'],df['count'],color='purple')
plt.title('Nuclear Particles Count')
plt.xlabel('Type of Particle')
plt.ylabel('Quantity')
plt.show()
        #فیلتر کردن داده ها
filtered_df=df[df['count']>500]
plt.bar(filtered_df['particle_type'], filtered_df['count'],color='purple')
plt.title('High Intensity Particles (>500)')
plt.show()

#خواندن فایل
import pandas as pd
     # خواندن فایل از پوشه data
import pandas as pd
df = pd.read_csv('data/temps.txt')
avg_temp = df['Temperature'].mean()
print("Average Temperature:", avg_temp)
df = pd.read_csv('data/temps.txt')
     # چاپ کردن کل جدول در خروجی
print(df)
     # چاپ کردن فقط ستون دما
     # print(df['Temperature'])
#میانگین دما
import pandas as pd
df = pd.read_csv('data/temps.txt')
avg_temp = df['Temperature'].mean()
print("Average Temperature:", avg_temp)

#بیشترین دما
max_temp = df['Temperature'].max()
print("Maximum Temperature:", max_temp)

#رسم نمودار
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data/temps.txt')
plt.plot(df['Time'], df['Temperature'], marker='o', color='purple')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (K)')
plt.title('Temperature vs Time')
plt.grid(True)
plt.show() 

#تمرین 
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data/temps.txt')
plt.plot(df['Time'], df['Temperature'], marker='o', color='purple')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (K)')
plt.title('Temperature vs Time')
plt.grid(True)
plt.show() 
max_temp = df['Temperature'].max()
print("Maximum Temperature:", max_temp)
min_temp = df['Temperature'].min()
print("Minimum Temperature:", min_temp)
avg_temp = df['Temperature'].mean()
print("Average Temperature:", avg_temp)
delta_t = df['Temperature'].max() - df['Temperature'].min()
print("Temperature Range:", delta_t)
df['Delta_T'] = df['Temperature'] - df['Temperature'][0]
print(df)








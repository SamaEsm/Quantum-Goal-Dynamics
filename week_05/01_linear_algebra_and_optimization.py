#بردار
import numpy as np 
v= np. array ([2,5,1])
print(v)
 #ماتریس
x= np. array([
    [120,3,10],
    [80,2,5],
    [200,4,2]
])
#تمرین1
A=np. array([
      [1,3],
      [2,4]
])
B=np. array([
      [5,7]
      [6,8]
])
C=np.dot(A,B)
print(C)

#تمرین2
A= np.array([
      [1,2,3]
      [4,5,6]
])
AT=A.T
print(AT)

#تمرین3
v=np. array([
      [2,4,6]
])
W=v@v
print(W)
#ضزب بردار در وزن ها 
x= np.array([3,4])
w=np. array([2,5])
y=np.dot(x,w)
print(y)
#تمرین 
import numpy as np
data= np.array([
    [10,0.5],
    [20,1.0],
    [30,1.5]
])
weights= np. array ([0.1, 2.0])
result= np.dot(data,weights)
print(f"نتیجه ترکیب خطی: {result}")
#تمرین
X= np. array ([1,2,3,4,5])
y_true = np.array([2, 4, 6, 8, 10])
        # حدس اولیه مدل (پارامتر w)
w_guess = 1.5 
        # پیش‌بینی مدل
y_pred = w_guess * X
        # محاسبه خطا (Mean Squared Error)
mse = np.mean((y_pred - y_true)**2)

print(f"حدس مدل: {w_guess}")
print(f"میزان خطا (Loss): {mse}")
 
#تمرین (محاسبه مشتق)
X= np. array([1,2,3,4,5])
y_true= np.array([2,4,6,8,10])
w_guess= 0
        #محاسبه خطا
y_pred= y_true* X
mse= np.mean((y_pred- y_true)**2)
        # این یک راهنمایی برای ساختارِ داخل حلقه‌ست:
n = len(X) # تعداد داده‌ها
alpha = 0.01 # نرخ یادگیری (چقدر قدم‌های بزرگ برداریم)
for i in range(1000):
         # قدم ۱: پیش‌بینی مدل با w فعلی
    y_pred = w_guess * X
        # قدم ۲: محاسبه خطا
    error = y_pred - y_true
        # قدم ۳: محاسبه گرادیان (شیب)
        # راهنمایی: فرمول ریاضی مشتق 2 * (error) * X هست که باید میانگین بگیری
    gradient = (2 / n) * np.sum(error * X)
        # قدم ۴: آپدیت کردن w
    w = w - (alpha * gradient)
if i % 100 == 0:
        print(f"Iteration {i}: w = {w}")

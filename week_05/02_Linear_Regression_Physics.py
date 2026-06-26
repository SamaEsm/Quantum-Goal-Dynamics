#Linear Regression via Gradient Descent
#در این مدل ما دو چیز را کشف می کنیم: شیب خط و عرض از مبدا 
import numpy as np
import matplotlib.pyplot as plt
        # ۱. داده‌های فرضی (مثلاً رابطه طول فنر و وزنه)
x = np.array([1, 2, 3, 4, 5]) 
y = np.array([2, 4, 6, 8, 10]) # می‌بینیم که y = 2x هست، پس هدف مدل پیدا کردن w=2 است
        # ۲. مقادیر اولیه تصادفی
w = 0.0
b = 0.0
learning_rate = 0.01
epochs = 100 # تعداد دفعاتی که مدل تمرین می‌کنه
        # ۳. حلقه آموزش (Gradient Descent)
for i in range(epochs):
        # پیش‌بینی مدل
    y_pred = w * x + b
        # محاسبه مشتق‌ها (گرادیان) نسبت به w و b
    dw = (-2 / len(x)) * sum(x * (y - y_pred))
    db = (-2 / len(x)) * sum(y - y_pred)
        # آپدیت کردن وزن‌ها در جهت عکس گرادیان
    w = w - learning_rate * dw
    b = b - learning_rate * db
    if i % 10 == 0:
        print(f"Epoch {i}: w = {w:.3f}, b = {b:.3f}")
print(f"\nFinal Result: y = {w:.2f}x + {b:.2f}")

#تمرین
        # داده ها
x = np.array([1,2,3,4,5])
y = np.array([2,4,6,8,10])
        # پارامترهای اولیه
w = 0
b = 0
learning_rate = 0.01
epochs = 20
for i in range(epochs):
    y_pred = w*x + b
    dw = (-2/len(x)) * np.sum(x*(y - y_pred))
    db = (-2/len(x)) * np.sum(y - y_pred)
    w = w - learning_rate*dw
    b = b - learning_rate*db
    print(i, w, b)

#تمرین 2
x = np.array([1,2,3,4,5])
y = np.array([1,7,4,12,6])
w = 0
b = 0
learning_rate = 0.01
epochs = 200
for i in range(epochs):
    y_pred = w*x + b
    dw = (-2/len(x)) * np.sum(x*(y - y_pred))
    db = (-2/len(x)) * np.sum(y - y_pred)
    w = w - learning_rate*dw
    b = b - learning_rate*db
print("w =", w)
print("b =", b)
        # پیش بینی جدید
print("prediction for x=6 :", w*6 + b)
        # رسم نمودار
plt.scatter(x, y, color="blue")
plt.plot(x, y_pred, color="red")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Regression")

plt.show()


#ساده‌ترین رگرسیون خطی با sklearn
import numpy as np
from sklearn.linear_model import LinearRegression
                # داده ها
x = np.array([1,2,3,4,5]).reshape(-1,1)
y = np.array([2,4,6,8,10])
                # ساخت مدل
model = LinearRegression()
                # آموزش مدل
model.fit(x, y)
                # پارامترهای یادگرفته شده
print("w =", model.coef_)
print("b =", model.intercept_)
                # پیش بینی
prediction = model.predict([[6]])
print("prediction for x=6:", prediction)

# ارزیابی مدل (Model Evaluation)
from sklearn.metrics import mean_squared_error, r2_score
                # فرض کنیم y_true مقادیر واقعی و y_pred پیش‌بینی‌های مدل تو هستند
y_true = [10,20,30,40]
y_pred = [12,18,33,38]
                # محاسبه MSE
mse = mean_squared_error(y_true, y_pred)
                # محاسبه R2
r2 = r2_score(y_true, y_pred)

print(f"MSE: {mse}")
print(f"R2 Score: {r2}")

#تمرین
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

                # ۱. داده‌های معمولی (۱۰ بازی اول رئال)
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
y = np.array([1, 1, 2, 1, 2, 1, 1, 2, 1, 1]) # میانگین گل‌ها حول ۱ و ۲

                # ۲. اضافه کردن یک بازی "عجیب" (Outlier) - بازی شماره ۱۱ که ۵ گل زده!
X_with_outlier = np.append(X, [[11]], axis=0)
y_with_outlier = np.append(y, [5])

                # مدل الف: با داده‌های عادی
model_normal = LinearRegression().fit(X, y)
                # مدل ب: با داده‌ی پرت (۵ گل)
model_outlier = LinearRegression().fit(X_with_outlier, y_with_outlier)

                # مقایسه پیش‌بینی‌ها
print(f"R2 مدل عادی: {r2_score(y, model_normal.predict(X)):.3f}")
print(f"R2 مدل با داده پرت: {r2_score(y_with_outlier, model_outlier.predict(X_with_outlier)):.3f}")

                # رسم نمودار برای دیدنِ انحرافِ خط
plt.scatter(X_with_outlier, y_with_outlier, color='red', label='Data')
plt.plot(X_with_outlier, model_outlier.predict(X_with_outlier), color='blue', label='Model with Outlier')
plt.legend()
plt.title("تأثیر داده پرت روی خط مدل")
plt.show()

#تمرین
possession = np.array([55, 60, 45, 70, 50]).reshape(-1, 1)
goals = np.array([1,1,1,1,1])

model = LinearRegression()

model.fit(possession, goals)

predictions = model.predict(possession)

mse = mean_squared_error(goals, predictions)

print(f"میانگین مربعات خطا (MSE) الان برابر است با: {mse:.2f}")



#پروژه 1
                # ۱. ساخت ماتریس ۳ در ۲ (۳ نقطه در فضای ۲ بعدی یا بالعکس)
x = np.array([
    [10, 20],
    [30, 40],
    [50, 60]
])

                # ۲. ساخت ماتریس ۲ در ۲ برای بزرگ‌نمایی (Scalar Matrix)
                # این ماتریس همون Identity ضربدر ۲ هست: [[2, 0], [0, 2]]
scaling_matrix = np.eye(2) * 2

                # ضرب ماتریسی: (3x2) @ (2x2) حاصل یک ماتریس (3x2) خواهد بود
A = x @ scaling_matrix

                # ۳. ترانهاده کردن حاصل (حاصل یک ماتریس 2x3 می‌شود)
AT = A.T

print("Matrix A (Scaled):\n", A)
print("\nMatrix AT (Transposed):\n", AT)


# تمرین Gradient Descent
#پروژه2 
X= np. array ([1,2,3])
y= np. array([2,4,6])
w=0.0
lr=1.0
epochs=10

for i in range(epochs):
    y_pred= w*X
    error = y - y_pred 
    dw = -2 * np.mean(X * error) 
    w = w - (lr * dw)
    print(f"مرحله {i+1}: وزن = {w:.2f}")


#پروژه 3
x = np.array([7,10,3,8,5]).reshape(-1,1)
y = np.array([2,3,0,2,1])

model = LinearRegression()

model.fit(x, y)
               
print("w =", model.coef_)
print("b =", model.intercept_)

y_pred = model.predict(x)
mse = mean_squared_error(y,y_pred)

prediction = model.predict([[12]])
print("prediction for x=12:", prediction)
print(f"میانگین مربعات خطا (MSE) الان برابر است با: {mse:.2f}")





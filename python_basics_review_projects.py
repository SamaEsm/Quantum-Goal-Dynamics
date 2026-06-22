# =========================================
#Project 1: Cafe Invoice System 
# =========================================
print("خوش اومدید به کافه کتاب لیمو")
        #دریاقت اطلاعات مشتری
customer_name=str(input("نام مشتری چیست؟"))
cashier_name=str(input("نام صندوق دار چیه"))
        #دریافت اطلاعات سفارش
drink_name =str(input("چه نوشیدنی ای میل دارید"))
drink_count=int(input("چه تعداد؟"))
drink_total = drink_count * 150

cake_name=str(input("چه کیکی میل دارید؟"))
cake_count=int(input("چه تعداد؟"))
cake_total = cake_count * 200

        #محاسبات
subtotal = drink_total + cake_total
tax = subtotal * 0.09
discount_percent = int(input("چند درصد تخفیف دارید؟ "))
discount_amount = (subtotal + tax) * (discount_percent / 100)
final_price = (subtotal + tax) - discount_amount

        #چاپ فاکتور
print("\n--- فاکتور نهایی ---")
print(f"مشتری: {customer_name} | صندوق‌دار: {cashier_name}")
print(f"مجموع قیمت {drink_name}: {drink_total}")
print(f"مجموع قیمت {cake_name}: {cake_total}")
print(f"مالیات (9%): {tax:.2f}")
print(f"مبلغ تخفیف: {discount_amount:.2f}")
print(f"مبلغ قابل پرداخت: {final_price:.2f}")


# =========================================
# Project 2: Gym Membership Calculator
# =========================================
name= input("نام و نام خانوادگی")
age= float(input("سن؟"))
base_price = 1000000
discount = 0 
extra_charge = 0 
has_private_coach = "خیر"
if age < 18:
    discount = base_price * 0.2 
elif age > 60:
    discount = base_price * 0.3  
underlying_disease = input("آیا بیماری خاصی دارید؟ (yes/no): ").strip().lower()

if underlying_disease == "yes":
    extra_charge = 500000
    has_private_coach = "بله (اجباری به دلیل شرایط سلامت)"
final_price = base_price - discount + extra_charge
print("\n" + "="*40)
print(f"  فاکتور عضویت باشگاه برای: {name}")
print("="*40)
print(f"قیمت پایه باشگاه:  {base_price:,} تومان")
print(f"تخفیف اعمال شده:   {discount:,} تومان")
print(f"نیاز به مربی خصوصی: {has_private_coach}")
print(f"هزینه مربی خصوصی:   {extra_charge:,} تومان")
print("-" * 40)
print(f"مبلغ نهایی قابل پرداخت: {final_price:,} تومان")
print("="*40)


# =========================================
# Project 3: Number Guessing Game
# =========================================
import random
secret_number = random.randint(1, 100)
attempts = 0
print("🎮 بازی حدس عدد شروع شد!")
print("یک عدد بین 1 تا 100 حدس بزن")
while True:
    guess = int(input("حدس تو: "))
    attempts += 1
    if guess > secret_number:
        print("عدد کوچکتر است")
    elif guess < secret_number:
        print("عدد بزرگتر است")
    else:
        print("🎉 درست حدس زدی!")
        print(f"تعداد تلاش‌ها: {attempts}")
        break



# =========================================
# Project 4: Shopping List Manager
# =========================================
shopping_list=[]
print("سیستم لیست خرید ")
print("برای خروج بنویسexit")
while True:
    item=input("چه چیزی بیاید بخریم؟").strip()
    if item.lower() == "exit":
        break
    shopping_list.append(item)
    print("به لیست اضافه شد ✅")
print("\nلیست خرید شما:")
for i, item in enumerate(shopping_list, start=1):
    print(f"{i}- {item}")
print(f"\nتعداد کل اقلام: {len(shopping_list)}")








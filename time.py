# ===========================================================
# 📊 Microsoft Stock Data Analysis Project
# -----------------------------------------------------------
# This project performs exploratory data analysis on Microsoft 
# stock historical data using pandas and matplotlib. It includes:
# - Data preprocessing (datetime conversion)
# - Statistical summaries
# - Day-of-week extraction
# - Date range filtering
# - Visualization of stock trends
# - Monthly resampling and aggregation
# Perfect for financial data insight and time-series visualization.
# ===========================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# قراءة البيانات من ملف CSV
data = pd.read_csv('Microsoft_Stock.csv')

# تحويل عمود التاريخ من نص إلى datetime object
data["Date"] = pd.to_datetime(data["Date"], format="%m/%d/%Y %H:%M:%S")

# عرض أول 5 صفوف من البيانات
print(data.head())

# عرض معلومات عامة عن الأعمدة ونوع البيانات
print(data.info())

# عرض إحصائيات وصفية للبيانات
print(data.describe())

# إضافة عمود يحتوي على اسم يوم الأسبوع لكل تاريخ
data["days of week"] = data["Date"].dt.day_name()
print(data)

# استخراج اسم اليوم لأول صف في البيانات
day = data.loc[0, "Date"].day_name()
print(day)

# طباعة أقدم تاريخ في البيانات
print(data["Date"].min())

# طباعة أحدث تاريخ في البيانات
print(data["Date"].max())

# حساب الفترة الزمنية بين أقدم وأحدث تاريخ
print(data["Date"].max() - data["Date"].min())

# عرض الصفوف التي بعد سنة 2020
print(data[data["Date"] > "2020"])

# تعيين عمود "Date" كمؤشر (index) للبيانات
data.set_index("Date", inplace=True)
print(data)

# استخراج البيانات الخاصة بسنة 2020 فقط
data1 = data.loc["2020"]
print(data1)

# استخراج البيانات من يونيو 2020 إلى سبتمبر 2021
data2 = data.loc["2020-06":"2021-09"]
print(data2)

# رسم إغلاق السهم خلال مارس 2020
plt.plot(data.loc["2020-03"]["Close"])
plt.title("Microsoft Stock Close Price - March 2020")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.grid(True)
plt.show()

# رسم إغلاق السهم خلال عام 2020
print(data.loc["2020"]["Close"].plot(title="Microsoft Close Price - 2020"))
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.grid(True)
plt.show()

# إعادة تجميع البيانات شهريًا وحساب متوسط السعر الأعلى
print(data["High"].resample('M').mean())

# إعادة تجميع شهرية وإجراء إحصاءات مختلفة على الأعمدة
print(data.resample("M").agg({
    "Open": "mean",
    "High": "sum",
    "Low": "min",
    "Volume": "max",
    "Close": "mean"
}))








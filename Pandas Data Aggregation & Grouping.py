import pandas as pd

data = {
    'Region': ['North', 'South', 'North', 'East', 'South', 'North'],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C'],
    'Sales': [100, 150, 120, 200, 180, 250],
    'Quantity': [10, 15, 12, 20, 18, 25]
}
df_sales = pd.DataFrame(data)
print("--- DataFrame ยอดขายเริ่มต้น ---")
print(df_sales)

# 🚀 ตัวอย่าง 1: ยอดขายรวมของแต่ละ Region
# จัดกลุ่มด้วย 'Region' แล้วหาผลรวมของคอลัมน์ตัวเลข
region_sales_sum = df_sales.groupby('Region').sum()
print("\n--- ยอดขายรวมของแต่ละ Region (Sum) ---")
print(region_sales_sum)
# สังเกตว่า 'Product' คอลัมน์ String จะหายไปโดยอัตโนมัติ

# 🚀 ตัวอย่าง 2: จำนวนรายการขายในแต่ละ Region
region_sales_count = df_sales.groupby('Region').count()
print("\n--- จำนวนรายการขายของแต่ละ Region (Count) ---")
print(region_sales_count)

# 🚀 ตัวอย่าง 3: ยอดขายเฉลี่ยและปริมาณเฉลี่ยของแต่ละ Product
product_avg = df_sales.groupby('Product')[['Sales', 'Quantity']].mean()
print("\n--- ยอดขายเฉลี่ยและปริมาณเฉลี่ยของแต่ละ Product (Mean) ---")
print(product_avg)

# 🚀 ตัวอย่าง 4: จัดกลุ่มด้วยหลายคอลัมน์ (Region และ Product)
# แล้วหาผลรวมของ Sales
multi_group_sum = df_sales.groupby(['Region', 'Product'])['Sales'].sum()
print("\n--- ยอดขายรวมตาม Region และ Product (Sum of Sales) ---")
print(multi_group_sum)
# ผลลัพธ์จะเป็น Series ที่มี MultiIndex (ดัชนีซ้อนกัน)

# ถ้าต้องการให้ผลลัพธ์กลับมาเป็น DataFrame ปกติ
multi_group_sum_df = df_sales.groupby(['Region', 'Product'])['Sales'].sum().reset_index()
print("\n--- ยอดขายรวมตาม Region และ Product (Sum of Sales - เป็น DataFrame) ---")
print(multi_group_sum_df)

# ใช้ df_sales ตัวเดิม
# ต้องการหายอดรวม, ยอดเฉลี่ย, และจำนวนของ Sales ในแต่ละ Region
region_multi_agg = df_sales.groupby('Region').agg(
    Sales_Total=('Sales', 'sum'), # ตั้งชื่อคอลัมน์ใหม่
    Sales_Average=('Sales', 'mean'),
    Sales_Count=('Sales', 'count'),
    Quantity_Total=('Quantity', 'sum') # สามารถรวมคอลัมน์อื่นได้ด้วย
)
print("\n--- การรวมข้อมูลหลายฟังก์ชันด้วย .agg() ---")
print(region_multi_agg)
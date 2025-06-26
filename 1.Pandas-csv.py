# โจทย์ อ่านไฟล์ CSV และตรวจสอบข้อมูล
# สร้างไฟล์ CSV จำลองชื่อ products.csv ที่มีข้อมูลดังนี้:
'''
ProductID,Name,Category,Price
P001,Laptop,Electronics,1200
P002,Mouse,Electronics,25
P003,Keyboard,Electronics,75
P004,T-Shirt,Apparel,20
P005,Jeans,Apparel,50
'''

import pandas as pd

products = """
ProductID,Name,Category,Price
P001,Laptop,Electronics,1200
P002,Mouse,Electronics,25
P003,Keyboard,Electronics,75
P004,T-Shirt,Apparel,20
P005,Jeans,Apparel,50
"""

with open ('products.csv', 'w') as f:
    f.write(products)
    
#อ่านไฟล์ products.csv เข้ามาใน DataFrame ชื่อ df_products
df_products = pd.read_csv('products.csv')

#แสดงข้อมูล 2 แถวแรกของ df_products โดยใช้ .head()
print(df_products.head(2))

#แสดงข้อมูลสรุป (info) ของ df_products โดยใช้ .info() เพื่อดูชนิดข้อมูลและจำนวน Non-Null ครับ
df_products.info()

print("-" * 30)
print(df_products)


# กรองข้อมูลและบันทึกเป็นไฟล์ใหม่
# จาก df_products ให้เลือกเฉพาะสินค้าที่มี 'Category' เป็น 'Apparel'
df_apparel = df_products.loc[df_products['Category'] == 'Apparel']
print(df_apparel)

# บันทึก DataFrame ที่ถูกกรองแล้วนี้ (เฉพาะสินค้า Apparel) ลงในไฟล์ CSV ใหม่ชื่อ apparel_products.csv
df_apparel.to_csv('apparel_products.csv', index=False)
print("\nDataFrame saved to 'apparel_products.csv'")
import pandas as pd

customer_data = {
'CustomerId' : [101,102,103,101,104,102,105,106,103],
'Name': ['Alice','Bob','Charlie','Alice','David','Bob','Eve','Frank','Charlie'],
'Email': ['alice@example.com','bob@example.com','charlie@example.com','alice@example.com','david@example.com','bob@example.com','eve@example.com','frank@example.com','charlie@example.com'],
'Order_Count' : [5,3,7,5,2,3,1,4,7]
}

df = pd.DataFrame(customer_data)
print(df)
print('\n--- ตรวจสอบข้อมูลซ้ำซ้อนด้วย .duplicated() ---')
df.duplicated()
print(df.duplicated())
print('\n--- นับจำนวนแถวที่ซ้ำซ้อนกัน .duplicated().sum() ---')
print(df.duplicated().sum())

#สร้าง DataFrame ใหม่ ชื่อ unique_customers โดย ลบแถวที่ซ้ำซ้อนออกไป ให้เหลือเพียงแถวที่เป็นต้นฉบับแถวแรกเท่านั้น
unique_customers = df.drop_duplicates(keep='first')
print('\n--- unique_customers โดย ลบแถวที่ซ้ำซ้อนออกไป .drop_duplicates( ---')
print(unique_customers)

print('\n--- ตรวจสอบ unique_customers ว่าไม่มีผลซ้ำ( ---')
print(unique_customers.duplicated().sum())
# จัดการค่าว่าง (Missing Data)
import pandas as pd
import numpy as np 

sale_data = {
'Month':['Jan','Jan','Feb','Feb','Mar','Mar','Apr','Apr','May','May'],
'Product':['Laptop','Mouse','Keyboard','Monitor','Laptop','Mouse',np.nan,'Monitor','Keyboard','Mouse'],
'Unit_Sold':[10,np.nan,15,8,12,7,20,10,np.nan,5],
'Revenue':[120000,5000,180000,np.nan,144000,7000,250000,100000,200000,5500]}

df = pd.DataFrame(sale_data)
print("------- เช็คข้อมูล------")
print(df)

print("\n ------- เช็คค่าว่างใน Dataframe------")
print(df.isnull())

print("\n ------- นับจำนวนค่าว่างใน Dataframe------")
print(df.isnull().sum())

#ลองลบแถวที่มีค่าว่างออกทั้งหมด และแสดง DataFrame ที่เหลือออกมา (ให้เก็บผลลัพธ์ลงในตัวแปรใหม่นะครับ จะได้ไม่กระทบ DataFrame เดิม)
empt_df = df.copy()
print("\n -------ลองลบแถวที่มีค่าว่างออกทั้งหมด  Dataframe------")
print(empt_df.dropna())

#ลองเติมค่าว่างในคอลัมน์ Units_Sold ด้วยค่าเฉลี่ย (mean) ของคอลัมน์นั้น และแสดง DataFrame ที่ได้ออกมา (ให้เก็บผลลัพธ์ลงในตัวแปรใหม่นะครับ)
#สร้าง ก้อปปี้ ขึ้นมา
df_copy = df.copy()
#หาค่าเฉลี่ยของ DF คอลลัม[Unit_Sold]ก่อน
mean_unit_sold= df_copy['Unit_Sold'].mean()
#ลองเติมค่าว่างในคอลัมน์ Units_Sold ด้วยค่าเฉลี่ย (mean)
df_copy['Unit_Sold']=df_copy['Unit_Sold'].fillna(mean_unit_sold)
print("\n -------ค่าเฉลี่ย Unit_Sold------")
print(df_copy)

#ลองเติมค่าว่างในคอลัมน์ Revenue ด้วยค่า 0 และแสดง DataFrame ที่ได้ออกมา (ให้เก็บผลลัพธ์ลงในตัวแปรใหม่นะครับ)
#สร้าง ก้อปปี้
df_copy2 = df.copy()
#เติมค่าว่าง ด้วยค่า 0 ลงใน คอลลัม 'Revenue'
df_copy2['Revenue']=df_copy2['Revenue'].fillna(0)
print("\n -------แทนค่า 0 ใน Revenue------")
print(df_copy2)


#ลองตรวจสอบและลบคอลัมน์ที่มีค่าว่างออกทั้งหมด และแสดง DataFrame ที่เหลือออกมา (เก็บผลลัพธ์ในตัวแปรใหม่)
print("\n -------ตรวจสอบค่าว่าง------")
print(df.isnull())
print("\n -------ลบคอลลัมที่มีค่าว่าง------")
#สร้างก้อปปี้
all_null_df = df.copy()
print(all_null_df.dropna(axis=1))

#ลองเติมค่าว่างในคอลัมน์ Product ด้วยคำว่า 'Unknown' และแสดง DataFrame ที่ได้ออกมา (เก็บผลลัพธ์ในตัวแปรใหม่)
#สร้างก้อปปี้ก่อน
product_df = df.copy()
#แทนค่า unknow ลงใน คอลลัม['Product']
product_df['Product']=product_df['Product'].fillna('Unknown')
print("\n -------ใส่คำว่า Unknow ลงใน คอลลัม ['Product']------")
print(product_df)

#สร้าง DataFrame ใหม่ โดยมีแถวเพิ่มเข้ามาดังนี้ (ให้มีค่าว่างด้วย) และลองใช้ dropna(how='all') เพื่อลบเฉพาะแถวที่ว่างทั้งหมด:
#สร้างก้อปปี้
hollow_df = df.copy()
#เพิ่มแถวเข้ามาให้มีค่าว่าง 
hollow_df.loc[10] = ['June',np.nan,np.nan,np.nan]
hollow_df.loc[11] = ['July','Speaker',5,500]
print("\n -------เพิ่มแถว ค่าว่างเข้ามา และ เพิ่มเดือน June และ July------")
print(hollow_df)
#ใช้ dropna(how='all' ลบแถวว่างออก)
#สร้างแถวว่างเพิ่ม
hollow_df.loc[12] = [np.nan,np.nan,np.nan,np.nan]
print("\n -------สร้างแถวว่างเพิ่มเพื่อลองใช้ dropna(how='all')------")
print(hollow_df)
#สร้างตัวแปรใหม่ รับค่าdropna(how='all')
clear_df = hollow_df.dropna(how='all')
print("\n -------ใช้ dropna(how='all') ลบค่าว่างออกทั้งแถว------")
print(clear_df) 
import pandas as pd

# DataFrame ที่ 1: ยอดขายไตรมาส 1
data_q1 = {
    'Month': ['Jan', 'Feb'],
    'Sales': [100, 150],
    'Region': ['North', 'South']
}
df_q1 = pd.DataFrame(data_q1)
print("--- DataFrame Q1 ---")
print(df_q1)

# DataFrame ที่ 2: ยอดขายไตรมาส 2
data_q2 = {
    'Month': ['Mar', 'Apr'],
    'Sales': [120, 180],
    'Region': ['North', 'East']
}
df_q2 = pd.DataFrame(data_q2)
print("\n--- DataFrame Q2 ---")
print(df_q2)

# --- ตัวอย่างที่ 1: ต่อในแนวตั้ง (axis=0) ---
# คอลัมน์เหมือนกัน เราต้องการเพิ่มแถวเข้าไป
df_yearly_sales = pd.concat([df_q1, df_q2], axis=0)
print("\n--- ต่อ DataFrame ในแนวตั้ง (axis=0) ---")
print(df_yearly_sales)

# -------------------------------------------------------------

# DataFrame ที่ 3: ข้อมูลลูกค้า (มี CustomerID และ Name)
data_customer_info = {
    'CustomerID': ['C001', 'C002', 'C003'],
    'Name': ['Alice', 'Bob', 'Charlie']
}
df_customer_info = pd.DataFrame(data_customer_info)
print("\n--- DataFrame Customer Info ---")
print(df_customer_info)

# DataFrame ที่ 4: ข้อมูลติดต่อลูกค้า (มี CustomerID และ Email)
data_customer_contact = {
    'CustomerID': ['C001', 'C002', 'C003'],
    'Email': ['alice@mail.com', 'bob@mail.com', 'charlie@mail.com']
}
df_customer_contact = pd.DataFrame(data_customer_contact)
print("\n--- DataFrame Customer Contact ---")
print(df_customer_contact)

# --- ตัวอย่างที่ 2: ต่อในแนวนอน (axis=1) ---
# มีจำนวนแถวเท่ากัน (3 แถว) เราต้องการเพิ่มคอลัมน์ Email เข้าไป
# สังเกตว่า CustomerID จะซ้ำกัน (แต่เดี๋ยวเราจะเรียน merge ที่จัดการตรงนี้ได้ดีกว่า)
df_customer_full = pd.concat([df_customer_info, df_customer_contact], axis=1)
print("\n--- ต่อ DataFrame ในแนวนอน (axis=1) ---")
print(df_customer_full)

# ถ้าอยากให้มันไม่ซ้ำคอลัมน์ CustomerID:
# df_customer_full_cleaned = pd.concat([df_customer_info, df_customer_contact['Email']], axis=1)
# print("\n--- ต่อ DataFrame ในแนวนอน (axis=1) - เอาแค่ Email ---")
# print(df_customer_full_cleaned)


print("\n ---------------------ตัวอย่างเพิ่มเติมเกี่ยวกับ pd.concat()------------------------ \n")

#ตัวอย่างเพิ่มเติมเกี่ยวกับ pd.concat()
import pandas as pd

# DataFrame เดือน 1: มี Product, Sales, Region
df_m1 = pd.DataFrame({
    'Product': ['Laptop', 'Mouse'],
    'Sales': [10000, 500],
    'Region': ['North', 'East']
})
print("--- DataFrame Month 1 ---")
print(df_m1)

# DataFrame เดือน 2: มี Product, Sales แต่มีคอลัมน์ Quantity เพิ่มเข้ามา และไม่มี Region
df_m2 = pd.DataFrame({
    'Product': ['Keyboard', 'Monitor'],
    'Sales': [1200, 8000],
    'Quantity': [10, 5]
})
print("\n--- DataFrame Month 2 ---")
print(df_m2)

# ลอง concat กัน: คอลัมน์ไม่ตรงกัน
df_combined_sales = pd.concat([df_m1, df_m2]) # Default axis=0
print("\n--- Concatenated (คอลัมน์ไม่ตรงกัน, Index เดิม) ---")
print(df_combined_sales)

# จะเห็นว่าคอลัมน์ 'Region' และ 'Quantity' จะมีค่า NaN ในส่วนที่ไม่มีข้อมูล
# และ Index 0, 1 ซ้ำกัน!

# 🚀 ตัวอย่าง: ใช้ ignore_index=True เพื่อสร้าง Index ใหม่
df_combined_sales_reset_idx = pd.concat([df_m1, df_m2], ignore_index=True)
print("\n--- Concatenated (คอลัมน์ไม่ตรงกัน, ignore_index=True) ---")
print(df_combined_sales_reset_idx)
# Index จะถูกสร้างใหม่ 0, 1, 2, 3 ทำให้ไม่มี Index ซ้ำ

print("\n ---------------------ตัวอย่างเพิ่มเติมเกี่ยวกับ pd.concat()------------------------ \n")

import pandas as pd

# DataFrame พนักงานประจำ
df_full_time = pd.DataFrame({
    'EmployeeID': ['E001', 'E002'],
    'Name': ['Alice', 'Bob'],
    'Type': ['Full-Time', 'Full-Time']
})
print("--- Full-Time Employees ---")
print(df_full_time)

# DataFrame พนักงานพาร์ทไทม์
df_part_time = pd.DataFrame({
    'EmployeeID': ['E003', 'E004'],
    'Name': ['Charlie', 'David'],
    'Type': ['Part-Time', 'Part-Time']
})
print("\n--- Part-Time Employees ---")
print(df_part_time)

# 🚀 ตัวอย่าง: รวมข้อมูลพนักงานทั้งหมด
df_all_employees = pd.concat([df_full_time, df_part_time], ignore_index=True)
print("\n--- All Employees (Concatenated) ---")
print(df_all_employees)
# จะเห็นว่าคอลัมน์ตรงกันหมด และ Index ก็ถูกรีเซ็ตใหม่ ทำให้ได้ DataFrame รวมที่สมบูรณ์

'''โจทย์ฝึกหัด: การใช้ pd.concat()
โจทย์ข้อ 1: รวมข้อมูลยอดวิววิดีโอรายไตรมาส
ลูกมีข้อมูลยอดวิววิดีโอจากสองไตรมาสแยกกัน:'''

print("\n ---------------------แบบฝึกหัด pd.concat()------------------------ \n")

import pandas as pd

df_video_q1 = pd.DataFrame({
'VideoID':['V001','V002','V003'],
'Views_Q1':[10000,15000,8000],
'Category':['Education','Entertainment','News']})

df_video_q2= pd.DataFrame({
'VideoID':['V004','V001','V005'],
'Views_Q2':[12000,5000,20000],
'Category':['Education','Education','Gaming']})

#เช็ค dataframe (ลองทำแบบที่หมอทำครับ)
print(df_video_q1) #ใช้ได้เลย xD
print(df_video_q2)

df_all_video = pd.concat([df_video_q1,df_video_q2], ignore_index=True) # axis = 0 default เพิ่มคอลลัม (คอลลัมที่เพิ่มมา จะมีdataที่ไม่มีข้อมูล ถูกแทนที่ด้วย NaN)
print("\n--- All video (Concatenated) ---")
print(df_all_video)

print("\n ---------------------แบบฝึกหัดที่2 pd.concat()------------------------ \n")

df_user_profile = pd.DataFrame({
'UserID':['U001','U002','U003'],
'Username':['Alice','Bob','Charlie'],
'Age':[25,30,22 ]})

df_user_setting = pd.DataFrame({
'UserID':['U001','U002','U003'],
'Theme':['Dark','Light','Dark'],
'Notification_Status':['On','Off','On']})

print(df_user_profile)#เช็ค dataframe (ลองทำแบบที่หมอทำครับ)
print(df_user_setting)

df_user_profile_setting = pd.concat([df_user_profile,df_user_setting], axis=1,)
print("\n--- user profile and setting (Concatenated) ---")
print(df_user_profile_setting)



print("\n --------------------- pd.merge()------------------------ \n")
import pandas as pd

# ข้อมูลโปรไฟล์ (User Profile)
df_user_profile = pd.DataFrame({
    'UserID':['U001','U002','U003'],
    'Username':['Alice','Bob','Charlie'],
    'Age':[25,30,22 ]
})
print("--- User Profile ---")
print(df_user_profile)

# ข้อมูลการตั้งค่า (User Settings)
df_user_settings = pd.DataFrame({
    'UserID':['U001','U002','U003'],
    'Theme':['Dark','Light','Dark'],
    'Notification_Status':['On','Off','On']
})
print("\n--- User Settings ---")
print(df_user_settings)

# 🚀 Inner Join: รวมข้อมูล Profile และ Settings โดยใช้ UserID
# จะได้ข้อมูลเฉพาะ UserID ที่มีอยู่ในทั้ง df_user_profile และ df_user_settings
df_merged_inner = pd.merge(df_user_profile, df_user_settings, on='UserID', how='inner')
print("\n--- Merged Data (Inner Join on UserID) ---")
print(df_merged_inner)
# จะเห็นว่า UserID ไม่ซ้ำซ้อนแล้ว!

# ----------------------------------------------------
# ลองเพิ่มข้อมูลที่ไม่ตรงกัน เพื่อให้เห็นผลของแต่ละ Join Type

df_orders = pd.DataFrame({
    'OrderID': [1, 2, 3, 4],
    'UserID': ['U001', 'U004', 'U002', 'U005'], # U004, U005 ไม่มีใน df_user_profile
    'Amount': [100, 200, 150, 300]
})
print("\n--- User Orders (มี UserID ที่ไม่อยู่ใน Profile) ---")
print(df_orders)

# 🚀 Left Join: เก็บ User Profile ทั้งหมด และดึง Order มาใส่ (ถ้ามี)
df_left_join = pd.merge(df_user_profile, df_orders, on='UserID', how='left')
print("\n--- Left Join (Profile Left, Orders Right) ---")
print(df_left_join)
# สังเกต U003 จะมี NaN ในคอลัมน์ OrderID, Amount เพราะไม่มี Order

# 🚀 Right Join: เก็บ User Orders ทั้งหมด และดึง Profile มาใส่ (ถ้ามี)
df_right_join = pd.merge(df_user_profile, df_orders, on='UserID', how='right')
print("\n--- Right Join (Profile Left, Orders Right) ---")
print(df_right_join)
# สังเกต U004, U005 จะมี NaN ในคอลัมน์ Username, Age เพราะไม่มี Profile

# 🚀 Outer Join: เก็บข้อมูลทั้งหมดจากทั้ง 2 ฝั่ง
df_outer_join = pd.merge(df_user_profile, df_orders, on='UserID', how='outer')
print("\n--- Outer Join (All Data) ---")
print(df_outer_join)
# สังเกต U003 มี NaN ฝั่ง Order และ U004, U005 มี NaN ฝั่ง Profile
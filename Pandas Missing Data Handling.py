import pandas as pd
import numpy as np # เราจะใช้ np.nan แทนค่าว่าง

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, np.nan, 22, 35, np.nan], # Bob กับ Eve ไม่มีข้อมูลอายุ
    'City': ['New York', 'London', np.nan, 'Paris', 'Tokyo'], # Charlie ไม่มีข้อมูลเมือง
    'Score': [85, 90, 78, np.nan, 92] # David ไม่มีข้อมูลคะแนน
}
df = pd.DataFrame(data)

print("--- DataFrame เริ่มต้นที่มีค่าว่าง ---")
print(df)

print("\n--- ตรวจสอบค่าว่างด้วย .isnull() ---")
print(df.isnull())

print("\n--- ตรวจสอบว่าไม่ใช่ค่าว่างด้วย .notnull() ---")
print(df.notnull())

# ใช้ df ตัวเดิมจากตัวอย่างข้างบน
print("\n--- จำนวนค่าว่างในแต่ละคอลัมน์ ---")
print(df.isnull().sum())
# Output:
# Name     0  (ไม่มีค่าว่าง)
# Age      2  (Bob, Eve)
# City     1  (Charlie)
# Score    1  (David)
# dtype: int64

# ถ้าอยากรู้อัตราส่วนค่าว่าง (เปอร์เซ็นต์)
total_rows = len(df)
print("\n--- เปอร์เซ็นต์ค่าว่างในแต่ละคอลัมน์ ---")
print((df.isnull().sum() / total_rows) * 100)

# ใช้ df ตัวเดิมจากข้างบน
print("\n--- DataFrame หลังใช้ .dropna() (ลบทุกแถวที่มีค่าว่าง) ---")
df_dropped = df.dropna()
print(df_dropped)
# Output จะเหลือแค่แถวของ Alice (เพราะแถวอื่นมีค่าว่าง)

print("\n--- DataFrame หลังใช้ .dropna(how='all') (ลบเฉพาะแถวที่ว่างทั้งแถว) ---")
df_all_null = df.copy() # สร้างสำเนาเพื่อไม่ให้ df เดิมเปลี่ยน
df_all_null.loc[5] = [np.nan, np.nan, np.nan, np.nan] # เพิ่มแถวที่ว่างเปล่าทั้งแถว
df_all_null_dropped = df_all_null.dropna(how='all')
print(df_all_null_dropped) # แถวที่ 5 จะถูกลบไป

print("\n--- DataFrame หลังใช้ .dropna(subset=['Age']) (ลบเฉพาะแถวที่ Age เป็นค่าว่าง) ---")
df_dropped_age = df.dropna(subset=['Age'])
print(df_dropped_age) # แถวของ Bob และ Eve จะถูกลบไป


# ใช้ df ตัวเดิมจากข้างบน
print("\n--- DataFrame หลังใช้ .fillna(0) (เติมค่าว่างด้วย 0) ---")
df_filled_zero = df.fillna(0)
print(df_filled_zero)

print("\n--- DataFrame หลังใช้ .fillna(method='ffill') (เติมค่าว่างด้วยค่าก่อนหน้า) ---")
df_filled_ffill = df.fillna(method='ffill')
print(df_filled_ffill)
# สังเกต: Bob จะได้อายุของ Alice, Charlie จะได้เมืองของ Bob (ถ้ามี)

print("\n--- DataFrame หลังใช้ .fillna(ค่าเฉลี่ยของ Age) ---")
# คำนวณค่าเฉลี่ยของคอลัมน์ 'Age' ก่อน
mean_age = df['Age'].mean()
df_filled_mean_age = df.copy() # สร้างสำเนาเพื่อไม่ให้ df เดิมเปลี่ยน
df_filled_mean_age['Age'] = df_filled_mean_age['Age'].fillna(mean_age)
print(df_filled_mean_age)

print("\n--- DataFrame หลังใช้ .fillna(ค่า Mode ของ City) ---")
# คำนวณค่าฐานนิยม (Mode) ของคอลัมน์ 'City'
# .mode()[0] เพราะ mode อาจมีหลายค่า เราเอาค่าแรก
mode_city = df['City'].mode()[0]
df_filled_mode_city = df.copy()
df_filled_mode_city['City'] = df_filled_mode_city['City'].fillna(mode_city)
print(df_filled_mode_city)


print('\n'+"#" * 100 + '\n')

import pandas as pd

data = {
    'ID': [1, 2, 3, 2, 4, 1],
    'Name': ['Alice', 'Bob', 'Charlie', 'Bob', 'David', 'Alice'],
    'Score': [85, 90, 78, 90, 92, 85]
}
df = pd.DataFrame(data, index=['แถวที่ 0','แถวที่ 1','แถวที่ 2','แถวที่ 3','แถวที่ 4','แถวที่ 5'])

print("--- DataFrame เริ่มต้นที่มีข้อมูลซ้ำซ้อน ---")
print(df)

print("\n--- ตรวจสอบข้อมูลซ้ำซ้อนด้วย .duplicated() (ค่าเริ่มต้น: ตรวจสอบทุกคอลัมน์, เก็บตัวแรก) ---")
print(df.duplicated())
# Output:
# 0    False  (Alice, ID=1)
# 1    False  (Bob, ID=2)
# 2    False  (Charlie, ID=3)
# 3     True  (Bob, ID=2, Score=90 - ซ้ำกับแถวที่ 1)
# 4    False  (David, ID=4)
# 5     True  (Alice, ID=1, Score=85 - ซ้ำกับแถวที่ 0)
# dtype: bool

print("\n--- ตรวจสอบข้อมูลซ้ำซ้อนเฉพาะคอลัมน์ 'ID' ---")
print(df.duplicated(subset=['ID']))
# Output:
# 0    False
# 1    False
# 2    False
# 3     True  (ID=2 ซ้ำกับแถวที่ 1)
# 4    False
# 5     True  (ID=1 ซ้ำกับแถวที่ 0)
# dtype: bool

print("\n--- ตรวจสอบข้อมูลซ้ำซ้อนเฉพาะคอลัมน์ 'Name' และ 'Score' ---")
print(df.duplicated(subset=['Name', 'Score']))
# Output:
# 0    False
# 1    False
# 2    False
# 3     True  (Name='Bob', Score=90 ซ้ำกับแถวที่ 1)
# 4    False
# 5     True  (Name='Alice', Score=85 ซ้ำกับแถวที่ 0)
# dtype: bool

print("\n--- ตรวจสอบข้อมูลซ้ำซ้อน (ทำเครื่องหมาย True ทุกตัวที่เป็นซ้ำ) ---")
print(df.duplicated(keep=False))
# Output:
# 0     True  (Alice เป็นซ้ำ)
# 1     True  (Bob เป็นซ้ำ)
# 2    False
# 3     True  (Bob เป็นซ้ำ)
# 4    False
# 5     True  (Alice เป็นซ้ำ)
# dtype: bool
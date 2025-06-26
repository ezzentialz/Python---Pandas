import pandas as pd
import numpy as np

axis = {
'A': [1, 2, np.nan],
'B': [4, np.nan, 6],
'C': [7, 8, 9]
}

df_axis = pd.DataFrame(axis)
#เช็คข้อมูล dataframe
print("\n -----------------ต้นฉบับ--------------")
print(df_axis)
#สร้างก้อปปี้สำรอง
df_axis_copy1 = df_axis.copy()
#ลบคอลลัมค่าวางทั้งหมด จากแถว
df_axis_copy1.dropna(axis=1, how='all')
#output คือไม่มีอะไรเปลี่ยนเพราะไม่มีค่าว่าง 
print("\n -------------.dropna(axis=1, how='all')------------------")
print(df_axis_copy1)

#สร้างก้อปปี้ 2
df_axis_copy2 = df_axis.copy()
#เติมค่าว่าง โดยกำหนดให้ค่าว่าง เท่ากับ 0 โดยดูจากคอลลัมในแนวตั้ง
df_axis_copy2 = df_axis_copy2.fillna(0, axis=0)
print("\n -------------.fillna(0, axis=0)------------------")
print(df_axis_copy2)




import pandas as pd
import numpy as np

products = {
'ProductID': ['P001','P002','P003','P004','P005','P006'],
'ProductName': ['Laptop','Mouse','Keyboard','Monitor','Webcam','External HDD'],
'Price': [12000,500,1500,8000,800,3500]}
#สร้าง dataframe
df_products = pd.DataFrame(products)
#สร้าง คอลลัม'category' ให้ np.where price มากกว่า 5000 = high-end / ไม่งั้น np.where price มากกว่าเท่า 1000 = Midrange หากไม่ใช่อีกก็ lowend ละ
df_products['Category'] = np.where(df_products['Price'] > 5000, 'High-End', np.where(df_products['Price'] >= 1000, 'Mid-Range', 'Low-End'))
#ปริ๊น df_products
print(df_products)


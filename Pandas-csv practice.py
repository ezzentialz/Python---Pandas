##############################################################################################################################
#สร้างไฟล์ Excel จำลอง ชื่อ sales_data.xlsx ที่มีข้อมูล 2 ชีท (sheets) ดังนี้:
#Sheet 1: Q1_Sales 
'''
Product,Region,Sales_Amount
Laptop,North,12000
Mouse,South,500
Keyboard,East,1500
Monitor,North,8000
Desk,South,3000
'''
#Sheet 2: Q2_Sales
'''
Product,Region,Sales_Amount
Laptop,West,10000
Mouse,North,700
Keyboard,South,1800
Monitor,East,7500
Chair,West,2500
'''
#*** Hint: การสร้างไฟล์ Excel ในโค้ด เราจะสร้าง DataFrame สองอันก่อน แล้วใช้ pd.ExcelWriter() 
# เพื่อเขียน DataFrame ทั้งสองลงในชีทที่แตกต่างกันในไฟล์ Excel เดียวกันครับ

# ตัวอย่างการสร้างและบันทึก Excel ที่มีหลายชีท
# pip install openpyxl
# import pandas as pd
# df1 = pd.DataFrame({'col1': [1,2], 'col2': [3,4]})
# df2 = pd.DataFrame({'colA': [5,6], 'colB': [7,8]})
# with pd.ExcelWriter('multi_sheet.xlsx') as writer:
#     df1.to_excel(writer, sheet_name='Sheet_One', index=False)
#     df2.to_excel(writer, sheet_name='Sheet_Two', index=False)

import pandas as pd

Q1_sale_data = {
  'Product':['Laptop','Mouse','Keyboard','Monitor','Desk'],
  'Region':['North','South','East','North','South'],
  'Sale_Amount':[12000,500,1500,8000,3000]   
}
#ได้รับข้อมูลดิบมา ต้องแก้ไขให้เป็น dict ที่สามารถใช้งานได้ #โอ้ยยยยยยย

Q2_sale_data = {
  'Product':['Laptop','Mouse','Keyboard','Monitor','Chair'],
  'Region':['West','North','South','East','West'],
  'Sale_Amount':[10000,700,1800,7500,2500]   
}
   
# เอาdata มาสร้าง dataframe แยกเป็น df1, df2
df1 = pd.DataFrame(Q1_sale_data)
df2 = pd.DataFrame(Q2_sale_data)

#รวม dataframe เป็น multi_sheet.xlsx <<< อันนี้คือการจำลอง สร้างไฟล์ multisheet โดยเอาข้อมูล data ทั้งสอง มารวมกัน
#จำเป็นต้องใช้ with pd.ExcelWriter(ชื่อไฟล์ที่อยากสร้าง) as [writer] - writer คือชื่อเล่น ของ pd.ExcelWriter*** หากไม่กำหนดชื่อเล่น ต้องเขียนชื่อเต็มตลอดการใช้งาน
with pd.ExcelWriter('Sales_data.xlsx') as writer: # (กำหนดให้ writer ทำหน้าที่ เขียนexcel ชื่อSales_data.xlsx ***สำคัญต้องใช้เพื่อเขียนExcel*** )
    df1.to_excel(writer, sheet_name='Q1_Sales', index=False) #ใช้writerดึง dataframe1 เข้า pd.excel กำหนดชื่อชีท **ไม่ต้องใส่ indexตอนเขียน***อันนี้สำคัญ
    df2.to_excel(writer, sheet_name='Q2_Sales', index=False) #ดึง data อันที่2


#อ่านเฉพาะชีทชื่อ Q1_Sales จากไฟล์ sales_data.xlsx เข้ามาใน DataFrame ชื่อ df_q1_sales
df_q1_sales = pd.read_excel('Sales_data.xlsx', sheet_name='Q1_Sales')
print(df_q1_sales)

#กรองข้อมูลใน df_q1_sales เพื่อเลือกเฉพาะรายการที่ Region เป็น 'North'
north_q1 = df_q1_sales.loc[df_q1_sales['Region']=='North']
print(north_q1)

#บันทึก DataFrame ที่ถูกกรองแล้ว (เฉพาะยอดขายจากภูมิภาค North ของ Q1) 
# ลงใน ไฟล์ Excel ใหม่ ชื่อ north_region_q1_sales.xlsx ใน ชีทชื่อ North_Sales_Report
with pd.ExcelWriter('north_region_q1_sales.xlsx') as writer_report: # ✅ สร้าง writerอันใหม่ สำหรับไฟล์ใหม่
    north_q1.to_excel(writer_report, sheet_name='North_Sales_Report', index=False) # ✅ ใช้ writer_report และระบุ sheet_name
    
    
    
'''
โจทย์ของลูกคือ:

1.สร้างไฟล์ CSV จำลองทั้งสองไฟล์ (q1_raw_sales.csv และ q2_raw_sales.csv) ขึ้นมาในโค้ด
2.อ่านไฟล์ q1_raw_sales.csv และ q2_raw_sales.csv เข้ามาใน DataFrame ชื่อ df_q1_raw และ df_q2_raw ตามลำดับ
3.รวม DataFrame ทั้งสอง (df_q1_raw และ df_q2_raw) แล้ว บันทึกเป็นไฟล์ Excel ใหม่ชื่อ consolidated_sales.xlsx โดยให้:
    # จำเป็นต้องใช้ with pd.ExcelWriter(ชื่อไฟล์ที่อยากสร้าง) as [writer]
4.df_q1_raw ไปอยู่ในชีทชื่อ Quarter1_Sales
5.df_q2_raw ไปอยู่ในชีทชื่อ Quarter2_Sales
6.จาก consolidated_sales.xlsx ที่ลูกเพิ่งสร้างไป ให้ อ่านเฉพาะชีทชื่อ Quarter1_Sales เข้ามาใน DataFrame ชื่อ df_q1_final
7.กรองข้อมูลใน df_q1_final เพื่อเลือกเฉพาะรายการที่ Region เป็น 'North'
8.บันทึก DataFrame ที่ถูกกรองแล้วนี้ (เฉพาะยอดขายจากภูมิภาค North ของ Q1) ลงใน ไฟล์ Excel ใหม่ ชื่อ north_q1_report.xlsx ใน ชีทชื่อ North_Region_Summary
'''


#Sheet 1: Q1_Sales 
'''
Product,Region,Sales_Amount
Laptop,North,12000
Mouse,South,500
Keyboard,East,1500
Monitor,North,8000
Desk,South,3000
'''
#Sheet 2: Q2_Sales
'''
Product,Region,Sales_Amount
Laptop,West,10000
Mouse,North,700
Keyboard,South,1800
Monitor,East,7500
Chair,West,2500
'''

q1_data ="""Product,Region,Sales_Amount
Laptop,North,12000
Mouse,South,500
Keyboard,East,1500
Monitor,North,8000
Desk,South,3000"""


q2_data = """Product,Region,Sales_Amount
Laptop,West,10000
Mouse,North,700
Keyboard,South,1800
Monitor,East,7500
Chair,West,2500
"""  

import pandas as pd

with open('q1_raw_sale.csv', 'w') as f:
  f.write(q1_data)
with open('q2_raw_sale.csv', 'w') as f:
  f.write(q2_data)  
  
df_q1_raw_sale = pd.read_csv('q1_raw_sale.csv')
df_q2_raw_sale = pd.read_csv('q2_raw_sale.csv')

with pd.ExcelWriter('consolidated_sales.xlsx') as writer:
  df_q1_raw_sale.to_excel(writer, sheet_name= 'Quarter1_Sales', index=False)
  df_q2_raw_sale.to_excel(writer, sheet_name= 'Quarter2_Sales', index=False)

df_q1_final = pd.read_excel('consolidated_sales.xlsx', sheet_name='Quarter1_Sales')
print(f"{df_q1_final} <<<")

north_sale_q1 = df_q1_final.loc[df_q1_final['Region'] == 'North']

with pd.ExcelWriter('north_q1_report.xlsx') as writer:
  north_sale_q1.to_excel(writer, sheet_name='North_Region_Summary', index=False)
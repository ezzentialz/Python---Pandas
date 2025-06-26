import pandas as pd

df_customers = pd.DataFrame({'CustomerID':['C001','C002','C003','C004'],
'Name':['Alice','Bob','Charlie','David'],
'City':['Bangkok','Chiang Mai','Phuket','Bangkok']})

df_orders = pd.DataFrame({'OrderID':['ORD001','ORD002','ORD003','ORD004'],
'CustomerID':['C001','C003','C001','C005'],
'Product':['Laptop','Mouse','Keyboard','Monitor'],
'Amount':[12000,500,1500,8000]})

df_customer_orders = pd.merge(df_customers,df_orders, on='CustomerID', how='inner')
#inner จะเหมือนจะคู่data ที่มีข้อมูล'CustomerID' เหมือกัน C001,C003,C001(มีซ้ำในdf_orders) อันที่ไม่เหมือนกัน ไม่เอา
print("\n -------------------pd.merge() inner-----------------------")
print(df_customer_orders)

df_employees = pd.DataFrame({'EmployeeID':['E001','E002','E003','E004'],
'Name':['Alice','Bob','Charlie','David'],
'DepartmentID':['D1','D2','D1','D4']
})

df_departments = pd.DataFrame({'DepartmentID':['D1','D2','D3'],
'DepartmentName':['HR','IT','Marketing'],
'Location':['Building A','Building B','Building C']})

df_employees_departments = pd.merge(df_employees,df_departments, on='DepartmentID', how='left')
print("\n -------------------pd.merge() how = left-----------------------") #ยึดข้อมูลฝั่งซ้าย เอาข้อมูลฝั่งขวาเติม จุดเชื่อมกันคือ'DepartmentID'
print(df_employees_departments)

df_products = pd.DataFrame({'ProductID':['P101','P102','P103','P105'],
'ProductName':['Laptop','Mouse','Keyboard','Webcam'],
'Price':[12000,500,1500,800]})

df_stock = pd.DataFrame({'Item_ID':['P101','P103','P104'],
'Quantity':[50,100,20],
'Warehouse':['A','B','C']})

df_products_stock = pd.merge(df_products,df_stock, left_on='ProductID', right_on='Item_ID', how='outer')
print("\n -------------------pd.merge() left_on และ right_on (จุดเชื่อมคือ ID: P101,P102..)how = outer-----------------------") 
#ระบุข้อมูลฝั่งซ้าย และ ฝั่งขวา ด้วยข้อมูลที่แชร์กันได้เช่น ID: P101,P102,P103,,,  แล้ว เอาข้อมูลทั้งหมด ของทั้งสองอัน รวมกัน >> how= outer
print(df_products_stock)
import pandas as pd

df_user_profile = pd.DataFrame({
    'UserID': ['U001', 'U002'],
    'Name': ['Alice', 'Bob'],
    'JoinDate': ['2023-01-01', '2023-02-15'] # คอลัมน์ชื่อซ้ำ
})
print("--- User Profile ---")
print(df_user_profile)

df_user_activity = pd.DataFrame({
    'UserID': ['U001', 'U002'],
    'LastLogin': ['2024-06-19', '2024-06-18'],
    'JoinDate': ['2023-01-01', '2023-02-15'] # คอลัมน์ชื่อซ้ำ (แต่ไม่ใช้ Join)
})
print("\n--- User Activity ---")
print(df_user_activity)

# ลอง merge แบบปกติ
df_merged_default = pd.merge(df_user_profile, df_user_activity, on='UserID', how='inner')
print("\n--- Merged (Default Suffixes) ---")
print(df_merged_default)
# จะเห็น JoinDate_x และ JoinDate_y

# 🚀 ตัวอย่าง: ใช้ suffixes เพื่อตั้งชื่อใหม่ให้คอลัมน์ที่ซ้ำกัน
df_merged_suffixes = pd.merge(
    df_user_profile,
    df_user_activity,
    on='UserID',
    how='inner',
    suffixes=('_Profile', '_Activity') # กำหนด suffix เอง
)
print("\n--- Merged (Custom Suffixes) ---")
print(df_merged_suffixes)
# จะเห็น JoinDate_Profile และ JoinDate_Activity



import pandas as pd

# DataFrame พนักงาน (มี EmployeeID, Name, และ ManagerID)
df_employees = pd.DataFrame({
    'EmployeeID': [101, 102, 103, 104],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'ManagerID': [None, 101, 101, 102] # Alice (101) ไม่มี Manager, Bob (102) มี Alice เป็น Manager
})
print("--- Employee Data ---")
print(df_employees)

# 🚀 ตัวอย่าง: Self-Merge เพื่อหาชื่อผู้จัดการ
# เราจะ merge df_employees กับ df_employees เอง
# df_employees (ฝั่งซ้าย) ใช้ EmployeeID เป็น Key ของพนักงาน
# df_employees (ฝั่งขวา) ใช้ ManagerID เป็น Key เพื่อดึงข้อมูลผู้จัดการ
df_employees_with_manager = pd.merge(
    df_employees,               # Left DataFrame
    df_employees,               # Right DataFrame (ตัวมันเอง)
    left_on='ManagerID',        # Key ของฝั่งซ้าย (ManagerID ของพนักงาน)
    right_on='EmployeeID',      # Key ของฝั่งขวา (EmployeeID ของผู้จัดการ)
    how='left',                 # Left Join เพื่อเก็บพนักงานทุกคนไว้
    suffixes=('_Employee', '_Manager') # กำหนด suffix เพื่อแยกคอลัมน์ Name, EmployeeID ที่ซ้ำกัน
)
print("\n--- Employee Data with Manager Names (Self-Merge) ---")
print(df_employees_with_manager)

# เลือกเฉพาะคอลัมน์ที่ต้องการแสดงผล
df_final_employees = df_employees_with_manager[['EmployeeID_Employee', 'Name_Employee', 'Name_Manager']]
df_final_employees = df_final_employees.rename(columns={
    'EmployeeID_Employee': 'EmployeeID',
    'Name_Employee': 'EmployeeName',
    'Name_Manager': 'ManagerName'
})
print("\n--- Employee Data (Cleaned) ---")
print(df_final_employees)




import pandas as pd

df_enrollment= pd.DataFrame({'StudentID':['S001','S002','S001','S003'],
'CourseID':['C101','C102','C102','C101'],
'EnrollmentDate':['2024-01-10','2024-01-15','2024-01-20','2024-01-25']})

df_attendance = pd.DataFrame({'StudentID':['S001','S001','S002','S003','S004'],
'CourseID':['C101','C102','C102','C101','C103'],
'AttendanceDate':['2024-02-01','2024-02-05','2024-02-10','2024-02-15','2024-02-20'],
'Status':['Present','Present','Absent','Present','Present']})

print(df_enrollment)
print(df_attendance)

#ใช้ pd.merge() เพื่อรวมสอง DataFrame นี้ โดยใช้ Multiple Keys 
# (StudentID และ CourseID) และใช้ Left Join (how='left') โดยให้ df_enrollment เป็น DataFrame ฝั่งซ้าย
print('\n ----------------pd.merge() ใช้ on คอลลั่มที่ต้องการ1','คอลลั่มที่ต้องการ2 นำมารวมกันโดยยึดข้อมูลฝั่งซ้าย how = left---------- \n')
df_enrollment_attendace = pd.merge(df_enrollment,df_attendance, on=['StudentID', 'CourseID'], how='left')
print(df_enrollment_attendace)


df_products_hierarchy = pd.DataFrame({'ProductID':['P001','P002','P003','P004','P005'],
'ProductName':['Desktop PC','Monitor','Keyboard','Laptop','Mouse'],
'ParentProductID':[None,'P001','P001',None,'P004']
})
print('\n ----------------dataFrame---------- \n')
print(df_products_hierarchy)

#ใช้ pd.merge() เพื่อรวม df_products_hierarchy เข้ากับตัวมันเอง (Self-Merge) 
# เพื่อให้ได้คอลัมน์ชื่อผลิตภัณฑ์หลัก (ParentProductName) มาอยู่ข้างๆ ชื่อผลิตภัณฑ์ย่อย
df_products_hierarchy_merge = pd.merge(df_products_hierarchy,df_products_hierarchy,left_on='ParentProductID', right_on='ProductID', suffixes=('_Parent','_Product'), how='left')
print(df_products_hierarchy_merge)

df_products_hierarchy_merge = df_products_hierarchy_merge[['ProductID_Parent','ProductName_Parent','ParentProductID_Parent','ProductName_Product']]
df_products_hierarchy_merge = df_products_hierarchy_merge.rename(columns={
    'ProductID_Parent' : 'ProductID',
    'ProductName_Parent' : 'ProductName',
    'ParentProductID_Parent' : 'ParentProductID',
    'ProductName_Product' : 'ParentProductName'
})
print(df_products_hierarchy_merge)
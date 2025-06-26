import pandas as pd

grade = {
'StudentID':['S001','S002','S001','S003','S002','S003','S001','S002'],
'Subject':['Math','Science','Science','Math','Math','Science','English','English'],
'Score':[85,70,90,60,75,80,92,88]}

df_grades = pd.DataFrame(grade)
#สร้าง dataframe
print("\n ---------------DataFrame-------------- \n")
print(df_grades)

#หาคะแนนเฉลี่ย (Mean Score) ของนักเรียนแต่ละคน (StudentID)
mean_score = df_grades.groupby('StudentID')[['Score']].mean()
print("\n ---------------หาค่าเฉลี่ย 'Score' จากGroup'StudentID'-------------- \n")
print(mean_score)

#หาคะแนนสูงสุด (Max Score) และคะแนนต่ำสุด (Min Score) ของแต่ละวิชา (Subject)
max_score = df_grades.groupby('Subject')[['Score']].max()
min_score = df_grades.groupby('Subject')[['Score']].min()

min_max_score = df_grades.groupby('Subject').agg( #ตรงนี้เข้าใจว่าเป็นการสร้างคอลลัมใหม่ เพื่อดู min/Max 
    Min_Score = ('Score', 'min'),
    Max_Score = ('Score', 'max')
)
print("\n ---------------หาค่าสูงสุด/ต่ำสุด 'Score' จากGroup'Subject'-------------- \n")
print(max_score)
print(min_score)
print('\n อันนี้ลองทำ \n') 
print(min_max_score)

#ใช้ .agg() เพื่อหา:
#คะแนนเฉลี่ย (mean)
#จำนวนวิชาที่นักเรียนแต่ละคนลงทะเบียน (count) (อาจจะนับจากคอลัมน์ Subject)
#โดยจัดกลุ่มตาม StudentID
#ตั้งชื่อคอลัมน์ผลลัพธ์ว่า Average_Score และ Subject_Count ตามลำดับ

avg_score_sub_count = df_grades.groupby('StudentID').agg(
    Average_Score = ('Score', 'mean'),
    Subject_Count = ('Subject', 'count')
)
print("\n -จากGroup'StudentID' ใช้ agg สร้างคอลลัมใหม่ Average_score หาค่าเฉลี่ย score.mean() /สร้างคอลลัมใหม่ Subject_count นับSubject subject.count() -\n")
print(avg_score_sub_count)




'''
UserID,App_Name,Usage_Minutes,Data_Usage_MB
,,,'''

app_usage = {
'UserID':['U001','U002','U001','U003','U002','U001','U003','U002'],
'App_Name':['Facebook','Instagram','YouTube','Facebook','YouTube','Instagram','TikTok','Facebook'],
'Usage_Minutes':[60,45,120,30,90,20,70,15],
'Data_Usage_MB':[100,80,500,50,300,40,120,30]
}

df_app_usage = pd.DataFrame(app_usage)
print(df_app_usage)

#หายอดรวมเวลาใช้งาน (Usage_Minutes) และยอดรวมการใช้ข้อมูล (Data_Usage_MB) ของแต่ละ UserID
total_min_data_usage = df_app_usage.groupby('UserID')[['Usage_Minutes','Data_Usage_MB']].sum()
print(total_min_data_usage)

#หาแอปพลิเคชันที่มีผู้ใช้มากที่สุด (App_Name ที่มี UserID ไม่ซ้ำกันมากที่สุด) (ใช้ .nunique() ในการนับ UserID ที่ไม่ซ้ำกันหลังจาก groupby('App_Name'))
max_app_usage = df_app_usage.groupby('App_Name')[['UserID']].nunique()
print(max_app_usage)

#ใช้ .agg() เพื่อหา:
#เวลาใช้งานเฉลี่ย (mean)
#การใช้ข้อมูลสูงสุด (max)
#ของ Usage_Minutes และ Data_Usage_MB โดยจัดกลุ่มตาม App_Name
#ตั้งชื่อคอลัมน์ผลลัพธ์ว่า Avg_Minutes, Max_Data_MB ตามลำดับ
avg_min_max_data = df_app_usage.groupby('App_Name').agg(
    Avg_Minutes = ('Usage_Minutes', 'mean'),
    Max_Data_MB = ('Data_Usage_MB', 'max')
)
print(avg_min_max_data)
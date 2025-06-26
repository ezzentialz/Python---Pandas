import pandas as pd

# สร้าง DataFrame ข้อมูลนักเรียน
student_data = {
    'Student_ID': ['S001', 'S002', 'S003', 'S004', 'S005'],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [18, 19, 18, 20, 19],
    'Grade': ['A', 'B', 'A', 'C', 'B']
}
df_students = pd.DataFrame(student_data, index=['Idx_A', 'Idx_B', 'Idx_C', 'Idx_D', 'Idx_E'])

print("--- Original DataFrame (df_students) ---")
print(df_students)
print("\n" + "-" * 30 + "\n")

#เข้า loc แถว Idx_C แล้วปริ้นออกมาทั้งแถว
print(df_students.loc['Idx_C'])
print("\n" + "-" * 30 + "\n")
# เลือกเฉพาะ column Name, Grade และ label A ถึง D
print(df_students.loc['Idx_A':'Idx_D', ['Name','Grade']])
print("\n" + "-" * 30 + "\n")

#เข้า iloc แถว แรก แล้วปริ๊นออกมาทั้งแถว
print(df_students.iloc[0])
print("\n" + "-" * 30 + "\n")
# เลือกเฉพาะ clomun 1(Name), 3(Grade) และ label 0 ถึง 3
print(df_students.iloc[0:3, [1,3]])
print("\n" + "-" * 30 + "\n")



#โจทย์แบบฝึกหัด
import pandas as pd

student_data = {
    'Student_ID': ['S001', 'S002', 'S003', 'S004', 'S005', 'S006'], # เพิ่ม S006
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'], # เพิ่ม Frank
    'Age': [18, 19, 18, 20, 19, 21], # เพิ่ม 21
    'Grade': ['A', 'B', 'A', 'C', 'B', 'A'] # เพิ่ม A
}
# ✅ หมอเพิ่ม Index Label 'Idx_F' ด้วยนะครับ
df_students = pd.DataFrame(student_data, index=['Idx_A', 'Idx_B', 'Idx_C', 'Idx_D', 'Idx_E', 'Idx_F'])

print("--- Original DataFrame (df_students - Updated) ---")
print(df_students)
print("\n" + "-" * 30 + "\n")

print("\n" + "-"* 10 + "Grade A Studens" + "-"*10)
df_students_grade_A = df_students.loc[df_students['Grade']=='A']
print(df_students_grade_A)

print("\n" + "-"* 10 + "iloc แถวที่1 - 4" + "-"*10)
print(df_students.iloc[1:4])

print("\n" + "-"* 10 + "เฉพาะแถวที่ 0 และ คอลลัม3" + "-"*10)
print(df_students.iloc[1, 3])

print("\n" + "-"* 10 + "ใช้ loc เฉพาะ เกรด B และ iloc 1(name),2(Age)" + "-"*10)
students_grade_B = df_students['Grade']=='B'

print(df_students.loc[students_grade_B, df_students.columns[[1,2]]])





import pandas as pd

student_data = {
    'Student_ID': ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008'], # เพิ่ม S007, S008
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry'], # เพิ่ม Grace, Henry
    'Age': [18, 19, 18, 20, 19, 21, 20, 18], # เพิ่ม 20, 18
    'Grade': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B'], # เพิ่ม C, B
    'Score': [90, 75, 88, 65, 78, 92, 60, 70] # ✅ เพิ่มคอลัมน์ Score
}
# ✅ หมอเพิ่ม Index Label ด้วยนะครับ
df_students = pd.DataFrame(student_data, index=['Idx_A', 'Idx_B', 'Idx_C', 'Idx_D', 'Idx_E', 'Idx_F', 'Idx_G', 'Idx_H'])

print("--- Original DataFrame (df_students - Final Update) ---")
print(df_students)
print("\n" + "-" * 30 + "\n")

# เลือกข้อมูลของนักเรียนที่ อายุ (Age) น้อยกว่า 20 ปี และ มี Grade เป็น 'B' แล้วพิมพ์ออกมา
df_students_gradeB_under20 = df_students.loc[(df_students['Age'] <20) & (df_students['Grade']=='B')]
print(df_students_gradeB_under20)

#ค้นหา 'Score' ของนักเรียนที่มี 'Student_ID' เป็น 'S005' แล้วพิมพ์ค่า Score นั้นออกมาเพียงค่าเดียว (ไม่เอาทั้งแถวหรือทั้งคอลัมน์)
score = df_students.loc[df_students['Student_ID'] == 'S005', 'Score'].item()
print(score)

#เปลี่ยน Grade ของนักเรียนชื่อ 'David' จาก 'C' ให้เป็น 'B+'
#และเปลี่ยน Score ของนักเรียนชื่อ 'Alice' จาก 90 ให้เป็น 95
#จากนั้น พิมพ์ DataFrame df_students ทั้งหมด ออกมาเพื่อดูผลการเปลี่ยนแปลง
df_students.loc[df_students['Name']=='David', 'Grade'] = 'B+'

df_students.loc[df_students['Name']=='Alice', 'Score'] = 95

print(df_students)



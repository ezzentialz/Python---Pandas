import pandas as pd
import numpy as np


customers = { 
'CustomerID' :['C001','C002','C003','C004','C005'],
'FullName':['John Doe','Alice Wonderland','Bob The Builder','Charlie Puth','Emily Blunt'],
'Email':['john.doe@example.com','alice.w@example.com','bob.builder@example.com','charlie.p@example.com','emily.b@example.com']}

df_customers = pd.DataFrame(customers)

#เช็ค df 
print(df_customers)
print('\n ------------------------ \n')
# ต้องการสร้างคอลัมน์ใหม่สำหรับเก็บ ชื่อแรก (First Name) เท่านั้นครับ
def first_name(row):
    fullname = row['FullName']
    name_split = fullname.split()
    first_name = name_split[0]
    return first_name

#สร้างก้อปปี้
df_customers1 = df_customers.copy()
#สร้างคอลลัม 'FirstName' โดยใช้ .apply() กับคอลัมน์ FullName
df_customers1['FirstName'] = df_customers1.apply(first_name, axis=1)
#test ครั้งแรก 
print('DataFrame with FirstName column')
print(df_customers1)
print("\n")


################################################################################################



movies= {
'MovieTitle':['Inception','The Matrix','Dune,Pulp','Fiction'],
'Critic1_Score':[9.0,8.8,7.5,9.5],
'Critic2_Score' :[8.5,9.0,8.0,9.3],
'Critic3_Score' :[9.2,8.7,8.2,9.0]}

df_movies = pd.DataFrame(movies)
#สร้าง df
print(df_movies)
#สร้างฟังก์ชัน Python ชื่อ calculate_average_score() ที่รับพารามิเตอร์เป็น row (แทนข้อมูลแต่ละแถว) 
# และส่งคืนค่า คะแนนเฉลี่ย ของ Critic1_Score, Critic2_Score, และ Critic3_Score ในแถวนั้น

def calculate_average_score(row):
    critic_score1 = row['Critic1_Score']
    critic_score2 = row['Critic2_Score']
    critic_score3 = row['Critic3_Score']
    sum_score = critic_score1 + critic_score2 + critic_score3
    mean_score = sum_score / 3 #จำวิธีาค่าเฉลี่ย ไม่ได้ครับ แป่ววว จำได้คร่าวๆว่า เอาผลรวม มาหาร จำนวน
    return mean_score

df_movies['Average_Rating'] = df_movies.apply(calculate_average_score, axis=1)
#test 1
print(df_movies)
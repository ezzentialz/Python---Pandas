# --- Python Code สำหรับสร้างไฟล์ Markdown สรุป Pandas ---

markdown_content = """
# 🐼 สรุป Pandas: การจัดการข้อมูลแบบตาราง

Pandas เป็นไลบรารีที่ทรงพลังสำหรับ Python ที่ใช้ในการจัดการและวิเคราะห์ข้อมูล โดยเฉพาะข้อมูลที่เป็นตาราง (Tabular Data) เหมือนใน Excel หรือ Database ครับ สร้างขึ้นบนพื้นฐานของ NumPy ทำให้ทำงานกับข้อมูลตัวเลขได้อย่างรวดเร็ว

---

## โครงสร้างข้อมูลหลักใน Pandas

1.  ### **`Series` (1 มิติ)**
    * เปรียบเสมือนคอลัมน์เดียวในตาราง หรือ List ที่มีชื่อกำกับ (Index)
    * **ตัวอย่าง:**
        ```python
        import pandas as pd
        s = pd.Series([10, 20, 30, 40], name='MyNumbers')
        # print(s)
        # Output:
        # 0    10
        # 1    20
        # 2    30
        # 3    40
        # Name: MyNumbers, dtype: int64
        ```

2.  ### **`DataFrame` (2 มิติ)**
    * หัวใจหลักของ Pandas! มันคือ **ตาราง** ที่ประกอบด้วยหลายคอลัมน์ แต่ละคอลัมน์คือ `Series`
    * มีทั้ง Index (สำหรับแถว) และ Column Names (สำหรับคอลัมน์)
    * **การสร้าง DataFrame (นิยมใช้ Dictionary of Lists):**
        ```python
        import pandas as pd
        data = {
            'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, 22],
            'City': ['NY', 'LDN', 'PAR']
        }
        df = pd.DataFrame(data)
        # print(df)
        # Output:
        #       Name  Age City
        # 0    Alice   25   NY
        # 1      Bob   30  LDN
        # 2  Charlie   22  PAR
        ```
    * สามารถกำหนด `index` เองได้:
        ```python
        # df_indexed = pd.DataFrame(data, index=['A', 'B', 'C'])
        ```

---

## การสำรวจข้อมูลเบื้องต้น (Initial Data Exploration)

หลังจากสร้างหรืออ่าน DataFrame แล้ว เรามักจะสำรวจข้อมูลเพื่อทำความเข้าใจโครงสร้างและภาพรวม:

* **`df.head(n=5)`**: แสดง `n` แถวแรกของ DataFrame (ค่าเริ่มต้นคือ 5 แถว)
* **`df.tail(n=5)`**: แสดง `n` แถวสุดท้ายของ DataFrame (ค่าเริ่มต้นคือ 5 แถว)
* **`df.shape`**: คืนค่าเป็น Tuple `(จำนวนแถว, จำนวนคอลัมน์)`
* **`df.columns`**: แสดงรายชื่อคอลัมน์ทั้งหมด
* **`df.info()`**: แสดงข้อมูลสรุปของ DataFrame เช่น จำนวนแถว/คอลัมน์, ชนิดข้อมูลของแต่ละคอลัมน์, จำนวนค่าที่ไม่ใช่ค่าว่าง (Non-Null Count)
* **`df.describe()`**: แสดงสถิติพื้นฐานของคอลัมน์ที่เป็นตัวเลข (เช่น count, mean, std, min, max, quartile)

---

## การเลือกและการกรองข้อมูล (Selection & Filtering)

เป็นหัวใจสำคัญของการทำงานกับ DataFrame!

1.  ### **เลือกคอลัมน์**
    * **คอลัมน์เดียว:** `df['ColumnName']` (คืนค่าเป็น `Series`)
        ```python
        # print(df['Name'])
        ```
    * **หลายคอลัมน์:** `df[['Col1', 'Col2']]` (คืนค่าเป็น `DataFrame`)
        ```python
        # print(df[['Name', 'Age']])
        ```

2.  ### **`.loc` (Label-based Selection)**
    * ใช้เลือกข้อมูลโดยใช้ **"ชื่อ (Label)"** ของ Index (แถว) และชื่อของคอลัมน์
    * **รูปแบบ:** `df.loc[row_label(s), column_label(s)]`
    * **ตัวอย่าง:**
        ```python
        # สมมติ df_indexed = pd.DataFrame(data, index=['A', 'B', 'C'])
        # print(df_indexed.loc['A', 'Name'])       # เลือกเซลล์เดียว: 'Alice'
        # print(df_indexed.loc[['A', 'C'], 'Age']) # เลือกหลายแถว, คอลัมน์เดียว
        # print(df_indexed.loc['B':'C', ['Age', 'City']]) # Slicing: 'B' ถึง 'C' (รวม 'C')
        ```
    * **การกรองข้อมูลด้วยเงื่อนไข (Conditional Selection):**
        * ใส่ `Boolean Series` เข้าไปในส่วนของแถว
        * **ตัวอย่าง:**
            ```python
            # เลือกนักเรียนที่มีอายุมากกว่า 25
            # print(df.loc[df['Age'] > 25])

            # เลือกนักเรียนที่มีอายุ < 30 และอยู่ใน NY (ใช้ & สำหรับ AND)
            # print(df.loc[(df['Age'] < 30) & (df['City'] == 'NY')])

            # เลือกนักเรียนที่มีอายุ > 28 หรืออยู่ใน PAR (ใช้ | สำหรับ OR)
            # print(df.loc[(df['Age'] > 28) | (df['City'] == 'PAR')])
            ```
            * **สำคัญ:** ต้องใส่วงเล็บ `()` ครอบแต่ละเงื่อนไขเมื่อใช้ `&` หรือ `|`

3.  ### **`.iloc` (Integer-location based Selection)**
    * ใช้เลือกข้อมูลโดยใช้ **"ตำแหน่ง (Position)" ที่เป็นตัวเลขเท่านั้น** (เริ่มจาก 0 เหมือน List)
    * **รูปแบบ:** `df.iloc[row_position(s), column_position(s)]`
    * **ตัวอย่าง:**
        ```python
        # print(df.iloc[0, 0])           # เลือกเซลล์เดียว: 'Alice'
        # print(df.iloc[[0, 2], 1])      # เลือกหลายแถว, คอลัมน์เดียว (Age ของ Alice, Charlie)
        # print(df.iloc[1:3, [1, 2]])    # Slicing: แถวตำแหน่ง 1 ถึง 2 (ไม่รวม 3), คอลัมน์ตำแหน่ง 1 ถึง 2
        ```
    * **สำคัญ:** การ Slicing ด้วยตำแหน่ง `start:end` จะ **ไม่รวม** ตำแหน่ง `end` (เหมือน Python List ทั่วไป)

---

## การเปลี่ยนแปลงข้อมูล (Updating Data)

ใช้ `.loc` หรือ `.iloc` ในการระบุตำแหน่งที่ต้องการเปลี่ยนแปลง **ทางด้านซ้ายมือของเครื่องหมาย `=`**

* **เปลี่ยนค่าในเซลล์เดียว:**
    ```python
    # df.loc[0, 'Age'] = 26 # เปลี่ยนอายุของ Alice เป็น 26
    ```
* **เปลี่ยนค่าทั้งคอลัมน์ (ตามเงื่อนไข):**
    ```python
    # df.loc[df['City'] == 'NY', 'City'] = 'New York City' # เปลี่ยน 'NY' เป็น 'New York City'
    ```

---

## การอ่านและเขียนไฟล์ (File I/O)

เชื่อมโยง DataFrame เข้ากับโลกภายนอก!

1.  ### **อ่านไฟล์ CSV:**
    * `pd.read_csv('filepath/filename.csv', sep=',')`
    * พารามิเตอร์สำคัญ: `sep`, `header`, `index_col`, `encoding`

2.  ### **อ่านไฟล์ Excel:**
    * `pd.read_excel('filepath/filename.xlsx', sheet_name='Sheet1')`
    * พารามิเตอร์สำคัญ: `sheet_name`, `header`, `index_col`
    * **ต้องติดตั้ง:** `pip install openpyxl` (สำหรับ .xlsx) หรือ `pip install xlrd` (สำหรับ .xls)

3.  ### **เขียน DataFrame ลงไฟล์ CSV:**
    * `df.to_csv('new_file.csv', index=False)`
    * `index=False`: ไม่บันทึก Index ของ DataFrame ลงไปด้วย

4.  ### **เขียน DataFrame ลงไฟล์ Excel (ชีทเดียว):**
    * `df.to_excel('new_file.xlsx', index=False)`

5.  ### **เขียน DataFrame หลายอันลงในไฟล์ Excel เดียว (หลายชีท):**
    * ใช้ `pd.ExcelWriter()` ร่วมกับ `with` statement
    * **ตัวอย่าง:**
        ```python
        # with pd.ExcelWriter('multi_sheet_report.xlsx') as writer:
        #     df_data1.to_excel(writer, sheet_name='Data_Sheet1', index=False)
        #     df_data2.to_excel(writer, sheet_name='Data_Sheet2', index=False)
        ```
    * `writer` คือ Object ที่ทำหน้าที่จัดการการเขียนไฟล์ Excel หลายชีท

---

**สรุป NumPy ที่เกี่ยวข้อง:**

* **NumPy (`ndarray`)** เป็นรากฐานของ Pandas DataFrame
* ให้ประสิทธิภาพสูงในการคำนวณตัวเลขขนาดใหญ่ และการดำเนินการแบบ **Element-wise**

---
"""

file_name = "Pandas_Summary.md"

try:
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(markdown_content)
    print(f"--- ไฟล์ '{file_name}' ถูกสร้างเรียบร้อยแล้วครับ! ---")
    print("ลูกสามารถเปิดไฟล์นี้ด้วยโปรแกรม Text Editor หรือ VS Code เพื่อดูเนื้อหาได้เลยครับ")
except Exception as e:
    print(f"โอ้ยยยยยยลูกกกกกกกก เกิดข้อผิดพลาดในการสร้างไฟล์ครับ: {e}")
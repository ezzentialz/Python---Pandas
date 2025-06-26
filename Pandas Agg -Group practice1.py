import pandas as pd

quarterly_sales = {
'Branch':['BKK1','BKK2','BKK1','CMX1','BKK2','CMX1','BKK1','CMX1','BKK2'],
'Category':['Electronics','Apparel','Electronics','Home Goods','Electronics','Apparel','Home Goods','Electronics','Home Goods'],
'Item':['Laptop','T-shirt','Mouse','Lamp','Monitor','Jeans','Chair','Keyboard','Table'],
'Sales_Amount':[120000,800,5000,1500,10000,2500,3000,2000,5000],
'Units_Sold': [10,20,50,10,5,5,3,10,1]     
}

df_quarterly_sales = pd.DataFrame(quarterly_sales)
#สร้าง dataframe
print("--------------Data Frame---------------")
print(df_quarterly_sales)

#หายอดขายรวม (Sales_Amount) และจำนวนหน่วยที่ขายได้รวม (Units_Sold) ของแต่ละ Branch
branch_quarterly_sales = df_quarterly_sales.groupby('Branch')[['Sales_Amount','Units_Sold']].sum()
print("\n --------------Group Branch ดูผลรวมของ Sales amount กับ units sold--------------- \n")
print(branch_quarterly_sales)

#หาจำนวนสินค้าที่ไม่ซ้ำกัน (Item) ในแต่ละ Category (ใช้ .nunique() ในการนับค่าที่ไม่ซ้ำกัน)
unique_item = df_quarterly_sales.groupby('Category')[['Item']].nunique()
print("\n --------------Group Category ดูitem ไม่ซ้ำกัน ใช้ .nunique() ในการนับค่าที่ไม่ซ้ำกัน--------------- \n")
print(unique_item)

#ใช้ .agg() เพื่อหายอดขายรวม (sum) และยอดขายเฉลี่ย (mean) ของ Sales_Amount 
# ในแต่ละ Category และตั้งชื่อคอลัมน์ผลลัพธ์เป็น Total_Sales และ Average_Sales ตามลำดับ
quarterly_sales_agg = df_quarterly_sales.groupby('Category').agg( #กรุ๊ป category แล้ว .agg(เพื่อใช้ฟังชั่นกับหลายตัวกับคอลลัมอื่น)
    Total_sales = ('Sales_Amount', 'sum'), #ตรงนี้ สร้าง คอลลัมใหม่ชื่อ Total_sales รับค่า > ฟังชัน sum ค่าทั้งหมดของ Sales_Amount
    Average_Sales = ('Sales_Amount','mean')  #คอลลัมใหม่ Average_Sales รับค่า > mean(เฉลี่ย) ทั้งหมดของ Sales_Amount
)
print("\n ----Group Category ใช้ agg ให้คอลลัมใหม่ Total_sales= Sales_Amount.sum() / Average_Sales = Sales_Amount.mean()--------------- \n")# คิดว่าอารมณ์น่าจะประมาณนี้
print(quarterly_sales_agg)
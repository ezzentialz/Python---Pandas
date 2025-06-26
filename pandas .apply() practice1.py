import pandas as pd

data = {
    'Product': ['Laptop', 'Mouse', 'Keyboard'],
    'Price': [1200, 25, 75],
    'Quantity': [2, 5, 3]
}
df_orders = pd.DataFrame(data)
print("--- DataFrame เดิม ---")
print(df_orders)

# 🚀 สร้างฟังก์ชันที่จะประมวลผลแต่ละแถว
def create_order_summary(row):
    product = row['Product']
    price = row['Price']
    quantity = row['Quantity']
    total = price * quantity
    return f"Order: {quantity}x {product} at ${price} each. Total: ${total}"

# ใช้ .apply() กับ DataFrame และระบุ axis=1
df_orders['Order_Summary'] = df_orders.apply(create_order_summary, axis=1)

print("\n--- DataFrame หลังใช้ .apply(axis=1) สร้าง Summary ---")
print(df_orders)
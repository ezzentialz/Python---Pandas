import pandas as pd

df_customer_details = pd.DataFrame({
'CustomerID':['C001','C002','C003','C004'],
'Name':['Alice','Bob','Charlie','David'],
'Email':['alice@email.com','bob@email.com','charlie@email.com','david@email.com'],
})

df_subscriptions = pd.DataFrame({
'SubscriptionID':['SUB001','SUB002','SUB003','SUB004'],
'CustomerID':['C001','C002','C001','C005'],
'ServiceType':['Premium','Basic','Extra_Storage','VIP'],
'StartDate':['2024-01-01','2024-02-15','2024-03-01','2024-04-01'],
})

print(df_customer_details)
print(df_subscriptions)

df_customer_sub = pd.merge(df_customer_details,df_subscriptions, on='CustomerID', how='left' )
print(df_customer_sub)


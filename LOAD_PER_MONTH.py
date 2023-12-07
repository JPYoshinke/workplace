#月ごとの差分チェック
import pandas as pd

#Snowflake - Azure = df3
df1 = pd.read_csv('../Snow_data.csv') #Snowflakeのデータ
df2 = pd.read_csv('../Azure_data.csv') #Azureのデータ
#print(df1)
#print(df2)



df3 = df1.copy()
df3.iloc[:,3:] = df1.iloc[:,3:] - df2.iloc[:,3:]
#print(df3)

S_Customer = df1["M_顧客数"]
A_Customer = df2["M_顧客数"]

Cust_Result = S_Customer- A_Customer
df3[["M_顧客数"]] = Cust_Result

print(df3)

#全体での引き算はうまくいかないがカラムごとだとうまくいく
#動きを確認しつつ修正する必要がある
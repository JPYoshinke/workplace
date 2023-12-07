#下記が各プロセス
#1.日ごとの差分チェック
#2.最後の差分チェックの仕組みは完成
#######  必ずOpenVPNでAzuregatewayをConnectした状態にすること      ######
import pyodbc
import pprint
import csv
import pandas as pd



#import respectivly csv , Snowflake and Azure
df1 = pd.read_csv('../S_202202.csv') #Snowflakeのデータ
df2 = pd.read_csv('../A_202202.csv') #Azureのデータ


#Snowflake - Azure = df3
df3 = df1.copy()
df3.iloc[:,3:] = df1.iloc[:,3:] - df2.iloc[:,3:]
col_id = df3.iloc[:,2]

print(df3["受注番号"])
#Delete duplicate and order by increment_id acendant
col_id = set(list(col_id))
st_col_id = str(col_id)
#print(st_col_id)




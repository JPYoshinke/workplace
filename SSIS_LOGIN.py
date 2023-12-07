
#最後の差分チェックの仕組みは完成
# -*- coding: utf-8 -*-
import pyodbc
import pprint

def login():
    # SQL_SERVER_NAME
    instance = "edsdi-sqlmi-p-1.7f600c251aab.database.windows.net"
    # ユーザー
    user = "KengoYoshinaga"
    #パスワード
    pasword = "ySc4z$cM,8#PrZqS"
    #DB
    db = "Reporting"

    connection = "DRIVER={SQL Server};SERVER=" + instance + ";uid=" + user + \
                 ";pwd=" + pasword + ";DATABASE=" + db


    return pyodbc.connect(connection)

if __name__ == '__main__':
    con = login()


# 検索
cursor = con.cursor()
cursor.execute( "select so.increment_id,so.created_at,so.updated_at,soi.sku,soi.name, sob.price as sob_price, null as sob_tax_riki, sob.tax_amount as sob_tax_amount, sob.discount_amount_excl_tax as sob_discount_amount_excl_tax, sob.qty_ordered as sob_qty_ordered, so.used_point as so_used_point, sop.method as sop_method, c.FIRST_NAME, c.LAST_NAME from MagentoOnlineshop.[dbo].[sales_order] so inner join MagentoOnlineshop.dbo.sales_order_item soi  on so.entity_id = soi.order_id and soi.product_type != 'bundle' inner join MagentoOnlineshop.dbo.sales_order_payment sop on so.entity_id = sop.parent_id left join reporting.dbo.sales_order_item_bundle_price sob on soi.order_id = sob.order_id and soi.item_id = sob.item_id left join MagentoOnlineshop.dbo.sales_order_item parent_soi on soi.parent_item_id = parent_soi.[ITEM_ID] and parent_soi.product_type = 'bundle' left join ConsumerDB_2.dbo.CUSTOMER c on so.customer_consumer_db_id = c.customer_code where so.increment_id in ('61000000392', '61000000393', '61000000394')" ) #ここでクエリの記載
rows = cursor.fetchall()
pprint.pprint( rows )

cursor.close()
con.close()

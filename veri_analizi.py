import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

conn = sqlite3.connect('olist_ecommerce.db')

customers_df = pd.read_csv('olist_customers_dataset.csv')
orders_df = pd.read_csv('olist_orders_dataset.csv')
order_items_df = pd.read_csv('olist_order_items_dataset.csv')

customers_df.to_sql('customers', conn, if_exists='replace', index=False)
orders_df.to_sql('orders', conn, if_exists='replace', index=False)
order_items_df.to_sql('order_items', conn, if_exists='replace', index=False)

query = """
SELECT 
    c.customer_state as eyalet, 
    COUNT(DISTINCT o.order_id) as toplam_siparis,
    SUM(oi.price) as toplam_ciro
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
WHERE o.order_status = 'delivered'
GROUP BY c.customer_state
ORDER BY toplam_ciro DESC
LIMIT 10;
"""

df = pd.read_sql_query(query, conn)

plt.figure(figsize=(10, 6))
sns.barplot(x='eyalet', y='toplam_ciro', data=df, palette='viridis')

plt.title('En Cok Ciro Yapan 10 Eyalet')
plt.xlabel('Eyaletler')
plt.ylabel('Toplam Ciro (BRL)')
plt.tight_layout()

plt.savefig('eyalet_ciro_analizi.png')

conn.close()

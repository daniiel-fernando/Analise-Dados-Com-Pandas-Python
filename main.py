from data_loader import load_data
from data_cleaner import DataCleaner
from eda import EDA
from analysis import DetailedAnalysis
from visualization import plot_bar_chart

orders_path = 'orders.csv'
customers_path = 'customers.csv'
products_path = 'products.csv'

orders = load_data(orders_path, create_if_not_exist=True, data_if_empty='order_id,order_date,total_amount\n1,2021-01-01,100.50\n')
customers = load_data(customers_path, create_if_not_exist=True, data_if_empty='customer_id,name\n')
products = load_data(products_path, create_if_not_exist=True, data_if_empty='product_id,name,price\n')

cleaner = DataCleaner(orders)
cleaner.remove_duplicates()
cleaner.convert_to_datetime('order_date')
orders = cleaner.get_cleaned_data()

eda = EDA(orders)
print(eda.descriptive_stats())
eda.plot_time_series('order_date', 'total_amount')

analysis = DetailedAnalysis(orders)
monthly_sales = analysis.analyze_seasonality()
print(monthly_sales)

customer_segments = analysis.customer_segmentation(customers)
print(customer_segments.describe())

plot_bar_chart(monthly_sales.index, monthly_sales.values, 'Vendas Mensais', 'Mês', 'Total Vendido')

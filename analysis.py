class DetailedAnalysis:
    def __init__(self, df):
        self.df = df

    def analyze_seasonality(self):
        self.df['month'] = self.df['order_date'].dt.month
        monthly_sales = self.df.groupby('month')['total_amount'].sum()
        return monthly_sales

    def customer_segmentation(self, customer_df):
        customer_segments = customer_df.groupby('customer_id').agg({
            'order_id': 'count',
            'total_amount': 'sum'
        })
        return customer_segments

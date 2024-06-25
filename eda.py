import pandas as pd
import matplotlib.pyplot as plt

class EDA:
    def __init__(self, df):
        self.df = df

    def descriptive_stats(self):
        return self.df.describe()

    def plot_time_series(self, date_column, value_column):
        self.df.set_index(date_column)[value_column].plot(figsize=(10, 6))
        plt.title('Vendas ao Longo do Tempo')
        plt.ylabel('Total Vendido')
        plt.xlabel('Data')
        plt.show()

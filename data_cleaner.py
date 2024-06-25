import pandas as pd

class DataCleaner:
    def __init__(self, df):
        self.df = df

    def remove_duplicates(self):
        self.df = self.df.drop_duplicates()

    def convert_to_datetime(self, column):
        self.df[column] = pd.to_datetime(self.df[column])

    def fill_missing_values(self, column, value):
        self.df[column] = self.df[column].fillna(value)

    def get_cleaned_data(self):
        return self.df

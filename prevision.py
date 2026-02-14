from database import engine
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

class PricePredictor:
    def __init__(self):
        self.model = LinearRegression()

    def get_data(self, product_name):
        query = f"SELECT \"Price\", \"Date\" FROM public.\"History\" WHERE \"Product\" = '{product_name}' ORDER BY \"Date\" ASC"
        try:
            with engine.connect() as connection:
                df = pd.read_sql(query, connection)
            df["Price"] = pd.to_numeric(df["Price"], errors='coerce')
            df = df.dropna(subset=["Price"])
            return df
        except Exception as e:
            print(f"Prediction Error for {product_name}: {e}")
            return pd.DataFrame()

    def calculate_probabilities(self, product_name):
        df = self.get_data(product_name)
        if len(df) < 3:
            return 50.0, 50.0
        X = np.array(range(len(df))).reshape(-1, 1)
        y = df["Price"].values
        self.model.fit(X, y)
        slope = self.model.coef_[0]
        if slope < 0:
            drop_prob = min(85, 50 + abs(slope / 10))
            rise_prob = 100 - drop_prob
        else:
            rise_prob = min(85, 50 + (slope / 10))
            drop_prob = 100 - rise_prob
            

        return round(drop_prob, 1), round(rise_prob, 1)

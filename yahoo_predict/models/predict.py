from ..database import engine
import pandas as pd

class PredictModel:
    def __init__(self):
        pass
    
    def get_dataset(self):
        query = "SELECT * FROM stock_data"
        df = pd.read_sql_query(query, engine)
        return df

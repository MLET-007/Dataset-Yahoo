from ..database import engine
from datetime import datetime
from sqlalchemy import text

class StockModel:
    def __init__(self, database):
        self.database = database

    def save_data(self, data):
        try:
            expected_columns = ['date', 'open', 'high', 'low', 'close', 'adj_close', 'volume', 'symbol']
            data.columns = expected_columns
            
            with self.database.begin() as conn:
                data.to_sql('stock_data', con=conn, if_exists='append', index=False)
        except Exception as e:
            print(f"Error saving data to database: {e}")
            raise
        
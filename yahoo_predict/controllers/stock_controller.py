import yfinance as yf
from yahoo_predict.models.stock import StockModel
from yahoo_predict.database import engine

class StockController:
    def __init__(self):
        self.stock_model = StockModel(engine)

    def import_data(self, ticker):
        # Download data and add symbol column
        data = yf.download(ticker)
        data['Symbol'] = ticker
        data['id'] = data.index
        
        # Select and rename columns in one step with a mapping
        column_mapping = {
            'Date': 'date',
            'Open': 'open',
            'High': 'high',
            'Low': 'low',
            'Close': 'close',
            'Adj Close': 'adj_close',
            'Volume': 'volume',
            'Symbol': 'symbol'
        }


        data = data.reset_index()  # Move Date from index to column
        # remove head of dataframe
        data = data.rename(columns=column_mapping)[column_mapping.values()]
        
        # Save to database
        self.stock_model.save_data(data)
        return {"message": "Data imported successfully"}

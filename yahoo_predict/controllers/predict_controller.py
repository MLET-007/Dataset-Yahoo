from pathlib import Path
import tensorflow as tf
from yahoo_predict.models.predict import PredictModel
import yfinance as yf

class PredictController:
    def __init__(self):
        model_path = Path(__file__).parent.parent.parent.joinpath('modelo_dis_v1.keras')
        self.model = tf.keras.models.load_model(model_path, safe_mode=False)


    def predict(self,):
        shuffle_buffer_size = 1000
        window_size = 5
        batch_size = 32

        dataset = self.get_dataset()

        try:
            result = self.model_forecast(self.model, dataset, window_size, batch_size)

            final_result = result.squeeze()

            cast_result = float(final_result)

            return f"Resultado previsto: {round(cast_result, 2)}"
        except Exception as e:
            print("Error predicting")
            print(e)
            return None


    def model_forecast(self, model, series, window_size, batch_size):
        series = tf.expand_dims(series, axis=-1)

        dataset = tf.data.Dataset.from_tensor_slices(series)

        dataset = dataset.window(window_size, shift=1, drop_remainder=True)

        dataset = dataset.flat_map(lambda w: w.batch(window_size))

        dataset = dataset.batch(batch_size).prefetch(1)

        forecast = model.predict(dataset, verbose=0)

        return forecast
    
    def get_dataset(self):
        try:
            # dataset = self.predict_model.get_dataset()
            symbol = 'DIS'
            df2 = yf.download(symbol)
            df_tail = df2.tail(5)

            forecast_series2 = df_tail['Close']

            return forecast_series2
        except Exception as e:
            print(e)
            return None

        return dataset

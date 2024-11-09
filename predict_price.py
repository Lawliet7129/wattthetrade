import matlab.engine
import json

def get_forecasted_price(historical_data):
    eng = matlab.engine.start_matlab()
    price = eng.forecastPrice(historical_data)
    eng.quit()
    return price

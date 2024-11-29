import yfinance as yf
from pandas import DataFrame


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data

def calculate_and_display_average_price(data:DataFrame):
    if 'Close' not in data.columns:
        raise ValueError("DataFrame does not contain 'Close' column")
    total_sum = data['Close'].sum()
    count = data['Close'].count()
    average_price = round(total_sum / count, 2)
    return average_price
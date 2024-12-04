import os

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
    '''
    функция вычисляющая среднюю цену фкций за заданный период при закрытии'''
    if 'Close' not in data.columns:
        raise ValueError("DataFrame does not contain 'Close' column")
    total_sum = data['Close'].sum()
    count = data['Close'].count()
    average_price = round(total_sum / count, 2)
    return f' average price closed: {average_price}'

def notify_if_strong_fluctuations(data:DataFrame, threshold: int):
    '''Функция которая отправляет уведомление пользователю если цена закрытия
     колебалась на указанный  процент в период времени введенным пользователем'''
    if not isinstance(threshold, int):
        raise ValueError("Threshold must be integer")
    if 'Close' not in data.columns:
        raise ValueError("DataFrame does not contain 'Close' column")
    max_price_close = data['Close'].max()
    min_price_close = data['Close'].min()
    difference = max_price_close - min_price_close
    percentage_difference = (difference / min_price_close) * 100
    if percentage_difference > threshold:
        print(f"Уведомление: Цена акций колебалась более чем на {threshold}% за период.")

def export_data_to_csv(data:DataFrame, filename):
    data.to_csv(filename, index=False)
    if os.path.isfile(filename):
        print("Export success")
    else:
        raise FileExistsError("Export not success")

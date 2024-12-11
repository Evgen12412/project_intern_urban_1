import os
from datetime import datetime

import ta
import yfinance as yf
from pandas import DataFrame


def fetch_stock_data(ticker, start=None, end=None, period='1mo'):
    stock = yf.Ticker(ticker)

    # Проверка формата дат
    if start is not None:
        if start.strip() == '':
            start = None
        else:
            try:
                start = datetime.strptime(start, '%Y-%m-%d')


            except ValueError:
                print("Ошибка: Дата начала не имеет распознаваемого формата. Используйте формат 'YYYY-MM-DD'.")

    if end is not None:
        if end.strip() == '':
            end = None
        else:
            try:
                end = datetime.strptime(end, '%Y-%m-%d')
            except ValueError:
                print("Ошибка: Дата конца не имеет распознаваемого формата. Используйте формат 'YYYY-MM-DD'.")

    # Если start и end не указаны, используем период по умолчанию
    if start is None and end is None:
        data = stock.history(period=period)
    else:
        data = stock.history(start=start, end=end)

    # Проверка на наличие данных
    if data.empty:
        print(f"Ошибка: Данные для тикера {ticker} в указанном диапазоне дат отсутствуют.")
        return None

    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data: DataFrame):
    '''
    функция вычисляющая среднюю цену акций за заданный период при закрытии'''
    if 'Close' not in data.columns:
        raise ValueError("DataFrame does not contain 'Close' column")
    total_sum = data['Close'].sum()
    count = data['Close'].count()
    average_price = round(total_sum / count, 2)
    return f' average price closed: {average_price}'


def notify_if_strong_fluctuations(data: DataFrame, threshold: int):
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


def export_data_to_csv(data: DataFrame, filename):
    '''Функция экспорта данных в файл '''
    data.to_csv(filename, index=False)
    if os.path.isfile(filename):
        print("Export success")
    else:
        raise FileExistsError("Export not success")


def calculate_rsi(data: DataFrame, window=14):
    # Расчет RSI с использованием библиотеки ta
    data['RSI'] = ta.momentum.RSIIndicator(data['Close'], window=window).rsi()
    print(data[['Close', 'RSI']])

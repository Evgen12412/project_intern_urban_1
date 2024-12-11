import matplotlib.pyplot as plt
import pandas as pd


def create_and_save_plot(data, ticker, period, style, filename=None):
    plt.figure(figsize=(10, 6))
    if style is None or style == '':
        plt.style.use('default')
    elif style == 'cl':
        plt.style.use('classic')
    elif style == 'd':
        plt.style.use('dark_background')
    else:
        raise ValueError("Введеное значение не верно. Выберите нужное")

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')

    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")


def create_and_show_rsi_plot(data, ticker, period, filename=None):
    plt.figure(figsize=(14, 8))

    # Создаем две оси: одну для цены и скользящей средней, другую для RSI
    ax1 = plt.subplot(2, 1, 1)
    ax2 = plt.subplot(2, 1, 2, sharex=ax1)

    # График цены закрытия и скользящей средней на первой оси
    ax1.plot(data.index, data['Close'], label='Close Price')
    ax1.plot(data.index, data['Moving_Average'], label='Moving Average')
    ax1.set_title(f"{ticker} Цена акций с течением времени")
    ax1.set_ylabel("Цена")
    ax1.legend()

    # График RSI на второй оси
    ax2.plot(data.index, data['RSI'], label='RSI', color='orange')
    ax2.set_title("RSI")
    ax2.set_xlabel("Дата")
    ax2.set_ylabel("RSI")
    ax2.legend()

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")

    plt.savefig(filename)
    print(f"График сохранен как {filename}")

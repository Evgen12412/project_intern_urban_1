import data_download as dd
import data_plotting as dplt


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print(
        "Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print()
    print(
        "Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")
    print()
    print(
        "Так же вы можете задать дату начала временного периода и дату конца периода в формате например(start - 2023-10-01 и. конец - 2023-11-10) будет показан период с 1 числа до 10 го не включительно")
    print(
        "Так же следует учесть что если вы у казали период 1mo то и при указании конкретнной даты учитывайте что будет показан промежуток за указанный период")
    print("Если вы не хотите устанавливать дату начало и конца просто нажмите enter")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    period = input("Введите период для данных (например, '1mo' для одного месяца): ")
    start = input("Введите дату начала периода (например, '2023-10-01'): ")
    end = input("Введите дату конца периода (например, '2023-11-10'): ")
    style = input("Вы можете выбрать отображения графика в определенном стиле для этого введите cl(classic) или d(dark_background)")

    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, start, end, period)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # Show average close price average_price
    average_price = dd.calculate_and_display_average_price(stock_data)
    print(average_price)

    # warning the user about the price threshold
    dd.notify_if_strong_fluctuations(stock_data, 10)

    # export data to csv
    dd.export_data_to_csv(stock_data, 'output.csv')

    # calculate rsi
    dd.calculate_rsi(stock_data)

    # new indicators
    dd.calculate_and_display_indicators(stock_data)

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period, style)

    # Plot the rsi
    dplt.create_and_show_rsi_plot(stock_data, ticker, period)

    dplt.create_and_save_plot_indicators(stock_data, ticker, period, style)


if __name__ == "__main__":
    main()

# Получение уведомления
На первом скриншоте видно что приходит уведомление что за указанный период цена закрытия колебалась
более 10%

![img_1.png](img_1.png)

# Экспорт данных в файл
так же в программе предусмотрен экспорт данных в csv файл

![img_2.png](img_2.png)

# Отображения rsi на графике 
за отображение отвечает функция: <br>
def create_and_show_rsi_plot(data, ticker, period, filename=None):

а за вычисление: <br>
def calculate_rsi(data: DataFrame, window=14):

![img_3.png](img_3.png)
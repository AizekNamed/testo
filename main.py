import schedule
import time


# создать конфиг для проведения испытаний
app_config = Config(text_config_data)

# создать класс для работы с qt-приложениями
compute_auto = Compute_auto()

# создать класс для работы с web-приложением
web_auto  	 = Web_auto()

# создать класс парсинга и преобразования данных
parser       = Parser_data()


# запустить iot vega sever, настроечный и пользовательский конфигуратор
compute_auto.start_app("vega")
compute_auto.start_app("config")
compute_auto.start_app("user")


scenario = new Scenario(text_scenario)

computer_auto.set_scenario(scenario.comp)
web_auto.set_scenario(scenario.web)


def plunnig_data():
    # выполнить действия по расписанию - накликать данные, отправить
    computer_auto.act()
    web_auto.act()


# возвращаем такой токен, и это задание снимается с выполнения в будущем
    return schedule.CancelJob


schedule.every(10).minute.at().do(plunnig_data)


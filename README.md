# Diploma-work-on-automation
Дипломная работа по автоматизации тестирования на основании финальной курсовой работы по ручному тестированию.

Здесь находяться немного автотестов для проверки API и UI интернет-магазина "Читай-город" https://www.chitai-gorod.ru/

**Перед запуском автотестов для API** (tests\test_api.py), следует подставить **актуальный токен авторизации** в файл с данными для тестов (tests\DataForTests.py). Для этого нужно быть авторизованным на сайте интернет-магазина, и через devtools из любого запроса вытащить даннный токен из заголовков. Подробнее можете посмотреть по ссылке ниже.
Ссылка на короткое видео по токену (откуда взять и куда вставить): **https://skrinshoter.ru/vTuPrFE4R9t**

Для запуска тестов с использованием отчетов Allure используйте команды в терминале:
**pytest tests\test_api.py --alluredir=./allure-result** - для запуска API тестов
**pytest tests\test_ui.py --alluredir=./allure-result** - для запуска UI тестов
**pytest tests\test_api.py tests\test_ui.py --alluredir=./allure-result** - запуск всех тестов

Чтобы просмотреть отчет о тестировании Allure используйте команду в терминале:
**allure serve allure-result**

Для запуска тестов без отчетности Allure используйте команды в терминале:
**pytest tests\test_api.py**
**pytest tests\test_ui.py**
**pytest tests\test_api.py tests\test_ui.py**


Настоятельно рекомендую при прогоне UI тестов уберите курсор мыши с окна отрывающегося браузера, так как могут возникнуть определенные проблемы с результатами тестов.



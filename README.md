Проект: Генератор Облака Слов

Описание:
Данное приложение предназначено для анализа текстов, содержащихся в JSON файле, и формирования облака слов с объединением синонимов. Используются современные NLP методы для обработки слов, их нормализации, а также для нахождения синонимичных слов по семантической близости.

Основные функции:
1.Загрузка и чтение слов из JSON файла.
2.Обработка слов с помощью библиотеки pymorphy3 для нормализации и фильтрации.
3.Сравнение слов с использованием модели SentenceTransformer для нахождения семантических синонимов.
4.Вывод итогового результата в JSON файл.

Установка и Запуск
Шаги для установки:
1.Клонировать репозиторий:

bash
git clone https://github.com/your-repository-url.git
2.Перейти в директорию проекта:

bash
cd your-project-directory
3.Установить все необходимые зависимости:

bash
pip install -r requirements.txt

bash
python main.py

Зависимости:
Python 3.8+
pymorphy3
sentence-transformers
nltk
deep-translator
jsonschema

Запуск программы:
Для запуска программы используйте следующую команду:
bash
python main.py
После запуска программа предложит ввести путь к JSON файлу, который должен содержать список слов для анализа.

Использование:
Подготовьте JSON файл со словами. Пример формата файла:
json
[
  "слово1",
  "слово2",
  "слово3"
]
При запуске программа прочтет этот файл, произведет обработку, объединит синонимичные слова, а затем выведет результаты и сохранит их в новый JSON файл (synonyms.json) в папке output.

Пример работы
1.Загрузите .JSON файл
Программа проведет анализ и выведет на экран объединенные слова с их количеством:
 
2.Анализ завершен. Список объединенных слов:
слово1: 3
слово2: 2
Результат будет также сохранен в файл output/synonyms.json.

Структура проекта:
main.py - Основной файл программы для запуска.
index.py - Логика обработки синонимов.
reading_file.py - Чтение и валидация JSON файла.
word_processing.py - Обработка слов, нормализация и фильтрация.
data/mat.txt - Список нежелательных слов (матерных).
output/ - Папка для сохранения результатов анализа.

Лицензия
Данный проект распространяется под лицензией MIT.

Сделано командой "русские слоны"

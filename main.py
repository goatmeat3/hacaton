import os
import json
from index import merge_synonyms
from reading_file import read_word_from_json


def main():
    # Убедимся, что папка для вывода существует
    SAVE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output')
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)

    # Запросить у пользователя путь к JSON файлу
    file_path = input("Введите путь к JSON файлу: ").strip()

    # Проверяем, существует ли файл
    if not os.path.exists(file_path):
        print("Ошибка: Файл не найден!")
        return

    # Анализ файла и вывод результата
    try:
        word_counts = read_word_from_json(file_path)
        merged_words = merge_synonyms(file_path)

        # Печать результата анализа
        print("\nАнализ завершен. Список объединенных слов:")
        for word, count in merged_words.items():
            print(f"{word}: {count}")

        # Сохранение результата в файл
        output_path = os.path.join(SAVE_DIR, 'synonyms.json')
        with open(output_path, 'w', encoding='utf-8') as json_file:
            json.dump(merged_words, json_file, ensure_ascii=False, indent=4)

        print(f"\nРезультат сохранен в файл: {output_path}")

    except Exception as e:
        print(f"Произошла ошибка при обработке файла: {e}")


if __name__ == '__main__':
    main()

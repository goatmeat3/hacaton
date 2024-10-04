import os
import json
from index import merge_synonyms

SAVE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output')  # Папка для сохранения результатов

# Убедимся, что папка 'output' существует
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)


def main():
    print("Добро пожаловать в Генератор Облака Слов с Объединением Синонимов!\n")

    while True:
        print("\nПожалуйста, введите полный путь к вашему JSON файлу (или 'exit' для выхода):")
        file_path = input("> ")

        # Условие для выхода из программы
        if file_path.lower() == 'exit':
            print("Программа завершена. До свидания!")
            break

        # Проверка на существование файла
        if not os.path.exists(file_path) or not file_path.endswith('.json'):
            print(f"Ошибка: файл {file_path} не найден или имеет неверный формат. Попробуйте снова.")
            continue

        try:
            # Получаем объединённые синонимы
            merged_words = merge_synonyms(file_path)
            
            print("\nАнализ завершен. Список объединенных слов:")
            for word, count in merged_words.items():
                print(f"{word}: {count}")

            # Путь для сохранения нового JSON файла с результатами
            output_path = os.path.join(SAVE_DIR, 'synonyms.json')

            # Сохранение результата в файл
            with open(output_path, 'w', encoding='utf-8') as json_file:
                json.dump(merged_words, json_file, ensure_ascii=False, indent=4)

            print(f"Результаты анализа сохранены в {output_path}")

        except Exception as e:
            print(f"Произошла ошибка: {e}. Попробуйте снова.")

        # Запрос на повторное выполнение программы
        print("\nХотите обработать другой файл? (да/нет):")
        retry = input("> ")
        if retry.lower() not in ['да', 'yes']:
            print("Программа завершена. До свидания!")
            break


if __name__ == '__main__':
    main()

import json
from jsonschema import validate, ValidationError
from word_processing import process_word

def read_word_from_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

            # Проверка валидности структуры JSON
            schema = {
                "type": "array",
                "items": {"type": "string"},
                "minItems": 1
            }

            validate(instance=data, schema=schema)

            word_count = {}
            for word in data:
                processed_word = process_word(word)
                if processed_word:
                    if processed_word not in word_count:
                        word_count[processed_word] = 1
                    else:
                        word_count[processed_word] += 1

            return word_count

    except FileNotFoundError:
        print(f"Ошибка: Файл не найден.")
    except ValidationError as e:
        print(f"Ошибка валидации JSON: {e}")
    except json.JSONDecodeError:
        print("Ошибка чтения JSON файла.")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
